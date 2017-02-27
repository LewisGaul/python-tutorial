"github.com/lewisgaul/python-tutorial"
# WEEK 6 CHALLENGE - classes and GUIs

# The code below makes a timer inside a GUI which can be stopped and started.


import tkinter as tk
import time as tm


# The code here doesn't define any new classes, but it's less structured.
window = tk.Tk() #Initialise the tkinter window with the Tk class.
timer = tk.Label(window, text='0.00', bg='black', fg='turquoise',
    font=('Arial', 20, 'bold'))
timer.pack()
start_time = tm.time()
stop = False

def stop_timer():
    global stop #Making variables global is bad practice! Use classes!
    stop = True
    
def update_timer():
    timer.config(text="{:.2f}".format(tm.time() - start_time))
    if not stop:
        # Run this method again after 1 millisecond.
        window.after(1, update_timer)

# Here we give the button text and an action
# which is a function which will be run when it is clicked.
stop_button = tk.Button(window, text='Stop', command=stop_timer)
stop_button.pack()
update_timer() #Start timer
window.mainloop() #Start GUI


# The version below using classes makes it much easier to create and include a
# second timer, for example, since the variables like start_time belong in the
# Timer class.
class TimerGui(tk.Tk):
    def __init__(self):
        super().__init__()
        # Create a Timer instance (defined below).
        self.timer = Timer(self, start=False)
        self.timer.pack()
        # Call the method below.
        self.create_buttons()

    def create_buttons(self):
        # When creating a widget (e.g. Button, Label) there are a number of
        # arguments you can pass.
        frame = tk.Frame(self)
        frame.pack()
        # Here we give the button text and an action
        # which is a function which will be run when it is clicked.
        start_button = tk.Button(frame, text='Start', command=self.start_timer)
        # Place the button (it is only created above).
        start_button.pack(side='left')
        stop_button = tk.Button(frame, text='Stop', command=self.stop_timer)
        stop_button.pack(side='left')

    def start_timer(self):
        print("Start button pressed")
        self.timer.restart() #Use method defined in Timer class (below)
        
    def stop_timer(self):
        print("Stop button pressed")
        self.timer.stop = True #Change the 'stop' attribute on the timer


class Timer(tk.Label):
    def __init__(self, parent, start=True):
        # Create a Label instance from the tk module.
        super().__init__(parent, text='0.00', bg='black', fg='turquoise',
                         font=('Arial', 20, 'bold'))
        self.start_time = tm.time()
        self.paused_time = 0 #Time displayed on the timer when it's (re)started
        # Use the optional argument 'start' to determine whether the timer
        # starts automatically.
        self.stop = not(start)

    def update(self):
        # Below is some string formatting (2 decimal places).
        # Configure the text that is displayed on the timer label.
        self.config(text="{:.2f}".format(
            tm.time() - self.start_time + self.paused_time))
        if self.stop:
            self.paused_time += tm.time() - self.start_time 
        else:
            # Run this method again after 1 millisecond.
            self.after(1, self.update)

    def restart(self):
        # Restart the timer from where it was.
        self.stop = False
        self.start_time = tm.time()
        self.update()



if __name__ == '__main__':
    gui = TimerGui() #create a gui
    gui.mainloop() #method inherited from tk.Tk (starts the GUI)



    
