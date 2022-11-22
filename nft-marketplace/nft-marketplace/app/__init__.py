
from kivy.app import App
from kivy.utils import QueryDict, rgba
from kivy.metrics import dp, sp
from kivy.properties import ColorProperty

from .view import MainWindow

class MainApp(App):
    colors = QueryDict()
    color_primary = ColorProperty(rgba("#18A0FB"))
    color_secondary = ColorProperty(rgba("#9AD5E7"))
    color_success = ColorProperty(rgba("#1FC98E"))
    color_success_light = ColorProperty(rgba("#1FC98E20"))
    color_warning = ColorProperty(rgba("#F2C94C"))
    color_danger = ColorProperty(rgba("#D45B71"))
    color_tertiary = ColorProperty(rgba("#E8F0FF"))
    color_tertiary_light = ColorProperty(rgba("#F3F7FF"))
    color_grey_dark = ColorProperty(rgba("#c4c4c4"))
    color_grey_light = ColorProperty(rgba("#f5f5f5"))
    color_black = ColorProperty(rgba("#000000"))
    color_white = ColorProperty(rgba("#ffffff"))

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
    fonts.body = 'assets/fonts/Inter/Inter-ExtraLight.otf'

    def build(self):
        return MainWindow()
