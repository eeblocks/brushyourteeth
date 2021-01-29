from tkinter import *
from tkinter.font import Font
import time

window = Tk()

font = Font(family='Helvetica')

window.title("Brush Your Teeth")
window.iconbitmap('tooth.ico')
window.configure(width=600, height=500)
window.geometry('600x500')
window.resizable(False, False)
window.configure(bg='white')

# move window center
winWidth = window.winfo_reqwidth()
winwHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))

# eat
def eat(widget):

	# eating
	print('Eating...')

	time.sleep(60)

	# ate
	print('Brush Your Teeth after eating!')
	widget.pack_forget()

	window.configure(bg='deep sky blue')

	byt_btn = Button(window, text="Brush Your Teeth!\n\n (click if you brushed it)", font=font, command=lambda: window.quit()) 
	byt_btn.pack(
		ipadx=75,
	    ipady=50,
	    expand=True
	) 


eat_btn = Button(window, text="Go to eat?", font=font, command=lambda: eat(eat_btn)) 
eat_btn.pack(
	ipadx=75,
    ipady=50,
    expand=True
)

window.mainloop()

# Credits: github.com/esiquiel