from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.metrics import dp, sp
from kivy.clock import Clock
from kivy.utils import rgba, QueryDict, get_random_color
from kivy.properties import ColorProperty, ObjectProperty, BooleanProperty, ListProperty, StringProperty, NumericProperty
from kivy.graphics.transformation import Matrix

Builder.load_string('''
<ArcProgress>:
    canvas.before:
        PushMatrix:
        Rotate:
            angle: -270
            origin: self.center
    canvas.after:
        PopMatrix:
    RelativeLayout:
        id: rl
<Arc>
    canvas.after:
        Color:
            rgba: self.arc_color
        Line:
            circle: [self.center_x, self.center_y, min(self.width, self.height)/2, self.arc_length[0], self.arc_length[1]]
            width: self.arc_width
    
''')
class ArcProgress(BoxLayout):
    arc_width = NumericProperty(10)
    items = ListProperty([])
    arc_max = NumericProperty(180)
    colors = ListProperty([])
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)
        self._item_end = 0

    def render(self, _):
        pass

    def update_colors(self):
        ch = list(reversed(self.ids.rl.children))

        if len(self.colors) != len(ch)+1:
            return

        for i,c in enumerate(ch[1:]):
            c.arc_color = self.colors[i]

    def on_arc_width(self, inst, width):
        for c in self.ids.rl.children:
            c.arc_width = width

    def on_colors(self, *args):
        self.update_colors()

    def on_items(self, inst, val):
        self.ids.rl.clear_widgets()
        arc = Arc()
        arc.arc_length = [0, 180]
        arc.arc_color = rgba("#c4c4c4")
        self.ids.rl.add_widget(arc)

        for i in val:
            pos = self.calc_arc_pos(i)
            arc = Arc()
            arc.arc_length = pos
            arc.arc_color = get_random_color()

            self.ids.rl.add_widget(arc)
        
        self.update_colors()

    def calc_arc_pos(self, pos) -> list:
        start = self._item_end
        end = (pos/self.arc_max)*180
        end += start

        self._item_end = end

        return [start, end]

class Arc(Widget):
    arc_length = ListProperty([0,0])
    arc_width = NumericProperty(8)
    arc_color = ColorProperty([1,1,1,1])
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
