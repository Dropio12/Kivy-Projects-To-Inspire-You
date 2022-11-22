
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict

from kivy.clock import Clock

from kivy.properties import StringProperty, ObjectProperty, ListProperty, ColorProperty, NumericProperty
from widgets.articles import ArticleCard

Builder.load_file('views/fav/fav.kv')
class Fav(BoxLayout):
    date = StringProperty("04/05/2022")
    articles = ObjectProperty(allownone=True)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        pass

    def on_articles(self, inst, articles):
        grid = self.ids.gl_fav
        grid.clear_widgets()

        for a in articles:
            content = a.get('content')
            cover = a.get("image_url")

            if not cover:
                cover = ""

            if not content:
                content = a['description']

            art = ArticleCard()
            art.title = a['title']
            art.publisher = a['source_id']
            art.cover = cover
            art.date = a['pubDate']
            art.bookmarked = False
            art.link = a['link']
            art.content = content

            grid.add_widget(art)
    