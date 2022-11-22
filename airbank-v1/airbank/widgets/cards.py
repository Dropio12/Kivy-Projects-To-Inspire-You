from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.properties import ColorProperty, ObjectProperty, BooleanProperty, ListProperty, StringProperty, NumericProperty

from widgets.images import CircleAvatar

Builder.load_string('''
#: import SProgressBar widgets.progress.SProgressBar

<SharedCard>:
    padding: dp(12)
    spacing: dp(10)
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: self.bcolor
        RoundedRectangle:
            size: self.size[0], self.size[1]
            pos: self.pos
            radius: root.radius
    BoxLayout:
        spacing: dp(10)
        Widget:
            size_hint_x: None
            width: self.height
            canvas.before:
                Color:
                    rgba: [1,1,1,1]
                Rectangle:
                    size: self.size[0], self.size[1]
                    pos: self.pos
                    source: "assets/imgs/ic_folder.png"
            
        BoxLayout:
            padding: [0, dp(8)]
            AvatarStack:
                id: stack
                sources: root.users
    Label:
        text: root.title
        color: [1,1,1,1]
        bold: True
        font_size: sp(18)
        text_size: self.size
        valign: "middle"
    Label:
        text: "%s Files"%root.file_count
        color: [1,1,1, .3]
        font_size: sp(14)
        text_size: self.size
        valign: "bottom"

<StorageCard>:
    padding: dp(12)
    spacing: dp(10)
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: self.bcolor
        RoundedRectangle:
            size: self.size[0], self.size[1]
            pos: self.pos
            radius: root.radius
    BoxLayout:
        spacing: dp(10)
        size_hint_y: .3
        Widget:
            size_hint_x: None
            width: self.height
            canvas.before:
                Color:
                    rgba: [1,1,1,1]
                Rectangle:
                    size: self.size[0], self.size[1]
                    pos: self.pos
                    source: root.cover
            
        AnchorLayout:
            padding: [0, dp(8)]
            anchor_x: "right"
            anchor_y: "top"
            Button:
                text: root.icon
                color: rgba("#c4c4c4")
                background_normal: ""
                background_down: ""
                background_color: [0,0,0,0]
                size_hint: None, None
                size: [dp(32), dp(32)]
                markup: True
    BoxLayout:
        size_hint_y: .2
        Label:
            text: root.title
            color: [0,0,0, 1]
            bold: True
            font_size: sp(18)
            text_size: self.size
            valign: "top"
    BoxLayout:
        id: storage_progress
        size_hint_y: None
        height: dp(42)
        orientation: "vertical"
        Label:
            id: storage_indicator
            text: ""
            color: rgba("#e2e2e2")
            bold: True
            font_size: sp(12)
            text_size: self.size
            valign: "bottom"
            halign: "right"
        SProgressBar:
            id: pb
            value: int(root.used.strip("gb"))
            pmax: int(root.total.strip("gb"))
            bg_color: rgba("#e2e2e2")
            fg_color: rgba("#5172E5")

<QuickFileCard>:
    orientation: "vertical"
    spacing: dp(10)
    padding: dp(12)
    canvas.before:
        Color:
            rgba: self.bcolor
        RoundedRectangle:
            size: self.size[0], self.size[1]
            pos: self.pos
            radius: root.radius
    BoxLayout:
        size_hint_y: .9
        RelativeLayout:
            AnchorLayout:
                Image:
                    color: root.file_color
                    source: "assets/imgs/bg_file.png"  
            Label:
                text: root.ext
                color: rgba("#ffffff")
                font_size: sp(18)
                bold: True
                text_size: self.size
                halign: "center"
                valign: 'bottom'
    Widget:
        size_hint_y: .1
    BoxLayout:
        size_hint_y: None
        height: dp(42)
        orientation: 'vertical'
        spacing: dp(8)
        Label:
            text: root.title
            color: [0,0,0, 1]
            font_size: app.fonts.size.h5
            bold: True
            text_size: self.size
            halign: "center"
            valign: 'bottom'
        Label:
            text: root.file_size
            color: rgba("#909090")
            font_size: app.fonts.size.h6
            font_name: app.fonts.body
            text_size: self.size
            halign: 'center'
            size_hint_y: None
            height: dp(16)

<PremiumCard>:
    orientation: "vertical"
    padding: dp(12)
    canvas.before:
        Color:
            rgba: self.bcolor
        RoundedRectangle:
            size: self.size[0], self.size[1]
            pos: self.pos
            radius: root.radius
    AnchorLayout:
        size_hint_y: .45
        Image:
            source: "assets/icons/ic_cloud.png"
    BoxLayout:
        size_hint_y: .4
        orientation: "vertical"
        spacing: dp(10)
        Label:
            text: root.title
            font_size: sp(18)
            bold: True
            text_size: self.size
            size_hint_y: None
            height: dp(22)
            halign: "center"
            valign: 'top'
            color: rgba("#5172E5")
        Label:
            text: root.desc
            font_size: sp(12)
            text_size: self.parent.width, None
            size: self.texture_size
            halign: "center"
            color: rgba("#000000")
    AnchorLayout:
        size_hint_y: .15
        Button:
            text: "Show Me"
            bold: True
            color: [1,1,1,1]
            background_down: ""
            background_normal: ""
            background_color: [0,0,0,0]
            canvas.before:
                Color:
                    rgba: root.cta_color
                RoundedRectangle:
                    size: self.size[0], self.size[1]
                    pos: self.pos
                    radius: [self.height*.25]

<RecentCard>:
    size_hint_y: None
    height: dp(42)
    padding: dp(4)
    spacing: dp(8)
    canvas:
        Color:
            rgba: self.bcolor
        RoundedRectangle:
            size: self.size[0], self.size[1]
            pos: self.pos
            radius: [self.height*.1]
    BoxLayout:
        spacing: dp(10)
        size_hint_x: .4
        AnchorLayout:
            size_hint_x: None
            width: self.height
            canvas.before:
                Color:
                    rgba: root.icon_color
                RoundedRectangle:
                    size: self.size[0], self.size[1]
                    pos: self.pos
                    radius: [self.height*.2]
            Text:
                text: root.ext
                color: app.colors.white
                halign: "center"
                font_size: app.fonts.size.h6
        Text:
            text: root.title
            color: [0,0,0,1]
            font_size: app.fonts.size.h5
    Text:
        size_hint_x: .3
        text: root.ext
        color: [0,0,0,1]
        font_name: app.fonts.body
        font_size: app.fonts.size.h5
    Text:
        size_hint_x: .3
        text: root.modified
        color: [0,0,0,1]
        font_name: app.fonts.body
        font_size: app.fonts.size.h5

<UsageCard>:
    size_hint_y: None
    height: dp(42)
    spacing: dp(10)
    AnchorLayout:
        size_hint_x: None
        width: self.height
        canvas.before:
            Color:
                rgba: root._bcolor
            RoundedRectangle:
                size: self.size[0], self.size[1]
                pos: self.pos
                radius: [self.height*.2]
        Text:
            id: icon
            text: root.icon
            color: root.bcolor
            halign: "center"
            font_size: app.fonts.size.h1
    BoxLayout:
        orientation: 'vertical'
        Text:
            text: root.title
            color: [0,0,0,1]
            font_name: app.fonts.subheading
            font_size: app.fonts.size.h5
        Text:
            text: "%s files"%root.total
            color: app.colors.black
            font_name: app.fonts.body
            font_size: app.fonts.size.h5
    Text:
        text: root.used
        color: app.colors.primary
        font_name: app.fonts.body
        font_size: app.fonts.size.h6
        halign: 'center'
        valign: 'middle'
        size_hint_x: None
        width: self.height
''')

