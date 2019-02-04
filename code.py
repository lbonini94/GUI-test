from tkinter import *

#Create Window
window = Tk()
window.title("Teste - Tese #######")

#geometry of window
window.geometry('1024x720')

#labels
volts = Label(window, text="Tensão  ", font=("Arial", 14))
volts.grid(column=0, row=0)
current = Label(window, text="Corrente  ", font=("Arial", 14))
current.grid(column=0, row=1)

#buttons
btn = Button(window, text="Enviar", bg="orange", fg="red")
btn.grid(column=3, row=0)

#entries
value = Entry(window, width=10)
value.grid(column=2, row=0)

#button click event
def clicked():
    print("clicked")
    #label.configure(text="Button was clicked !!")

#variables
v1 = 14.1
v1l = Label(window, text=str(v1), font=("Arial", 12))
v1l.grid(column=2, row=1)

window.mainloop() #wait until interact

