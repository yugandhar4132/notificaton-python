from kivy.app import App
from kivy.uix.button import Button
import plyer

class Myapp(App):
    def build(self):
        return Button(text='press to explore my app', on_press=self.notify)

    def notify(self, obj):
        plyer.notification.notify(title="application", messsage="welcome To My app")

Myapp().run()
