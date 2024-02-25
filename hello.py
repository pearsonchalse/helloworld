#print("Hello, world!")


# tkinter 사용
#import tkinter

#window = tkinter.Tk()
#window.mainloop()

# tkinter 사용
import tkinter

window = tkinter.Tk()

window.title("Hello, title!")
window.geometry("640x400+100+100")
window.resizable(False, False)

label = tkinter.Label(window, text="This is a label!")

label.pack()

window.mainloop()
