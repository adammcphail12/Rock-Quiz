from tkinter import *
from functools import partial # to prevent unwanted windows




class Quiz():
    def __init__(self):
        #common format for all buttons
        BUTTON_FONT = ('Arial', '12', 'bold')
        BUTTON_FG = '#ffffff'

        # sets up the frame

        self.quiz_frame = Frame(padx=10,pady=10, bg = '#50808E')
        self.quiz_frame.grid()

        # the heading label

        self.quiz_heading = Label(self.quiz_frame, text='Rock and Roll Hall of Fame Inductee Quiz', font = BUTTON_FONT, bg = '#A3C9A8', bd = 2, relief='ridge')
        self.quiz_heading.grid(row=0,padx=10,pady=10)


        # This is te instructions Label

        instructions_text = 'The Rock and Roll Hall of Fame Inductee Quiz is a multi choice band quiz. The quiz will give you the name of a inductee and you have to pick which band they were from. Enter the amount of questions you would like to play with below, and then press the Begin Quiz Button. The maximum amount of questions is 687.'

        self.instructions_label = Label(self.quiz_frame, text = instructions_text, font = ('Arial', '9',), bg = '#A3C9A8', bd = 2, relief = 'ridge', wraplength= 250)
        self.instructions_label.grid(row=1,padx=5,pady=10)

        # this is the entry box
        
        self.quiz_question_entry = Entry(self.quiz_frame, font=('Arial','14'))
        self.quiz_question_entry.grid(row=2,padx=10,pady=10)

        # and this is the error label

        self.error_label = Label(self.quiz_frame, text = '', font = BUTTON_FONT,fg = '#ED2939',bg='#50808E',wraplength=250)
        self.error_label.grid(row=3,padx=10,pady=10)

        # this is the Start quiz button

        self.start_button = Button(self.quiz_frame, text = 'Begin Quiz!', bg='#DDD8C4', fg = '#FFFFFF', font = BUTTON_FONT, command=self.question_input)
        self.start_button.grid(row=4,padx=10,pady=10)
    
    def question_input(self):
        # set a variable to define if the user's input 'has errors' or not
        has_errors = 'no'

        error_msg = 'Please input a whole number between 1 and 687'


        # runs a try function to see if the functions has errors

        try:
            # gets entry from our entry box
            response = self.quiz_question_entry.get()
            # checks to see if it is a interger
            response = int(response)

            # checks to see if it  fits in the range
            if response < 1 or response > 687:
                has_errors = 'yes'
        # this is what happens if its not a valid interger
        except ValueError:
            has_errors = 'yes'
    
        if has_errors == 'yes':
            # now we change our error labels config to show the user the the error message because they have errors.
            self.error_label.config(text=error_msg)

        else: 
            # make sure that the error message is not showing if the users input is valid.\
            self.error_label.config(text='')
            




# main routine

if __name__ == '__main__':
    root = Tk()
    root.title('Hall Of Fame Quiz')
    # calling class
    Quiz()
    root.mainloop()