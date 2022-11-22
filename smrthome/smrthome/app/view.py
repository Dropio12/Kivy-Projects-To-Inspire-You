
from tokenize import String
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ColorProperty, ObjectProperty, BooleanProperty, ListProperty, StringProperty, NumericProperty

class MainWindow(BoxLayout):
    username = StringProperty("Sam")
    avatar = StringProperty("assets/imgs/avatar.jpg")
    def __init__(self, **kw):
        super().__init__(**kw)

class NavTabs(BoxLayout):
    text = StringProperty("")
    active = BooleanProperty(False)
    state = StringProperty("normal")
    def __init__(self, **kw):
        super().__init__(**kw)

    def handle_state(self, inst, value):
        if value == "down":
            self.active = True
        else:
            self.active = False
