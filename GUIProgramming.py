# George Juarez

import tkinter
import tkinter.messagebox

# 14.2
# tkinter module ("TK interface") is used to create simple GUI programs
# comes with widgets that the user can interact with or view
'''
# this code creates a main window widget and enter tkinter main loop
# should be placed in a class, MyGUI

class MyGUI:
    def __init__(self):
         main_window = tkinter.Tk()
         tkinter.mainloop()

# create instance of MyGUI class

myGui = MyGUI()

''' 

# an info dialog box is a simple window that displays a message to the user and has an OK buttom
# that dismissed the dialog box. (can use tkinter.messagebox module's showinfo function to show that)
# callback function: aka event handler, handles the event that occurs when the user clicks the button


class MySampleLabelFrameGUI:
    
    def __init__(self):
        # create main window widget
        self.main_window = tkinter.Tk()

        # create two frames, one for top and one for bottom window
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create Label widget with Hello World
        # first param (self.main_window) is a reference to the root widget
        
        self.label1 = tkinter.Label(self.main_window, text = "Hello World!")
        self.label2 = tkinter.Label(self.main_window, text = "Memes are cool!")
        self.label3 = tkinter.Label(self.main_window, text = "But ISIS is not.")
        
        # call Label's pack method, will all be on top of each other
        self.label1.pack(side = 'top')
        self.label2.pack(side = 'top')
        self.label3.pack(side = 'top')

        # make 3 more Label widgets for bottom frame
        self.label4 = tkinter.Label(self.main_window, text = "Foo")
        self.label5 = tkinter.Label(self.main_window, text = "Bar")
        self.label6 = tkinter.Label(self.main_window, text = "Fum")

        # and then pack them into the bottom frame
        self.label4.pack(side = 'left')
        self.label5.pack(side = 'left')
        self.label6.pack(side = 'left')

        # and pack frames too
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


# for organization purposes, i guess, ill just make a new class for button widgets

class MyButtonGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()

        # create Button widget. do_something method will execute when user clicks button
        # also create quit button, to demonstrate the destroy feature
        # also pack buttons
        self.my_button = tkinter.Button(self.main_window, text = "Click me!", command = self.do_something)
        self.quit_button = tkinter.Button(self.main_window, text = "Quit", command = self.main_window.destroy)

        self.my_button.pack()
        self.quit_button.pack()
        
        tkinter.mainloop()

    # callback function for button widget
    def do_something(self):
        tkinter.messagebox.showinfo('Response', "Thanks for clicking me. :)")

def main():
    # uncomment each testX to see how each class above works
    
    # testLabelFrameGUI = MySampleLabelFrameGUI()
    testButtonGUI = MyButtonGUI()

    
# call main
main()
