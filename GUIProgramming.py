# George Juarez

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
# 

import tkinter

def main():
    main_window = tkinter.Tk()

    tkinter.mainloop()

# call main
main()
