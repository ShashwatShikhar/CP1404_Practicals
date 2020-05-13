from kivy.app import App
from kivy.lang import Builder


class DynamicLabels(App):
    def build(self):
        self.title = "Names List"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root
DynamicLabels().run()