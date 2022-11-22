from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.properties import ColorProperty, ObjectProperty, BooleanProperty, ListProperty, StringProperty, NumericProperty

Builder.load_string('''
#: import SoftBox widgets.gradient.SoftBox
#: import BackBox widgets.box.BackBox
#: import Text widgets.labels.Text

<CircularDialer>:
    SoftBox:
        radius: [self.height]
        bcolor: root.colors
        vertical: True
        padding: root.height*.07
        BackBox:
            radius: [self.height]
            padding: root.height*.05
            bcolor: root.colors[1]
            BoxLayout:
                padding: root.height*.07
                canvas.before:
                    PushMatrix:
                    Rotate: 
                        angle: 180
                        origin: self.center
                    Color:
                        rgba: [1,1,1,1]
                    Ellipse:
                        size: self.size[0], self.size[1]
                        pos: self.pos
                        source: "assets/imgs/dial-normal.png"
                    Ellipse:
                        size: self.size[0], self.size[1]
                        pos: self.pos
                        angle_start: 0
                        angle_end: (root.dial_value/root.dial_max)*360
                        source: root.dialer_source
                canvas.after:
                    PopMatrix:
                BackBox:
                    radius: [self.height]
                    padding: dp(12)
                    bcolor: root.colors[1]
                    canvas.before:
                        PushMatrix:
                        Rotate:
                            angle: 180
                            origin: self.center
                    canvas.after:
                        PopMatrix:
                    BackBox:
                        bcolor: rgba("#070c11")
                        radius: [self.height]
                        Text:
                            text: "%s[sup]o[/sup]"%round(root.dial_value,1)
                            halign: 'center'
                            valign: "middle"
                            font_size: sp(64)
                            font_name: app.fonts.body
                            color: app.colors.white
                

''')

class CircularDialer(BoxLayout):
    dial_min = NumericProperty(0)
    dial_max = NumericProperty(100)
    dial_value = NumericProperty(0)
    colors = ListProperty([rgba("#192A3C"), rgba("#000000")])
    dialer_source = StringProperty("assets/imgs/dial-active.png")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
