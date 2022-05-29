import kivy

kivy.require('2.1.0')  # replace with your current kivy version !

from kivy.app import App
# from kivy.uix.label import Label
from kivy.uix.widget import Widget


class PongGame(Widget):
    pass


class PongApp(App):

    def build(self):
        return PongGame()


if __name__ == '__main__':
    PongApp().run()
