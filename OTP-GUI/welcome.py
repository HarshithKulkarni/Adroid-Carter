import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.config import Config

kivy.require("1.10.1")

Config.set('graphics', 'width', '720')
Config.set('graphics', 'height', '340')

class Welcome:
	def ret_img(self):
		return Image(source='bot.jpeg')

	def ret_text(self):
		return Label(text='Adroid-Carter')
# class OTP_Accept(GridLayout):
# 	def __init__(self,**kwargs):
# 		super().__init__(**kwargs)

# 		self.cols = 2

# 		self.add_widget(Label(text='OTP:'))
# 		self.otp = TextInput(multiline=False)
# 		self.add_widget(self.otp)

class OTPApp(App):
    def build(self):
        return Welcome().ret_img()

if __name__ == "__main__":
    OTPApp().run()