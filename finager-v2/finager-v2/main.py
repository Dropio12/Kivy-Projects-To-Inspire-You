
from os.path import dirname, join

from kivy.garden.iconfonts import register

from app import MainApp

register(
    "MatIcons",
    join(dirname(__file__), "assets/fonts/zmdi/Material-Design-Iconic-Font.ttf"),
    join(dirname(__file__), "assets/fonts/zmdi/zmd.fontd")
)
MainApp().run()
