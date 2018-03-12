from tkinter import *

def clear():
    txtDisplay.delete(0, END)
    return

def Numbers(sign):
    global somelwor
    somelwor = somelwor + str(sign)
    text_Input.set(somelwor)

def sumup():
    global somelwor
    result = str(eval(somelwor))
    text_Input.set(result)
    somelwor = ""

root = Tk()
frame = Frame(root)
frame.pack()
root.title('Kalkulator')
text_Input = StringVar()
somelwor=""

topframe = Frame(root)
topframe.pack(side=TOP)
txtDisplay = Entry(frame, textvariable=text_Input, bd=10, insertwidth=1, font=20)
txtDisplay.pack(side=TOP)

frame1 = Frame(root)
frame1.pack(side=BOTTOM)
button0 = Button(frame1, font="Helvetica", padx=50, pady=15, bd=3, text="0", fg="black", command=lambda:Numbers(0))
button0.pack(side=LEFT)
buttonres = Button(frame1, font="Helvetica", padx=48, pady=15, bd=3, text="C", fg="black", command=clear)
buttonres.pack(side=LEFT)
buttondot = Button(frame1, font="Helvetica", padx=50, pady=15, bd=3, text="=", fg="black", command=sumup)
buttondot.pack(side=LEFT)
buttondz = Button(frame1, font="Helvetica", padx=50, pady=15, bd=3, text="/", fg="black", command=lambda:Numbers("/"))
buttondz.pack(side=LEFT)

frame2 = Frame(root)
frame2.pack(side=BOTTOM)
plusminus = Button(frame2, font="Helvetica", padx=50, pady=15, bd=3, text="1", fg="black", command=lambda:Numbers(1))
plusminus.pack(side=LEFT)
button0 = Button(frame2, font="Helvetica", padx=50, pady=15, bd=3, text="2", fg="black", command=lambda:Numbers(2))
button0.pack(side=LEFT)
buttondot = Button(frame2, font="Helvetica", padx=50, pady=15, bd=3, text="3", fg="black", command=lambda:Numbers(3))
buttondot.pack(side=LEFT)
buttonres = Button(frame2, font="Helvetica", padx=48, pady=15, bd=3, text="+", fg="black", command=lambda:Numbers("+"))
buttonres.pack(side=LEFT)

frame3 = Frame(root)
frame3.pack(side=BOTTOM)
plusminus = Button(frame3, font="Helvetica", padx=50, pady=15, bd=3, text="4", fg="black", command=lambda:Numbers(4))
plusminus.pack(side=LEFT)
button0 = Button(frame3, font="Helvetica", padx=50, pady=15, bd=3, text="5", fg="black", command=lambda:Numbers(5))
button0.pack(side=LEFT)
buttondot = Button(frame3, font="Helvetica", padx=50, pady=15, bd=3, text="6", fg="black", command=lambda:Numbers(6))
buttondot.pack(side=LEFT)
buttonres = Button(frame3, font="Helvetica", padx=50, pady=15, bd=3, text="-", fg="black", command=lambda:Numbers("-"))
buttonres.pack(side=LEFT)

frame4 = Frame(root)
frame4.pack(side=BOTTOM)
plusminus = Button(frame4, font="Helvetica", padx=50, pady=15, bd=3, text="7", fg="black", command=lambda:Numbers(7))
plusminus.pack(side=LEFT)
button0 = Button(frame4, font="Helvetica", padx=50, pady=15, bd=3, text="8", fg="black", command=lambda:Numbers(8))
button0.pack(side=LEFT)
buttondot = Button(frame4, font="Helvetica", padx=50, pady=15, bd=3, text="9", fg="black", command=lambda:Numbers(9))
buttondot.pack(side=LEFT)
buttonres = Button(frame4, font="Helvetica", padx=50, pady=15, bd=3, text="*", fg="black", command=lambda:Numbers("*"))
buttonres.pack(side=LEFT)

root.mainloop()

