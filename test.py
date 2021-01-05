from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from KivyCalendar import CalendarWidget
from kivy.lang import Builder

kv = Builder.load_file("scroll.kv")



class SetIndex(BoxLayout):
    def setDate(self, *args):
        popup = Popup(title='Insert Old Date', content=CalendarWidget(), size_hint=(.9, .5)).open()


class Demo(App):
    def bulid(self):
        return SetIndex()


if __name__ == '__main__':
    Demo().run()