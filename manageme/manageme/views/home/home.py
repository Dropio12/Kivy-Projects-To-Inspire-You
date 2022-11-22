from datetime import datetime

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict

from kivy.clock import Clock

from widgets.shadow import ShadowBox
from kivy.properties import StringProperty, BooleanProperty, ListProperty, ColorProperty, NumericProperty

Builder.load_file('views/home/home.kv')
class Home(BoxLayout):
    current_time = StringProperty("")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .3)
        Clock.schedule_interval(self.update_time, 1)

    def render(self, _):
        viewed = self.ids.gl_viewed
        progress = self.ids.gl_progress
        viewed.clear_widgets()
        progress.clear_widgets()

        tasks = [
            {"title": "Make landing page", "complete": True}, 
            {"title": "Make presentation", "complete": False}, 
            {"title":"Call Mr.Rendy", "complete": False}, 
            {"title":"Prepare meeting room", "complete": True}, 
            {"title":"Prepare UX project", "complete": False}, 
            {"title": "buy property for event", "complete": True}
        ]

        self.ids.gl_tasks.clear_widgets()
        for t in tasks:
            task = Task()
            task.title = t['title']
            task.complete = t['complete']

            self.ids.gl_tasks.add_widget(task)

        schedules = [
            {
                "title": "Program Class",
                "range": "08:00 - 11:30",
                "desc":  'Add class functions and properties',
                "color": App.get_running_app().colors.success,
            },
            {
                "title": "UI Class",
                "range": "13:00 - 15:30",
                "desc":  'Misc blah blah study app',
                "color": App.get_running_app().colors.success,
            },
            {
                "title": "Weekly Meeting",
                "range": "16:00 - 17:00",
                "desc":  'Status meeting with team',
                "color": App.get_running_app().colors.warning,
            },
            {
                "title": "UX Project Meeting",
                "range": "18:00 - 20:00",
                "desc":  'Discuss project launch',
                "color": App.get_running_app().colors.danger,
            },
        ]

        self.ids.schedules.clear_widgets()
        for s in schedules:
            schedule = Schedule()
            schedule.title = s['title']
            schedule.desc = s['desc']
            schedule.time_range = s['range']
            schedule.color = s['color']

            self.ids.schedules.add_widget(schedule)

        projects = [
            {
                "id": "780990",
                "title": "Resto App",
                "desc": "Some subtitle here",
                "progress": 100,
                "date": "Monday, 23 February 2022",
                "icon": "box",
                "users": [],
                "color": App.get_running_app().colors.success
            },
            {
                "id": "780994",
                "title": "Web Design",
                "desc": "Some subtitle here",
                "progress": 75,
                "date": "Monday, 22 February 2022",
                "icon": "edit-2",
                "users": [],
                "color": App.get_running_app().colors.tertiary
            },
            {
                "id": "474534",
                "title": "Redesign Web",
                "desc": "Some subtitle here",
                "progress": 35,
                "date": "Thursday, 24 February 2022",
                "icon": "globe",
                "users": [],
                "color": App.get_running_app().colors.warning
            },
            {
                "id": "26558",
                "title": "Music App",
                "desc": "Some subtitle here",
                "progress": 50,
                "date": "Friday, 25 February 2022",
                "icon": "headphones",
                "users": [],
                "color": App.get_running_app().colors.danger
            },
        ]

        for i,p in enumerate(projects):
            pb = ProjectBox()
            pb.users = p['users']
            pb.title = p['title']
            pb.subtitle = p['desc']
            pb.icon = p['icon']
            pb.start_date = p['date']
            pb.progress = p['progress']
            pb.icon_color = p['color']
            if i%2 == 0:
                viewed.add_widget(pb)
            else:
                progress.add_widget(pb)

    def update_time(self, _):
        now = datetime.now()

        t = "%s : %s : %s"%(str(now.hour).zfill(2), str(now.minute).zfill(2), str(now.second).zfill(2))
        self.current_time = t

    
class Schedule(BoxLayout):
    title = StringProperty("")
    desc = StringProperty("")
    color = ColorProperty([1,1,1,1])
    time_range = StringProperty("")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        pass
    
class Task(BoxLayout):
    title = StringProperty("")
    complete = BooleanProperty(False)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        pass
    
class ProjectBox(BoxLayout):
    users = ListProperty([])
    title = StringProperty("")
    subtitle = StringProperty("")
    icon = StringProperty("")
    start_date = StringProperty("")
    progress = NumericProperty(0)
    # icon_back_color = ColorProperty([0,0,0,0])
    progress_color = ColorProperty([0,0,0,0])
    icon_color = ColorProperty([0,0,0,0])
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        pass

    def on_progress(self, inst, value):
        if value < 50:
            self.progress_color = App.get_running_app().colors.danger
        elif value >= 50 and value < 100:
            self.progress_color = App.get_running_app().colors.warning
        else:
            self.progress_color = App.get_running_app().colors.success

    def on_icon_color(self, inst, value):
        col = value[:3]
        col.append(.4)

        self.ids.icon_back.bcolor = col
    