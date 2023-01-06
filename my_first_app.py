from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childApp(GridLayout):
    def __init__(self, **kwargs):
        super(childApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text = 'Student Name'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text = 'Student Marks'))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text = 'Student Gender'))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.press = Button(text = 'click')
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)
    
    def click_me(self, instance):
        print('name of student: '+self.s_name.text)
        print('marks of student: '+self.s_marks.text)
        print('gender of student: '+self.s_gender.text)

class parentApp(App):
    def build(self):
        return childApp()

if __name__ == "__main__":
    parentApp().run()