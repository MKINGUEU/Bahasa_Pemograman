import tkinter as tk

window = tk.Tk()
window.title(" GUI Dengan Python")
frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label1 = tk.Label(master=frame, text="haloooooo", bg="red")
label1.place(x=0, y=35)

label2 = tk.Label(master=frame, text="Guyssss", bg="yellow")
label2.place(x=70, y=35)

window.mainloop()