import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.config import Config
from kivy.uix.button import Button
from random import randint

#OTP Generation
gen_OTP = randint(1000,9999)

# SMS class
#class sendSMS:


# UI Code
kivy.require("1.10.1")
Config.set('graphics', 'width', '720')
Config.set('graphics', 'height', '340')

typed_OTP = []

class OTP_Accept(GridLayout):
	def __init__(self,**kwargs):
		super(OTP_Accept,self).__init__(**kwargs)

		
		self.cols = 3

		self.one = Button(text="1")
		self.one.bind(on_press=self.one_pressed)
		self.add_widget(self.one)

		self.two = Button(text="2")
		self.two.bind(on_press=self.two_pressed)
		self.add_widget(self.two)

		self.three = Button(text="3")
		self.three.bind(on_press=self.three_pressed)
		self.add_widget(self.three)

		self.four = Button(text="4")
		self.four.bind(on_press=self.four_pressed)
		self.add_widget(self.four)
		
		self.five = Button(text="5")
		self.five.bind(on_press=self.five_pressed)
		self.add_widget(self.five)
		
		self.six = Button(text="6")
		self.six.bind(on_press=self.six_pressed)
		self.add_widget(self.six)
		
		self.seven = Button(text="7")
		self.seven.bind(on_press=self.seven_pressed)
		self.add_widget(self.seven)
		
		self.eight = Button(text="8")
		self.eight.bind(on_press=self.eight_pressed)
		self.add_widget(self.eight)
		
		self.nine = Button(text="9")
		self.nine.bind(on_press=self.nine_pressed)
		self.add_widget(self.nine)
	
		self.zero = Button(text="0")
		self.zero.bind(on_press=self.zero_pressed)
		self.add_widget(Label())
		self.add_widget(self.zero)
		self.add_widget(Label())

		self.submit = Button(text="Submit",font_size=20)
		self.submit.bind(on_press=self.submit_pressed)
		self.add_widget(Label())
		self.add_widget(self.submit)
	
	def one_pressed(self,instance):
		one_button_val = '1'
		typed_OTP.append(one_button_val)
	
	def two_pressed(self,instance):
		two_button_val = '2'
		typed_OTP.append(two_button_val)

	def three_pressed(self,instance):
		three_button_val = '3'
		typed_OTP.append(three_button_val)

	def four_pressed(self,instance):
		four_button_val = '4'
		typed_OTP.append(four_button_val)
		
	def five_pressed(self,instance):
		five_button_val = '5'
		typed_OTP.append(five_button_val)

	def six_pressed(self,instance):
		six_button_val = '6'
		typed_OTP.append(six_button_val)

	
	def seven_pressed(self,instance):
		seven_button_val = '7'
		typed_OTP.append(seven_button_val)

	def eight_pressed(self,instance):
		eight_button_val = '8'
		typed_OTP.append(eight_button_val)

	def nine_pressed(self,instance):
		nine_button_val = '9'
		typed_OTP.append(nine_button_val)

	def zero_pressed(self,instance):
		zero_button_val = '0'
		typed_OTP.append(zero_button_val)

	def submit_pressed(self,instance):
		tmp = [''.join(typed_OTP[0:4])]
		l = ""
		for ele in tmp:
			l += ele 
		print(l)
		typed_OTP.clear()

class OTPApp(App):
    def build(self):
        return OTP_Accept()


if __name__ == "__main__":
	
	OTPApp().run()