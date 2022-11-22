from threading import Thread
import pickle
import json

from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock, mainthread
from kivy.properties import ColorProperty, ObjectProperty, BooleanProperty, ListProperty, StringProperty, NumericProperty

from api import get_latest
class MainWindow(BoxLayout):
    articles = ObjectProperty(allownone=True)
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.render, .2)

    def render(self, _):
        t1 = Thread(target=self.get_data, daemon=True)
        t1.start()
        
    @mainthread
    def on_articles(self, inst, articles):
        if articles:
            articles = articles['results']
            self.ids.home.articles = articles
            self.ids.news_list.articles = articles
            self.ids.fav.articles = articles
    
    def get_data(self):
        self.articles = get_latest()
