from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.properties import ColorProperty, ObjectProperty, BooleanProperty, ListProperty, StringProperty, NumericProperty
Builder.load_string("""
#: import Window kivy.core.window.Window

#region
<ArticleCard>:
    orientation: 'vertical'
    spacing: dp(4)
    size_hint: [None, None]
    height: dp(180) + title.height
    width: Window.width*.9
    BackBox:
        size_hint_y: .7
        RelativeLayout:
            AsyncImage:
                id: cover
                source: root.cover
                opacity: 0
            Widget:
                canvas.before:
                    Color:
                        rgba: app.colors.white
                    RoundedRectangle:
                        size: self.size[0], self.size[1]
                        pos: self.pos
                        radius: [self.height*.1]
                        texture: cover.texture
            AnchorLayout:
                anchor_y: 'top'
                anchor_x: "right"
                BackBox:
                    size_hint: [None, None]
                    size: [dp(32), dp(32)]
                    radius: [dp(8)]
                    bcolor: [1,1,1, .4]
                    Text:
                        text: icon("icon-bookmark")
                        color: app.colors.primary
                        font_size: app.fonts.size.h1
    BoxLayout:
        size_hint_y: None
        height: dp(28) + title.height
        orientation: 'vertical'
        spacing: dp(4)
        Label:
            id: title
            text: root.title
            font_size: app.fonts.size.h5
            font_name: app.fonts.heading
            size_hint_y: None
            text_size: (Window.width*.9, None)
            size: self.texture_size
            color: app.colors.white
        BoxLayout:
            size_hint_y: None
            height: dp(16)
            spacing: dp(8)
            Text:
                text: root.publisher
                font_name: app.fonts.body
                font_size: app.fonts.size.h6
                color: app.colors.white
            Text:
                text: root.date
                font_name: app.fonts.body
                font_size: app.fonts.size.h6
                color: app.colors.white
                halign: 'right'
#endregion
<ArticleTile>:
    size_hint_y: None
    height: dp(42) + title.height
    padding: dp(4)
    spacing: dp(8)
    AnchorLayout:
        size_hint_x: None
        width: dp(42)
        BoxLayout:
            size_hint: [None, None]
            size: [dp(42), dp(42)]
            # size_hint: [None, None]
            # size: [dp(72), dp(72)]
            RelativeLayout:
                AsyncImage:
                    id: cover
                    source: root.cover
                    opacity: 0
                Widget:
                    canvas.before:
                        Color:
                            rgba: app.colors.white
                        RoundedRectangle:
                            size: self.size[0], self.size[1]
                            pos: self.pos
                            radius: [self.height*.1]
                            texture: cover.texture
    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: dp(18) + title.height
        BoxLayout:
            Label:
                id: title
                text: root.title
                font_size: app.fonts.size.h6
                font_name: app.fonts.heading
                size_hint_y: None
                text_size: (Window.width*.6, None)
                size: self.texture_size
                color: app.colors.white
            AnchorLayout:
                anchor_y: "top"
                anchor_x: 'right'
                size_hint_x: None
                width: dp(24)
                ToggleButton:
                    id: bookmark
                    text: icon("icon-bookmark")
                    color: app.colors.primary if self.state == "normal" else app.colors.warning
                    size_hint: [None, None]
                    size: [dp(24), dp(24)]
                    background_normal: ""
                    background_down: ""
                    background_color: [0,0,0,0]
                    markup: True
        BoxLayout:
            size_hint_y: None
            height: dp(16)
            Text:
                text: root.publisher
                font_size: app.fonts.size.h6
                font_name: app.fonts.body
                color: app.colors.white
            Text:
                text: root.date
                font_size: app.fonts.size.h6
                font_name: app.fonts.body
                color: app.colors.white
                halign: 'right'
                size_hint_x: .4
<ArticleView>:
    background_color: app.colors.secondary
    background: ""
    BoxLayout:
        orientation: 'vertical'
        AnchorLayout:
            size_hint_y: None
            height: dp(54)
            padding: dp(12)
            anchor_x: 'left'
            BoxLayout:
                size_hint_x: None
                width: self.height
                canvas.before:
                    Color:
                        rgba: app.colors.primary
                    RoundedRectangle:
                        size: self.size[0], self.size[1]
                        pos: self.pos
                        radius: [self.height*.15]
                FlatButton:
                    text: icon("icon-chevron-left")
                    color: app.colors.white
                    font_size: app.fonts.size.h1
                    on_release: root.dismiss()
        BoxLayout:
            ScrollView:
                do_scroll: [False, True]
                size_hint_y: None
                height: self.parent.height
                GridLayout:
                    cols: 1
                    size_hint_y: None
                    height: self.minimum_height
                    spacing: dp(8)
                    padding: dp(8)
                    ArticleCard:
                        id: art
                        clickable: False
                    Label:
                        id: content
                        text: root.content
                        font_size: app.fonts.size.h6
                        font_name: app.fonts.body
                        size_hint_y: None
                        text_size: (Window.width*.9, None)
                        size: self.texture_size
                        color: app.colors.white
                    FlatButton:
                        text: "[u]Continue reading...[/u]"
                        color: app.colors.primary
                        size_hint_y: None
                        height: dp(42)
""")

class Article(ButtonBehavior, BoxLayout):
    title = StringProperty("")
    cover = StringProperty("")
    link = StringProperty("")
    author = StringProperty("")
    publisher = StringProperty("")
    content = StringProperty("")
    date = StringProperty("")
    bookmarked = BooleanProperty(False)
    clickable = BooleanProperty(True)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.bind(on_release=self.view_article)

    def view_article(self, *args):
        if self.clickable:
            av = ArticleView()
            av.content = self.content
            
            art = av.ids.art
            art.title = self.title
            art.publisher = self.publisher
            art.cover = self.cover
            art.date = self.date
            art.bookmarked = False
            art.link = self.link

            av.open()

class ArticleCard(Article):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

class ArticleTile(Article):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

class ArticleView(ModalView):
    title = StringProperty("")
    cover = StringProperty("")
    link = StringProperty("")
    author = StringProperty("")
    publisher = StringProperty("")
    content = StringProperty("")
    date = StringProperty("")
    bookmarked = BooleanProperty(False)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
