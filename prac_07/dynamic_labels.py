from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels App"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def create_labels(self):
        self.names = ["Clark", "Veronica", "Noah", "Patty"]
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.placeholder.add_widget(temp_label)

DynamicLabelsApp().run()