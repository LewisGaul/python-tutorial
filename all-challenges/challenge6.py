"github.com/lewisgaul/python-tutorial"
# WEEK 6 CHALLENGE - classes and GUIs

# Work out how the code below works, add in some comments to make it clearer
# where you can.

# First change the code below so that clicking the button stops the timer. If
# there's any style configuration you'd like to do try searching online
# (e.g. search 'tkinter button background colour'), or ask me.

# Use the code below to make a simple game (feel free to use your imagination
# and ask if you need help). Try to include some more widgets.


import tkinter as tk
import time as tm


class TimerGui(tk.Tk):
    def __init__(self):
        super().__init__()
        # Create a Timer instance (defined below).
        self.timer = Timer(self)
        self.timer.pack()
        # Call the method below.
        self.place_button('Click me!')

    def place_button(self, text):
        # When creating a widget (e.g. Button, Label) there are a number of
        # arguments you can pass. Here we give the button text and an action
        # which is a function which will be run when it is clicked.
        button = tk.Button(self, text=text, command=self.button_action)
        # Place the button (it is only created above).
        button.pack()

    def button_action(self):
        print("Button pressed")


class Timer(tk.Label):
    def __init__(self, parent):
        # Create a Label instance from the tk module.
        super().__init__(parent)
        self.start_time = tm.time()
        self.update()

    def update(self):
        # Below is some string formatting (2 decimal places).
        # Configure the text that is displayed on the timer label.
        self.config(text="{:.2f}".format(tm.time() - self.start_time))
        # Run this method again after 1 millisecond.
        self.after(1, self.update)




if __name__ == '__main__':
    gui = TimerGui() #create a gui
    gui.mainloop() #method inherited from tk.Tk (starts the GUI)
