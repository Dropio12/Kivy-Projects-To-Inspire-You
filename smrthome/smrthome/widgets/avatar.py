from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.properties import StringProperty

Builder.load_string('''
<Avatar>:
    canvas:
        Color:
            rgba: [1,1,1,1]
        Ellipse:
            size: self.size[0], self.size[1]
            pos: self.pos
            source: self.source
    
''')
class Avatar(Widget):
    source = StringProperty("")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
