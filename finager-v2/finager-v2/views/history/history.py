from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict, get_random_color
from kivy.clock import Clock

from widgets.tiles import ListTile

Builder.load_file('views/history/history.kv')
class History(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        trans = [
            {
                'id': '324f',
                'title': 'Freelance - Organik',
                'date': 'Today',
                'amount': '720.00',
                'initial-amount': '12,103',
                'icon': 'assets/icons/watch.png',
                'expense': False,
            },
            {
                'id': '345fj',
                'title': 'Spotify AB',
                'date': 'Today',
                'amount': '8.99',
                'initial-amount': '13,757',
                'icon': 'assets/icons/spotify-32 1.png',
                'expense': True,
            },
            {
                'id': '32rdwea',
                'title': 'Work Salary',
                'date': 'Yesterday',
                'amount': '540.00',
                'initial-amount': '12,472',
                'icon': 'assets/icons/monitor-outline.png',
                'expense': False,
            },
        ]

        self.refresh_transactions(trans)

    def refresh_transactions(self, data):
        grid = self.ids.gl_history
        grid.clear_widgets()

        for t in reversed(data):
            ic = get_random_color()[:3]
            ic.append(.3)

            tile = ListTile()
            tile.tile_id = t['id']
            tile.title = t['title']
            tile.subtitle = t['date']
            tile.amount = t['amount']
            tile.extra = t['initial-amount']
            tile.expense = t['expense']
            tile.icon = t['icon']
            tile.icon_color = ic

            grid.add_widget(tile)
