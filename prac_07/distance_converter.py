from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934

class DistanceConverterApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (800, 400)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('distance_converter.kv')
        return self.root

    def handle_increment(self, value):
        new_value = int(self.root.ids.input_number.text) + value
        self.root.ids.input_number.text = str(new_value)
        self.handle_calculate(int(new_value))


    def handle_calculate(self, value):
        converted_distance = value * MILES_TO_KM
        self.root.ids.output_label.text = str(converted_distance)


DistanceConverterApp().run()
