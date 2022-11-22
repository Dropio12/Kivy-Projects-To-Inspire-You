from random import randint, choice

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.clock import Clock, mainthread
from kivy.properties import StringProperty, ListProperty, ColorProperty, NumericProperty
from kivy.core.window import Window

from kivy.garden.iconfonts import icon

from widgets.cards import SharedCard, StorageCard, QuickFileCard, RecentCard, UsageCard
from api import Client

Builder.load_file('views/home/home.kv')
class Home(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)
        self.client = Client()

    def render(self, _):
        shared = self.client.get_shared()
        clouds = self.client.get_storage()
        quick = self.client.get_quick_access()
        recent = self.client.get_recents()
        usage = self.client.get_usage()
        
        self.render_shared(shared)
        self.render_clouds(clouds)
        self.render_quick_access(quick)
        self.render_recent(recent)
        self.render_usage(usage)

    @mainthread
    def render_shared(self, shared):
        self.ids.gl_shared.clear_widgets()
        for s in shared:
            sc = SharedCard()
            sc.file_count = s['total']
            sc.title = s['title']
            sc.users = [x['avatarUrl'] for x in s['users']]
            sc.size_hint_y = None
            sc.height = dp(160)
            sc.bcolor = App.get_running_app().colors.primary
            sc.radius = [dp(18)]

            self.ids.gl_shared.add_widget(sc)
        
    @mainthread
    def render_clouds(self, clouds):
        self.ids.gl_clouds.clear_widgets()
        for c in clouds:
            sc = StorageCard()
            sc.icon = icon("icon-more-vertical")
            sc.bcolor = App.get_running_app().colors.white
            sc.title = c['title']
            sc.cover = c['iconUrl']
            sc.radius = [dp(12)]
            sc.total = c['total']
            sc.used = c['used']
            sc.width = dp(180)
            sc.height = dp(132)
            sc.size_hint = [None, None]

            self.ids.gl_clouds.add_widget(sc)
    
    @mainthread
    def render_usage(self, usage):
        colors = [rgba("#EA384D"),rgba("#F9D423"),rgba("#5172E5"),rgba("#E65C00"),rgba("#45F08C"),]
        totals = [float(x['used'].replace("GB", "")) for x in usage]

        self.ids.arc.arc_max = sum(totals)
        self.ids.arc.items = totals

        self.ids.gl_used.clear_widgets()
        chosen = []
        for u in usage:
            uc = UsageCard()
            uc.icon = icon("icon-%s"%u['iconName'])
            uc.title = u['title'].title()
            uc.total = int(u['totalFiles'])
            uc.used = u['used']

            ch = choice(colors)
            chosen.append(ch)
            uc.bcolor = ch

            self.ids.gl_used.add_widget(uc)
        
        self.ids.arc.colors = chosen

    @mainthread
    def render_recent(self, recent):
        colors = [rgba("#EA384D"),rgba("#F9D423"),rgba("#5172E5"),rgba("#E65C00"),rgba("#45F08C"),]
        self.ids.gl_recent.clear_widgets()

        for r in recent:
            rc = RecentCard()
            rc.bcolor = App.get_running_app().colors.white
            rc.icon_color = choice(colors)
            rc.ext = r['title'].rsplit(".", 1)[1].upper()
            rc.title = r['title']
            rc.modified = r['modified']

            self.ids.gl_recent.add_widget(rc)
    
    @mainthread
    def render_quick_access(self, quick):
        colors = [rgba("#EA384D"),rgba("#F9D423"),rgba("#5172E5"),rgba("#E65C00"),rgba("#45F08C"),]

        self.ids.gl_quick.clear_widgets()
        for q in quick:
            qa = QuickFileCard()
            qa.title = q['name']
            qa.bcolor = App.get_running_app().colors.white
            qa.radius = [dp(12)]
            qa.ext = q['fileType'].upper()
            qa.file_size = q['size']
            qa.file_color = choice(colors)
            qa.size_hint = [None, None]
            qa.size = [Window.width*.12, Window.height*.25]
    
            self.ids.gl_quick.add_widget(qa)