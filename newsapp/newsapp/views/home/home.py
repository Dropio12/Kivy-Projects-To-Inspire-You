
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict

from kivy.clock import Clock

from kivy.properties import StringProperty, ObjectProperty, ListProperty, ColorProperty, NumericProperty

Builder.load_file('views/home/home.kv')
class Home(BoxLayout):
    date = StringProperty("04/05/2022")
    articles = ObjectProperty(allownone=True)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        pass

    def on_articles(self, inst, articles):
        grid = self.ids.gl_fav
        grid1 = self.ids.gl_all
        grid.clear_widgets()
        grid1.clear_widgets()

        """
            {'title': "Drake Got Trolled On Instagram & He Followed The Guy's Wife As Payback", 'link': 'https://www.narcity.com/toronto/drake-got-trolled-on-instagram-he-followed-the-guys-wife-as-payback', 'keywords': None, 'creator': ['Patrick John Gilson'], 'video_url': None, 'description': 'Welp, Drake just reminded the internet why he\'s not to be trolled.The Toronto icon started a social media frenzy on Tuesday night after following the wife of someone who attempted to roast him and his son on Instagram.It all started when Drizzy commented on a post by Chris Matthew, an NBA shooting coach, addressing the criticism being lobbed at fathers LaVar Ball and Tee Morant\'s sideline behaviour.The post encourages people to support positive father figures no matter how they show up for their sons, with the rapper offering up his two cents on the issue. See on Instagram "Imagine your son makes the league and he\'s Ja Or Melo or Lonzo all you can do is be elated and competitive and over supportive and it\'s a right of passage to that the OG\'s talk shit I know I\'mma be this way even if my son is in a rubix cube competition," Drake wrote.And that\'s when one user decided to hit Drake with this whopper:"ya son prolly plays with ghost writers."A move that caused the Hotline Bling singer to say he would follow the said troll\'s wife on Instagram, which he did because the Champagne Papi does what he wants.Of course, chaos immediately followed, with the commenter\'s partner appearing to get in on the joke via her Instagram stories.She also warned people about the fake accounts that have begun popping up using her name, in case you wanted to remember how weird the internet is. It\'s precisely that weird.Overall, it appears the spat ended on a harmless note, assuming, of course, this person doesn\'t leave her husband for Drake, which would be a very spicy development.', 'content': None, 'pubDate': '2022-05-04 21:08:07', 'image_url': 'https://www.narcity.com/media-library/drake-performing-on-stage.jpg?id=29760895&width=980', 'source_id': 'narcity', 'country': ['canada'], 'category': ['top'], 'language': 'english'}
        """

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

            art = ArticleTile()
            art.title = a['title']
            art.publisher = a['source_id']
            art.cover = cover
            art.date = a['pubDate']
            art.bookmarked = False
            art.link = a['link']
            art.content = content
            grid1.add_widget(art)
    