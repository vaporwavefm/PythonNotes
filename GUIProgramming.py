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

# replica of the Tip, Tax, Total problem
# ask user for subtotal, generates the recommended tip (15%), the tap, and the total (including tip and tax)
# TODO: add in the tax and tip features

class TipTaxTotalGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create widgets for top frame and pack
        
        self.prompt_label = tkinter.Label(self.top_frame, text = "Enter your subtotal: $")
        self.subtotal_entry = tkinter.Entry(self.top_frame, width = 10)
        
        self.prompt_label.pack(side = 'left')
        self.subtotal_entry.pack(side = 'left')

        # create widget for mid frame
        self.descr_label = tkinter.Label(self.mid_frame, text = "Your total is:")

        # need a StringVar obj to associate with an output label...use obj's set method to store string of blank chars
        self.value = tkinter.StringVar()

        # create a label and associate it with StringVar obj...any value sotre in StringVar obj will automatically be
        # be displayed in the label

        self.total_label = tkinter.Label(self.mid_frame, textvariable = self.value)

        #finally pack middle frame widgets

        self.descr_label.pack(side = 'left')
        self.total_label.pack(side = 'left')
        
        # create button widgets for the bottom frame

        self.calc_button = tkinter.Button(self.bottom_frame, text = 'Find total', command = self.calc_total)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)

        # pack buttons and frames
        
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def calc_total(self):
        total = format(float(self.subtotal_entry.get()) * 1.08875, '.2f')

        self.value.set(total)

# object below to demonstrate radio button feature on tkinter

class MyRadioGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        #two frames, one for Radiobuttons and another for regular button widgets

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # IntVar is for association of Radiobuttons, it stores unique integer value of a selected RadioButton
        # set to 1
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # create radiobutton widgets for top frame and pack
        self.rb1 = tkinter.Radiobutton(self.top_frame, text = "Mark Foster", variable= self.radio_var, value = 1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text = "Mark Pontius", variable= self.radio_var, value = 2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text = "Cubbie Fink", variable= self.radio_var, value = 3)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # create ok and quit buttons, pack them afterwards (along with top and bottom frames)
        self.ok_button = tkinter.Button(self.bottom_frame, text = "OK", command = self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text = "Quit", command = self.main_window.destroy)

        self.ok_button.pack(side = 'left')
        self.quit_button.pack(side = 'right')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo("Selection", "You selected option " + str(self.radio_var.get()))

# object below shown to demonstrate usage of the checkbutton feature

class MyCheckButtonGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create 3 IntVar objs to use with checkbuttons, and set all to 0
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        # create checkbutton widgets in top frame, and pack
        self.cb1 = tkinter.Checkbutton(self.top_frame, text = "Eggs", variable = self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text = "Milk", variable = self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text = "Cheese", variable = self.cb_var3)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        # create OK and quit buttons, and pack
        self.ok_button = tkinter.Button(self.bottom_frame, text = "OK", command = self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text = "Quit", command = self.main_window.destroy)

        self.ok_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    # show_choice is callback function for pressing OK button
    def show_choice(self):

        # create message str and determine which checkbuttons are selected and build message string accordingly
        self.message = "You selected choice(s):\n"

        if self.cb_var1.get() == 1:
            self.message = self.message + '1\n'
        if self.cb_var2.get() == 1:
            self.message = self.message + '2\n'
        if self.cb_var3.get() == 1:
            self.message = self.message + '3\n'

        # display message in an info dialog box
        tkinter.messagebox.showinfo("Selection", self.message)
            
def main():
    # uncomment each testX to see how each class above works
    
    # testLabelFrameGUI = MySampleLabelFrameGUI()
    # testButtonGUI = MyButtonGUI()
    # testTipTaxTotalGUI = TipTaxTotalGUI()
    # testRadioGUI = MyRadioGUI()
    testCheckButtonGUI = MyCheckButtonGUI()
    
# call main
main()
