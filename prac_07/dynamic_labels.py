from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels App"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.names = ["Clark", "Veronica", "Noah", "Patty", "Dave"]
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.placeholder.add_widget(temp_label)
        return self.root


DynamicLabelsApp().run()
