from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ColorProperty, ObjectProperty, BooleanProperty, ListProperty, StringProperty, NumericProperty
from kivy.clock import Clock
from kivy.metrics import dp, sp

from kivy.garden.graph import LinePlot
from api.hooks import Client

class MainWindow(BoxLayout):
    chart_data = ListProperty([])
    def __init__(self, **kw):
        super().__init__(**kw)
        self.client = Client()
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        # Graph init

        graph = self.ids.graph
        plot = LinePlot()
        plot.line_width = dp(1.2)
        plot.color = App.get_running_app().color_primary
        graph.add_plot(plot)

        # Add creators
        creators = self.client.get_creators()
        balances = self.client.get_balance()
        self.chart_data = balances

        grid = self.ids.gl_creators
        grid.clear_widgets()
        for c in creators:
            cc = CreatorCard()
            cc.author = c['name']
            cc.username = c['username']
            cc.avatar = c['avatar']
            cc.following = c['following']

            grid.add_widget(cc)
    
    def on_chart_data(self, inst, data):
        graph = self.ids.graph
        plots = graph.plots

        if len(plots) <= 0:
            return
        
        ymax = 0
        ymin = min(data)

        pts = []
        for i, d in enumerate(data):
            pt = (i+1, d)
            pts.append(pt)

            if d > ymax:
                ymax = d
        
        graph.ymax = ymax
        graph.ymin = ymin
        plots[0].points = pts

class CreatorCard(BoxLayout):
    author = StringProperty("")
    username = StringProperty("")
    avatar = StringProperty("")
    following = BooleanProperty(False)
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def on_following(self, inst, val):
        if val:
            self.ids.following.state = "down"
        else:
            self.ids.following.state = "normal"
