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
        new_value = self.get_valid_input() + value
        self.root.ids.input_number.text = str(new_value)
        self.handle_calculate()


    def handle_calculate(self):
        converted_distance = self.get_valid_input() * MILES_TO_KM
        self.root.ids.output_label.text = str(converted_distance)

    def get_valid_input(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0



DistanceConverterApp().run()
