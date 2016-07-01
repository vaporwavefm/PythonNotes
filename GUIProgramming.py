# George Juarez

import tkinter

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

class MySampleLabelGUI:
    
    def __init__(self):
        # create main window widget
        self.main_window = tkinter.Tk()

        # create Label widget with Hellow World
        # first param (self.main_window) is a reference to the root widget
        
        self.label1 = tkinter.Label(self.main_window, text = "Hello World!")
        self.label2 = tkinter.Label(self.main_window, text = "Memes are cool!")
        
        # call Label's pack method
        self.label1.pack(side = 'left')
        self.label2.pack(side = 'left')

        tkinter.mainloop()

    
def main():
    myLabelGUI = MySampleLabelGUI()

# call main
main()
