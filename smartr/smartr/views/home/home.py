
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict

from kivy.clock import Clock
from datetime import datetime

from kivy.properties import StringProperty, BooleanProperty, ListProperty, ColorProperty, NumericProperty

Builder.load_file('views/home/home.kv')
class Home(BoxLayout):
    username = StringProperty("Samuel")
    current_song = StringProperty("Skillet - Anchor")
    song_album = StringProperty("Victorious")
    live_room = StringProperty("Living room")
    weather_city = StringProperty("Suburbs, BYO")
    current_date = StringProperty("")
    outdoor_temp = StringProperty("21")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        bc = self.ids.chart
        bc.point_colors = [(rgba("#83BAED"), rgba("#83F3FA"))]
        bc.points = [(20, 10), (15, 32), (45, 24), (87, 38), (34, 27), (98, 54), (56, 90)]
        bc.xlabels = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]

        users = [
            {
                "name": "Sam",
                "source": "assets/imgs/avatar.jpg"
            },
            {
                "name": "Sarah",
                "source": "assets/imgs/Ellipse 11-1.png"
            },
            {
                "name": "Mitchelle",
                "source": "assets/imgs/Ellipse 11.png"
            },
            {
                "name": "Grandad",
                "source": "assets/imgs/Ellipse 12.png"
            },
            {
                "name": "Grandma",
                "source": "assets/imgs/Ellipse 13.png"
            },
            {
                "name": "Beny",
                "source": "assets/imgs/Ellipse 14.png"
            },
            {
                "name": "Spot",
                "source": "assets/imgs/Ellipse 15.png"
            },
        ]

        self.ids.gl_users.clear_widgets()
        for u in users:
            user = User()
            user.name = u['name']
            user.source = u['source']

            self.ids.gl_users.add_widget(user)

        now = datetime.now()
        days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
        mnths = ['Jan', 'Feb', "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        self.current_date = "%s, %s %s"%(days[datetime.weekday(now)], now.day, mnths[now.month-1])
    
class CircularProgress(BoxLayout):
    current_temp = NumericProperty(20)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
    
    def step(self, value):
        tmp = float(self.current_temp)
        tmp += value

        if tmp < 0:
            tmp = 0

        if tmp > 40:
            tmp = 40
        self.current_temp = tmp

class Mood(BoxLayout):
    name = StringProperty("")
    text = StringProperty("")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

class User(BoxLayout):
    name = StringProperty("")
    source = StringProperty("")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

class Device(BoxLayout):
    name = StringProperty("")
    on = BooleanProperty(False)
    icon = StringProperty("")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

    def toggle_device(self):
        if self.on:
            self.on = False
        else:
            self.on = True