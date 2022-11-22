from kivy.app import App
from kivy.lang import Builder
from kivy.uix.slider import Slider
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict

Builder.load_string('''
<SmoothSlider>:
    max: 100
    min: 0
    value: 34
    cursor_image: "assets/imgs/data/slider_cursor.png"
    background_horizontal: "assets/imgs/data/slider_bg.png"
    background_width: dp(2)
    cursor_size: [dp(16), dp(16)]
    value_track_color: app.colors.secondary
    value_track: True
    value_track_width: dp(2)
''')

class SmoothSlider(Slider):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
