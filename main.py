from kivy.lang import Builder
from kivy.app import App
from kivy.config import Config

# Define resolução "de celular"
Config.set('graphics', 'width', '360')   # largura
Config.set('graphics', 'height', '640')  # altura
Config.set('graphics', 'resizable', '0')  # evita redimensionamento (opcional)


class MyApp(App):
    first_number = 0.0
    next: bool = False
    operator: str = ''


    def build(self):
        return Builder.load_file("calculator.kv")
    

    def bt_number_click(self, number):
        if self.next:
            self.root.ids.workspace.text = number
            self.next = False
        else:
            self.root.ids.workspace.text += number

    
    def bt_action_click(self, number, operator):
        try:
            match operator:
                case "+" | "-" | "*" | "/":
                    self.first_number = float(number) if self.first_number == 0.0 else (f"{self.first_number} {operator} {float(number)}")
                    self.next = True
                case "=":
                    self.first_number = float(number) if self.first_number == 0.0 else (eval(f"{self.first_number} {self.operator} {float(number)}"))
                    self.root.ids.workspace.text = str(self.first_number)
                    self.first_number = 0.0
                    self.next = True
                    return
                case _:
                    raise Exception("Operação invalida.")
            self.operator = operator if operator != "=" else operator
            self.root.ids.workspace.text = str(self.first_number)
        except Exception as e:
            print(e)


    def bt_clear_click(self):
        self.root.ids.workspace.text = ''
        self.first_number = 0.0
        self.next = False
        self.operator = ''
    

if __name__ == '__main__':
    MyApp().run()
    