from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.properties import ColorProperty, ObjectProperty, BooleanProperty, ListProperty, StringProperty, NumericProperty
from kivy.clock import Clock, mainthread
from kivy.animation import Animation

from widgets.hover import HoverBehavior

Builder.load_string('''
<SideBarBase>:
    RelativeLayout:
        id: rl
        BoxLayout:
            BoxLayout:
                id: sidebar
                size_hint_x: None
                width: root.sidebar_width
            Widget:
        SideBarMain:
            id: main_content
            size_hint_y: 1*(1-self._width_hint) if root.scale_content else 1
            pos_hint: {"x": self._width_hint, "center_y": .5}
<SlideSideBar>:
    RelativeLayout:
        id: rl
        BoxLayout:
            BoxLayout:
                id: sidebar
                size_hint_x: None
                width: root.bar_offset
            Widget:
        BoxLayout:
            SideBarSmoother:
                id: smoother
                size_hint_x: None
                width: root.bar_offset
                hover_callback: root.toggle_drawer
            SideBarMain:
                id: main_content
            BoxLayout:
                id: collapsible
                size_hint_x: None
                width: 0
                
''')
class SideBarMain(BoxLayout):
    _width_hint = NumericProperty(0)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

class SideBarSmoother(HoverBehavior, Widget):
    hover_callback = ObjectProperty(print)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

    def on_enter(self, *args):
        self.hover_callback(True)

    def on_leave(self, *args):
        self.hover_callback(True)

class SideBarBase(BoxLayout):
    sidebar_width = NumericProperty(dp(0))
    anim_duration = NumericProperty(.2)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
    
    def toggle_drawer(self):
        side = self.ids.sidebar
        move_val = .1
        move = self.sidebar_width/move_val
        if side.width == self.sidebar_width:
            side.width = 0
            self._animate(0)
        else:
            side.width = self.sidebar_width
            self._animate(self.sidebar_width)
    
    def _animate(self, x):
        main = self.ids.main_content
        if x == 0:
            width = 0
        else:
            width = x/self.width

        anim = Animation(_width_hint=width, d=self.anim_duration)
        anim.start(main)
        # main.pos_hint = {"x": width}

    def add_widget(self, widget, index=0):
        if len(self.children) == 0:
            super().add_widget(widget, index=index)
            return

        if len(self.ids.sidebar.children) == 0:
            self.ids.sidebar.add_widget(widget, index=index)
        else:
            self.ids.main_content.add_widget(widget, index=index)
    
    def remove_widget(self, widget):
        try:
            self.ids.sidebar.remove_widget(widget)
        except:
            try:
                self.ids.main_content.remove_widget(widget)
            except:
                pass
        
    def clear_widgets(self, widgets=[]):
        self.ids.sidebar.clear_widgets()
        self.ids.main_content.clear_widgets()

class SlideSideBar(BoxLayout):
    sidebar_width = NumericProperty(dp(0))
    collapsible_width = NumericProperty(dp(0))
    anim_duration = NumericProperty(.2)
    bar_offset = NumericProperty(dp(42))
    slide_on_hover = BooleanProperty(True)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

    def toggle_collapsible(self):
        """ 
            Open or close far right collapsible content
        """

        tgt = self.ids.collapsible
        if (tgt.width == 0):
            self._animate(self.collapsible_width, tgt=tgt)
        else:
            self._animate(0, tgt=tgt)

    def toggle_drawer(self, hovered: bool=False):
        if hovered:
            if not self.slide_on_hover:
                return
        side = self.ids.sidebar
        side.width = self.sidebar_width + self.bar_offset
        tgt = self.ids.smoother
        move_val = .1
        move = self.sidebar_width/move_val
        # if side.width == self.bar_offset + self.sidebar_width:
        if tgt.width != self.bar_offset:
            # side.width = 0
            self._animate(self.bar_offset, tgt=tgt)
        else:
            self._animate(self.sidebar_width + self.bar_offset, tgt=tgt)

    def _animate(self, width: float, tgt: Widget):
        """
        Animate the opening and closing of the drawer

        Args:
            width (float): The new width to animate to
        """ 
        anim = Animation(width=width, d=self.anim_duration)
        anim.start(tgt)
        

    def add_widget(self, widget, index=0):
        if len(self.children) == 0:
            super().add_widget(widget, index=index)
            return

        if len(self.ids.sidebar.children) == 0:
            self.ids.sidebar.add_widget(widget, index=index)
        elif len(self.ids.main_content.children) == 0:
            self.ids.main_content.add_widget(widget, index=index)
        else:
            self.ids.collapsible.add_widget(widget, index=index)
    
    def remove_widget(self, widget):
        try:
            self.ids.sidebar.remove_widget(widget)
        except:
            try:
                self.ids.main_content.remove_widget(widget)
            except:
                pass
        
    def clear_widgets(self, widgets=[]):
        self.ids.sidebar.clear_widgets()
        self.ids.main_content.clear_widgets()

class SideBar(SideBarBase):
    scale_content = BooleanProperty(False)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self._trigger = None
        self._current_val = 0

