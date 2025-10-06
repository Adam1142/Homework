from tkinter import *
window  = Tk()
window.title("Length Converter App")
window.geometry("400x400")
def handler_keypress(event):
    """print the character associated with the keypress"""
    print(event.char)
window.bind("<Key>",handler_keypress)
def handle_click(event):
    print("\nthe button was clicked")
button = Button(text = "click me")
button.pack()
button.bind("<Button-1>",handle_click)
window.mainloop()
