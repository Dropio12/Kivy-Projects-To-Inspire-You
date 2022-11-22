
from cgitb import text
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.togglebutton import ToggleButton
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.clock import Clock, mainthread
from kivy.properties import StringProperty, ListProperty, ColorProperty, NumericProperty, BooleanProperty

from kivy.garden.graph import LinePlot

Builder.load_file('views/home/home.kv')
class Home(BoxLayout):
    air_value = NumericProperty(15)
    light_value = NumericProperty(75)
    chart_data = ListProperty([(0,0), (1,3)])
    current_feed = StringProperty("assets/imgs/porch.png")

    # Room Specs
    temperature = NumericProperty(29)
    curtains = BooleanProperty(True)
    lights = BooleanProperty(True)
    devices = ListProperty([])
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        users = [
            {
                "id": "00",
                "name": "Samuel M",
                "avatar": "assets/imgs/avatar.jpg",
            },
            {
                "id": "01",
                "name": "Julia M",
                "avatar": "assets/imgs/avatar-2.png",
            },
            {
                "id": "02",
                "name": "Angela M",
                "avatar": "assets/imgs/avatar-3.png",
            },
            {
                "id": "03",
                "name": "Shikamaru N",
                "avatar": "assets/imgs/avatar-4.png",
            },
            {
                "id": "04",
                "name": "Zabuza M",
                "avatar": "assets/imgs/avatar-1.png",
            },
        ]

        gl = self.ids.gl_users
        gl.clear_widgets()
        for u in users:
            us = User()
            us.text = u['name']
            us.source = u['avatar']

            gl.add_widget(us)

        graph = self.ids.graph
        plot = LinePlot()
        plot.line_width = dp(1.5)
        plot.color = App.get_running_app().colors.tertiary_light
        graph.add_plot(plot)

        points = [
            (0,10),
            (1,40),
            (2,15),
            (3,25),
            (4,45),
            (5,50),
            (6,60),
            (7,35),
            (8,80),
            (9,63),
            (10,75),
        ]

        plot.points = points
        self.chart_data = points

        feed = [
            {
                "text": "Front Porch",
                "source": "assets/imgs/porch.png",
            },
            {
                "text": "Living Room",
                "source": "assets/imgs/living-room.png",
            },
            {
                "text": "Kitchen",
                "source": "assets/imgs/kitchen.png",
            },
            {
                "text": "Bedroom 01",
                "source": "assets/imgs/bedroom-01.png",
            },
            {
                "text": "Bedroom 02",
                "source": "assets/imgs/bedroom-02.png",
            },
        ]

        gl_feed = self.ids.gl_feed
        gl_feed.clear_widgets()
        for i,f in enumerate(feed):
            f1 = FeedTab()
            f1.text = f['text']
            f1.source = f['source']
            f1.bind(state=self.update_feed)

            if i == 0:
                f1.state = "down"

            gl_feed.add_widget(f1)
        
        self.update_room("LIVING ROOM")
    
    @mainthread
    def update_feed(self, inst, value):
        if value == "down":
            self.current_feed = inst.source
    
    def update_room(self, room):
        rooms = [
            {
                "text": "LIVING ROOM",
                "temperature": 29,
                "curtains": True,
                "lights": True,
                "devices": [
                    {
                        "text": "Aircon",
                        "on": True,
                    },
                    {
                        "text": "Lights",
                        "on": True,
                    },
                    {
                        "text": "Curtains",
                        "on": True,
                    },
                    {
                        "text": "Tv",
                        "on": True,
                    },
                    {
                        "text": "Nest Speaker",
                        "on": False,
                    },
                    {
                        "text": "Smart Socket",
                        "on": False,
                    },
                ]
            },
            {
                "text": "DINING ROOM",
                "temperature": 24,
                "curtains": True,
                "lights": False,
                "devices": [
                    {
                        "text": "Aircon",
                        "on": True,
                    },
                    {
                        "text": "Lights",
                        "on": True,
                    },
                    {
                        "text": "Tv",
                        "on": True,
                    },
                ]
            },
            {
                "text": "KITCHEN",
                "temperature": 26,
                "curtains": False,
                "lights": False,
                "devices": [
                    {
                        "text": "Aircon",
                        "on": True,
                    },
                    {
                        "text": "Lights",
                        "on": True,
                    },
                    {
                        "text": "Nest Speaker",
                        "on": False,
                    }
                ]
            },
            {
                "text": "BEDROOM 01",
                "temperature": 16,
                "curtains": True,
                "lights": False,
                "devices": [
                    {
                        "text": "Aircon",
                        "on": True,
                    },
                    {
                        "text": "Lights",
                        "on": True,
                    },
                    {
                        "text": "Nest Speaker",
                        "on": False,
                    }
                ]
            },
            {
                "text": "BEDROOM 02",
                "temperature": 18.5,
                "curtains": True,
                "lights": True,
                "devices": [
                    {
                        "text": "Aircon",
                        "on": True,
                    },
                    {
                        "text": "Lights",
                        "on": True,
                    },
                    {
                        "text": "Nest Speaker",
                        "on": True,
                    }
                ]
            },
        ]
        
        tgt = [z for z in rooms if z['text'] == room]

        if len(tgt) > 0:
            tgt = tgt[0]

            # Update values
            self.temperature = tgt['temperature']
            self.curtains = tgt['curtains']
            self.lights = tgt['lights']
            self.devices = tgt['devices']

    def update_aircon(self, value: int) -> None:
        self.air_value = value
    
    def update_lights(self, value: int) -> None:
        self.light_value = value
    
class Room(BoxLayout):
    text = StringProperty("")
    source = StringProperty("")
    devices = ListProperty([])
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

    def on_devices(self, inst, devices):
        grid = self.ids.gl_devices
        grid.clear_widgets()

        for i,d in enumerate(devices):
            dev = Device()
            dev.text = d['text']
            dev.on = d['on']

            if i == len(devices)-1:
                dev.show_border = False

            grid.add_widget(dev)
    
class User(BoxLayout):
    text = StringProperty("")
    source = StringProperty("")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
    
class QuickDevice(BoxLayout):
    text = StringProperty("")
    icon = StringProperty("")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

class Device(BoxLayout):
    text = StringProperty("")
    on = BooleanProperty(False)
    show_border = BooleanProperty(True)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

    def toggle_device(self):
        if self.on:
            self.on = False
        else:
            self.on = True

class FeedTab(ToggleButton):
    source = StringProperty("")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

class RoomTabs(ToggleButton):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)