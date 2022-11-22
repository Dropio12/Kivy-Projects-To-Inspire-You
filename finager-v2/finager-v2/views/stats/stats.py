from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict, get_random_color
from kivy.clock import Clock

from widgets.tiles import ListTile

Builder.load_file('views/stats/stats.kv')
class Stats(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        # Plot Chart points
        points = [(100, 60), (300, 110), (320, 40), (150, 170), (300, 150), (300, 170), (250, 120), (200, 80), (320, 180), (290, 100), (320, 90), (300, 340)]
        colors = App.get_running_app().colors

        chart = self.ids.chart
        chart.point_colors = (colors.primary, colors.tertiary)
        chart.points = points
        chart.xlabels = ['Jan', 'Feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

        trans = [
            {
                'id': '6we',
                'title': 'Digitalocean Droplet',
                'date': 'Today',
                'amount': '22.00',
                'initial-amount': '12,472',
                'icon': 'assets/icons/cloud-drizzle.png',
                'expense': True,
            },
            {
                'id': '630e',
                'title': 'PicknPay Hyper Spring Groceries',
                'date': 'Today',
                'amount': '54.50',
                'initial-amount': '12,869',
                'icon': 'assets/icons/shopping-bag-outline.png',
                'expense': True,
            },
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
        grid = self.ids.gl_month_spend
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
            tile.icon = t['icon']
            tile.icon_color = ic
            tile.expense = t['expense']

            grid.add_widget(tile)
