from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        print("Building the app...")
        self.icon = "calc.png"
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(background_color="black", foreground_color="white",
                                  multiline=False, halign="right", font_size=55, readonly=True)
        main_layout.add_widget(self.solution)
        buttons = [
            ["9", "8", "7", "/"],
            ["6", "5", "4", "*"],
            ["3", "2", "1", "+"],
            [".", "0", "C", "-"]
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label, font_size=30, background_color="grey",
                    pos_hint={"center_x": 0.5, "center_y": 0.5}
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        equal_button = Button(
            text="=", font_size=30, background_color="grey",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equal_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_button)

        print("Returning main layout...")
        return main_layout

    def on_button_press(self, instance):
        print("Button pressed:", instance.text)
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            print("Clearing solution...")
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                print("Ignoring operator...")
                return
            elif current == "" and button_text in self.operators:
                print("Ignoring operator...")
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        print("Solving...")
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution

if __name__ == "__main__":
    app = MainApp()
    app.run()
