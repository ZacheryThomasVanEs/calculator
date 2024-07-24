import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

#Window setup
window = tk.Tk()
window.title('Calculator')
frame = tk.Frame(master=window, bg="grey", padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

#Function for entering input into window for each button
def myclick(number):
    entry.insert(tk.END, number)

#Function to evaluate current expresion in input
def equal():
    try:
        answer = str(eval(entry.get(),{"__builtins__":None},{}))
        entry.delete(0, tk.END)
        entry.insert(0, answer)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry.delete(0, tk.END)

#Create Number Buttons
button_1 = tk.Button(master=frame, text='1', padx=15, pady=5, width=3, command=lambda: myclick(1))
button_1.grid(row=1, column=0, pady=2)
button_2 = tk.Button(master=frame, text='2', padx=15, pady=5, width=3, command=lambda: myclick(2))
button_2.grid(row=1, column=1, pady=2)
button_3 = tk.Button(master=frame, text='3', padx=15, pady=5, width=3, command=lambda: myclick(3))
button_3.grid(row=1, column=2, pady=2)
button_4 = tk.Button(master=frame, text='4', padx=15, pady=5, width=3, command=lambda: myclick(4))
button_4.grid(row=2, column=0, pady=2)
button_5 = tk.Button(master=frame, text='5', padx=15, pady=5, width=3, command=lambda: myclick(5))
button_5.grid(row=2, column=1, pady=2)
button_6 = tk.Button(master=frame, text='6', padx=15, pady=5, width=3, command=lambda: myclick(6))
button_6.grid(row=2, column=2, pady=2)
button_7 = tk.Button(master=frame, text='7', padx=15, pady=5, width=3, command=lambda: myclick(7))
button_7.grid(row=3, column=0, pady=2)
button_8 = tk.Button(master=frame, text='8', padx=15, pady=5, width=3, command=lambda: myclick(8))
button_8.grid(row=3, column=1, pady=2)
button_9 = tk.Button(master=frame, text='9', padx=15, pady=5, width=3, command=lambda: myclick(9))
button_9.grid(row=3, column=2, pady=2)
button_0 = tk.Button(master=frame, text='0', padx=15, pady=5, width=3, command=lambda: myclick(0))
button_0.grid(row=4, column=1, pady=2)

#Create operation buttons
button_add = tk.Button(master=frame, text='+', padx=15, pady=5, width=3, command=lambda: myclick('+'))
button_add.grid(row=5, column=0, pady=2)
button_sub = tk.Button(master=frame, text='-', padx=15, pady=5, width=3, command=lambda: myclick('-'))
button_sub.grid(row=5, column=1, pady=2)
button_multi = tk.Button(master=frame, text='*', padx=15, pady=5, width=3, command=lambda: myclick('*'))
button_multi.grid(row=5, column=2, pady=2)
button_div = tk.Button(master=frame, text='/', padx=15, pady=5, width=3, command=lambda: myclick('/'))
button_div.grid(row=6, column=0, pady=2)

#Create function buttons
button_clear = tk.Button(master=frame, text='clear', padx=15, pady=5, width=12, command=clear)
button_clear.grid(row=6, column=1, columnspan=2, pady=2)
button_equal = tk.Button(master=frame, text='=', padx=15, pady=5, width=5, command=equal)
button_equal.grid(row=7, column=1, pady=2)


#Starts the window
window.mainloop()
