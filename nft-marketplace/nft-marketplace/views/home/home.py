
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.clock import Clock
from kivy.properties import StringProperty, ListProperty, ColorProperty, NumericProperty

from widgets.hover import HoverBehavior
from api.hooks import Client

Builder.load_file('views/home/home.kv')
class Home(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.client = Client()
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        nfts = self.client.get_nfts()
        trending = self.client.get_trending()

        # populate nft grid
        nft_grid = self.ids.gl_nfts
        nft_grid.clear_widgets()
        for nft in nfts:
            nc = NFTCard()
            nc.title = nft['title']
            nc.author = nft['author']
            nc.price = nft['price']
            nc.avatar = nft['avatar']
            nc.cover = nft['cover']

            nft_grid.add_widget(nc)
        
        tr_grid = self.ids.gl_trending
        tr_grid.clear_widgets()
        for nft in trending:
            nc = TrendingCard()
            nc.title = nft['title']
            nc.author = nft['author']
            nc.price = nft['price']
            nc.owners = nft['owners']
            nc.volume = nft['volume']
            nc.cover = nft['cover']

            tr_grid.add_widget(nc)

class NFTCard(BoxLayout):
    cover = StringProperty("")
    title = StringProperty("")
    author = StringProperty("")
    avatar = StringProperty("")
    price = StringProperty("0.1ETH")
    price_symbol = StringProperty("assets/icons/ethereum.png")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        pass

class TrendingCard(BoxLayout):
    cover = StringProperty("")
    title = StringProperty("")
    author = StringProperty("")
    owners = StringProperty("")
    volume = StringProperty("")
    price = StringProperty("0.1ETH")
    price_symbol = StringProperty("assets/icons/ethereum.png")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        pass
    