
from kivy.app import App
from kivy.utils import QueryDict, rgba
from kivy.metrics import dp, sp

from .view import MainWindow

class MainApp(App):
    colors = QueryDict()
    colors.primary = rgba("#5172E5")
    colors.secondary = rgba("#F0F3FF")
    colors.success = rgba("#1FC98E")
    colors.warning = rgba("#F2C94C")
    colors.danger = rgba("#EB5757")
    colors.tertiary = rgba("#E65C00")
    colors.tertiary_light = rgba("#F3F7FF")
    colors.grey_dark = rgba("#D9D9D9")
    colors.grey_light = rgba("#f2f2f2")
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

    fonts.heading = 'assets/fonts/Inter/Inter-Bold.otf'
    fonts.subheading = 'assets/fonts/Inter/Inter-Regular.otf'
    fonts.body = 'assets/fonts/Inter/Inter-Thin.otf'

    def build(self):
        return MainWindow()
