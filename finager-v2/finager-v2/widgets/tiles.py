from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.properties import ColorProperty, ObjectProperty, BooleanProperty, ListProperty, StringProperty, NumericProperty
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior

Builder.load_string('''
<ListTile>:
    spacing: dp(8)
    size_hint_y: None
    height: dp(48)
    BackBox:
        size_hint_x: None
        width: self.height
        radius: [self.height*.4]
        bcolor: root.icon_color
        padding: dp(8)
        IconButton:
            source: root.icon
    BoxLayout:
        orientation: 'vertical'
        size_hint_x: .7
        Text:
            text: root.title
            font_name: app.fonts.subheading
            font_size: app.fonts.size.h4
            color: app.colors.secondary
            shorten_from: 'center'
        Text:
            text: root.subtitle
            font_name: app.fonts.body
            font_size: app.fonts.size.h6
            color: app.colors.grey_dark
    BoxLayout:
        size_hint_x: .3
        orientation: 'vertical'
        Text:
            id: amount
            font_name: app.fonts.heading
            font_size: app.fonts.size.h5
            color: app.colors.danger if root.expense else app.colors.success
        Text:
            id: extra
            font_name: app.fonts.body
            font_size: app.fonts.size.h6
            color: app.colors.grey_dark
''')
class ListTile(ButtonBehavior, BoxLayout):
    tile_id = StringProperty("")
    icon = StringProperty("")
    title = StringProperty("")
    subtitle = StringProperty("")
    extra = StringProperty("")
    amount = NumericProperty(0.0)
    expense = BooleanProperty(True)
    data = ObjectProperty(allownone=True)
    icon_color = ColorProperty([1,1,1, .2])
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

    def on_amount(self, inst, amount):
        amountx = self.ids.amount
        amountx.text.replace("-", "").replace("+", "")
        if self.expense:
            amountx.text = f"-{round(amount, 2)}"
        else:
            amountx.text = str(amount).strip()

        if amountx.text.startswith("+-"):
            amountx.text = "+"+amount.text[2:]
        if amountx.text.startswith("-+"):
            amountx.text = "-"+amount.text[2:]
    
    def on_expense(self, inst, value):
        amount = self.ids.amount
        amount.text.replace("-", "").replace("+", "")
        if self.expense:
            amount.text = "-"+amount.text
        else:
            amount.text = "+"+amount.text
        
        if amount.text.startswith("+-"):
            amount.text = "+"+amount.text[2:]
        if amount.text.startswith("-+"):
            amount.text = "-"+amount.text[2:]
    
    def on_extra(self, inst, extra):
        self.ids.extra.text = f"${extra}"
