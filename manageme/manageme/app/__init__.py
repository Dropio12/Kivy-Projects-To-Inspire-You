
from kivy.app import App
from kivy.utils import QueryDict, rgba
from kivy.metrics import dp, sp

from .view import MainWindow

class MainApp(App):
    colors = QueryDict()
    colors.primary = rgba("#073B4C")
    colors.secondary = rgba("#118AB2")
    colors.success = rgba("#06D6A0")
    colors.warning = rgba("#FFD166")
    colors.danger = rgba("#EF476F")
    colors.tertiary = rgba("#118AB2")
    colors.grey_dark = rgba("#c4c4c4")
    colors.grey_light = rgba("#f5f5f5")
    colors.black = rgba("#010101")
    colors.white = rgba("#ffffff")

    fonts = QueryDict()
    fonts.size = QueryDict()
    fonts.size.h1 = dp(24)
    fonts.size.h2 = dp(22)
    fonts.size.h3 = dp(18)
    fonts.size.h4 = dp(16)
    fonts.size.h5 = dp(14)
    fonts.size.h6 = dp(12)

    fonts.heading = 'assets/fonts/Inter/Inter-Bold.otf'
    fonts.subheading = 'assets/fonts/Inter/Inter-Regular.otf'
    fonts.body = 'assets/fonts/Inter/Inter-ExtraLight.otf'

    def build(self):
        return MainWindow()