class RecentCard(BoxLayout):
    bcolor = ColorProperty(rgba("#ffffff"))
    icon_color = ColorProperty(rgba("#ffffff"))
    title = StringProperty("")
    ext = StringProperty("")
    modified = StringProperty("")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

class UsageCard(BoxLayout):
    bcolor = ColorProperty(rgba("#ffffff"))
    _bcolor = ColorProperty(rgba("#ffffff"))
    icon_color = ColorProperty(rgba("#ffffff"))
    title = StringProperty("")
    icon = StringProperty("")
    total = NumericProperty(0)
    used = StringProperty("")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

    def on_bcolor(self, _, color):
        col = color[:3]
        col.append(.2)

        self._bcolor = col

class SharedCard(BoxLayout):
    bcolor = ColorProperty(rgba("#ffffff"))
    radius = ListProperty([dp(4)])
    title = StringProperty("")
    users = ListProperty([])
    file_count = NumericProperty(0)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

class StorageCard(BoxLayout):
    bcolor = ColorProperty(rgba("#ffffff"))
    radius = ListProperty([dp(4)])
    title = StringProperty("")
    cover = StringProperty("")
    icon = StringProperty(":")
    total = StringProperty("10gb")
    used = StringProperty("5gb")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

    def on_used(self, _, val):
        self.ids.storage_indicator.text = "%s/%s"%(val, self.total)
        self.ids.pb.value = int(val.strip("GB"))

    def on_total(self, _, val):
        self.ids.storage_indicator.text = "%s/%s"%(self.used, val)
        self.ids.pb.pmax = int(val.strip("GB"))

class QuickFileCard(BoxLayout):
    title = StringProperty("")
    ext = StringProperty("")
    file_color = ColorProperty([1,1,1,1])
    bcolor = ColorProperty([1,1,1,1])
    radius = ListProperty([1])
    file_size = StringProperty("0Kb")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

class PremiumCard(BoxLayout):
    title = StringProperty("")
    desc = StringProperty("")
    bcolor = ColorProperty([1,1,1,1])
    cta_color = ColorProperty([1,1,1,1])
    radius = ListProperty([1])
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
