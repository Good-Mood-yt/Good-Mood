from tkinter import *
import tkinter.font as tkFont
root = Tk()
root.title("Prime or composite")
root.geometry('1280x720')
root["bg"] = "#6c5b7b"
fontStyle = tkFont.Font(family="Lucida Grande", size=50)
enter = Label(text = "Enter a number ", font = fontStyle,bg = "#6c5b7b").pack()
num = Entry(root , font = fontStyle)
num.pack()
ans = Label(root, font = fontStyle,bg = "#6c5b7b")
def check():
	try:
		is_prime = True
		number = int(num.get())
		if number == 0 or 1:		
			ans['text'] = f" {number} is not prime neither composite"
		if number > 1:
			for x in range(2,number):
				if(number % x) == 0:
					is_prime = False
					break
			if is_prime:
				ans['text'] =f"{number} is a prime number"
			else:
				ans['text'] = f"{number} is a composite number "
	except ValueError:
		ans['text'] = "Please Enter a number " 
empty = Label(bg =  "#6c5b7b").pack()
check = Button(text = "Check", command = check ,font = fontStyle, border = 0, bg = "#87ceeb").pack()
ans.pack()
root.mainloop()
