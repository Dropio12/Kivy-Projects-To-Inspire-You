
from kivy.app import App
from kivy.utils import QueryDict, rgba
from kivy.metrics import dp, sp

from .view import MainWindow

class MainApp(App):
    colors = QueryDict()
    colors.bg = rgba("#0E1618")
    colors.primary = rgba("#000000")
    colors.secondary = rgba("#122124")
    colors.success = rgba("#3176FB")
    colors.warning = rgba("#F2C94C")
    colors.danger = rgba("#FD1E53")
    colors.tertiary = rgba("#152331")
    colors.tertiary_light = rgba("#465C62")
    colors.grey_dark = rgba("#c4c4c4")
    colors.grey_light = rgba("#262626")
    colors.black = rgba("#a1a1a1")
    colors.white = rgba("#ffffff")

    fonts = QueryDict()
    fonts.size = QueryDict()
    fonts.size.extra = dp(54)
    fonts.size.h1 = dp(24)
    fonts.size.h2 = dp(22)
    fonts.size.h3 = dp(18)
    fonts.size.h4 = dp(16)
    fonts.size.h5 = dp(14)
    fonts.size.h6 = dp(12)

    fonts.heading = 'assets/fonts/Barlow/BarlowCondensed-Regular.ttf'
    fonts.subheading = 'assets/fonts/Barlow/BarlowCondensed-Light.ttf'
    fonts.body = 'assets/fonts/Barlow/BarlowCondensed-Thin.ttf'

    def build(self):
        return MainWindow()
