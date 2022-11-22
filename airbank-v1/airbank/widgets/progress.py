from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.properties import ColorProperty, ObjectProperty, BooleanProperty, ListProperty, StringProperty, NumericProperty
Builder.load_string('''
<SProgressBar>:
    size_hint_y: None
    height: dp(8)
    canvas.before:
        Color:
            rgba: self.bg_color
        RoundedRectangle:
            size: self.size[0], self.size[1]
            pos: self.pos
            radius: [dp(4)]
        Color:
            rgba: self.fg_color
        RoundedRectangle:
            size: (self.value/self.pmax)*self.size[0], self.size[1]
            pos: self.pos
            radius: [dp(4)]
''')
class SProgressBar(Widget):
    bg_color = ColorProperty([1,1,1,1])
    fg_color = ColorProperty([1,1,1,1])
    pmax = NumericProperty(100)
    value = NumericProperty(100)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

    def on_value(self, _, val):
        print("VALUE: ", val)
