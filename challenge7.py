"github.com/lewisgaul/python-tutorial"
# WEEK 7 CHALLENGE - classes and GUIs

# Take another look at the code below, try to understand where the classes are
# used. If it helps, try simplifying the code by removing it from classes and
# see if you can get it running that way too.

# Use the code below to make noughts and crosses.


import tkinter as tk


class Gui(tk.Tk):
    def __init__(self):
        super().__init__() #Create the main window (like 'window = tk.Tk()')
        # Call the method below.
        self.make_buttons()

    def make_buttons(self):
        # When creating a widget (e.g. Button, Label) there are a various
        # arguments you can pass. Here we give the buttons an action
        # which is a function which will be run when it is clicked.
        self.buttons = []
        for i in range(3):
            b = tk.Button(self, width=11, height=6,
                command=self.get_button_action(i))
            b.grid(row=0, column=i)
            self.buttons.append(b)

    def get_button_action(self, b_num):
        def action():
            print("Button", b_num, "pressed")
            b = self.buttons[b_num]
            b.config(text='O')
        # Return the function which will be called when button is pressed.
        return action




if __name__ == '__main__':
    gui = Gui() #create a gui
    gui.mainloop() #method inherited from tk.Tk (starts the GUI)
