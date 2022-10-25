from kivy.app import App
from kivy.uix.button import Button
import plyer

class techsnap(App):
    def build(self):
        return Button(text='press to explore techsnap', on_press=self.notify)

    def notify(self, obj):
        plyer.notification.notify(title="techsnap", messsage="welcome To techsnap")

techsnap().run()
