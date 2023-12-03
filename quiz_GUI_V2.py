from tkinter import *
from functools import partial # to prevent unwanted windows
import csv
import random




class Start_Page():
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
            self.to_quiz(response)
    
    def to_quiz(self, response):
        Play(response)
        root.withdraw()
    

class Play:
    def __init__(self, rounds):

        self.total_rounds = rounds

        self.play_box = Toplevel()

        BUTTON_FONT = ('Arial', '12', 'bold')

        # initially set rounds played and rounds won to 0
        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        self.rounds_done = 0

        self.rounds_won = IntVar()
        self.rounds_won.set(0)

        # lists to hold user score/s
        # used to work out statistics

        self.user_scores = []

        # get all questions for use in game
        self.all_questions = self.get_questions()

        # creates a space to hold info for question
        self.value = []

        # sets up new frame
        self.play_frame = Frame(self.play_box, padx=10,pady=10, bg = '#50808E')
        self.play_frame.grid()
        

        self.title = Label(self.play_frame, text = 'Insert Question Here', font = BUTTON_FONT, bg='#DDD8C4',bd = 2, relief='ridge', wraplength=250)
        self.title.grid(row=0,column=0,padx=10,pady=10)

        self.quiz_round_label = Label(self.play_frame, text = '{} / {}'.format(self.rounds_done, self.total_rounds),font = BUTTON_FONT, bg= '#A3C9A8', bd = 2, relief='ridge')
        self.quiz_round_label.grid(row=0,column=1,padx=10,pady=10)

        


        # row 2
        # create colour buttons (in choce frame)!
        self.answer_frame = Frame(self.play_frame,bg = '#50808E')
        self.answer_frame.grid(row=1, columnspan=2, padx=10,pady=10)

        self.answer_button_1 = Button(self.answer_frame, text = 'Answer 1', bg = '#EA6B66', width=20, font = BUTTON_FONT, fg = '#FFFFFF', wraplength=150)
        self.answer_button_1.grid(row=0,column=0,padx=5,pady=5)

        self.answer_button_2 = Button(self.answer_frame, text = 'Answer 2', bg = '#FFCE9F', width=20, font = BUTTON_FONT, fg = '#FFFFFF',wraplength=150)
        self.answer_button_2.grid(row=0,column=1,padx=5,pady=5)

        self.answer_button_3 = Button(self.answer_frame, text = 'Answer 3', bg = '#FFD966', width=20, font = BUTTON_FONT, fg = '#FFFFFF',wraplength=150)
        self.answer_button_3.grid(row=1,column=0,padx=5,pady=5)

        self.answer_button_4 = Button(self.answer_frame, text = 'Answer 4', bg = '#FFB570', width=20, font = BUTTON_FONT, fg = '#FFFFFF',wraplength=150)
        self.answer_button_4.grid(row=1,column=1,padx=5,pady=5)



        #row 3 

        # creates a results label
        self.results_text = 'Pick an answer from above.'

        self.results_label = Label(self.play_frame,text= self.results_text, fg = '#FFFFFF', font = ('Arial', '11',), bg = '#50808E', wraplength=250 )
        self.results_label.grid(row=2,column=0,padx=10,pady=10)

        # creates next round button.
        self.next_round = Button(self.play_frame,text= 'Next Round',fg='#FFFFFF',bg='#FFF2CC',width=10,font=('Arial', '12','bold'),command = lambda: self.new_round(),state=DISABLED)
        self.next_round.grid(row=2,column=1,padx=5,pady=5)

        self.new_round()


        




        # row 4 

        self.control_frame = Frame(self.play_frame, bg = '#50808E')
        self.control_frame.grid(row=3, columnspan=2)
        control_buttons=[
            ['#67AB9F','Help','get help'],
            ['#A3C9A8','Statistics','get stats'],
            ['#C3ABD0','Start Over','start over']
        ]

        self.control_button_ref = []

        for item in range(0,3):
            self.make_control_button=Button(self.control_frame,\
                                            fg='#FFFFFF',bg=control_buttons[item][0],\
                                            text=control_buttons[item][1],\
                                            width=11,font=('Arial','12','bold'),\
                                            command=lambda i=item:self.to_do(control_buttons[i][2]))
            self.make_control_button.grid(row=0,column=item,padx=5,pady=5)
            # add buttons to control list
            self.control_button_ref.append(self.make_control_button)



    


    # this is the retrieve questions function
    def get_questions(self):
        # this opens the file and retrieves all the questions and adds them to a list
        file = open('rrhof.csv', 'r')
        all_questions = list(csv.reader(file, delimiter= ','))
        file.close()
        # delete the header line of the file
        all_questions.pop(0)  
        return all_questions
    
    def create_question(self):
        # next we pick a random item from the list
        random_question = random.choice(self.all_questions)
        

        #phrase the question
        question_phrase = 'Which of the following bands did {} play in?'.format(random_question[0])
        print(question_phrase)
        # next we need to get three other bands, that are different from the one we allready have,
        # remember, each band has multiple members so their is a small chance that the same band could come up in our list,
        # some of these artists appear in multiple bands too,(take a look at Jimmy Paige - he is in The Yard birds and Led Zepplin) 
        # so we need to check that an artist doesnt have two of their own 
        # bands appear, because that would make for a unfair and inacurate system.

        # this sets our list of possible answers 
        answer_list = []

        while len(answer_list) < 3:
            choosen_answer = random.choice(self.all_questions)
            if choosen_answer[0] != random_question[0] and choosen_answer[1] != random_question[1]:
                # now check that the same band is not in the list
                if choosen_answer[1] not in answer_list:
                    answer_list.append(choosen_answer[1])

        # now add the questions answer to the list

        answer_list.append(random_question[1])

        # shuffles the list into a new order
        random.shuffle(answer_list)

        # removes question from master list
        index_question = self.all_questions.index(random_question)
        self.all_questions.pop(index_question)

        

        return random_question, answer_list, question_phrase
    
    def new_round(self):
        self.info = self.create_question()
        
        

        # sets buttons and labels     
        self.next_round.config(state=DISABLED)

        self.title.config(text = self.info[2])
        self.answer_button_1.config(text= self.info[1][0],command= lambda: self.answer_question(self.info[1][0]), state = NORMAL)
        self.answer_button_2.config(text= self.info[1][1],command= lambda: self.answer_question(self.info[1][1]),state = NORMAL)
        self.answer_button_3.config(text= self.info[1][2],command= lambda: self.answer_question(self.info[1][2]), state = NORMAL)
        self.answer_button_4.config(text= self.info[1][3],command= lambda: self.answer_question(self.info[1][3]), state = NORMAL)
        self.results_label.config(text=self.results_text, fg = '#FFFFFF')

    
    def answer_question(self, user_answer):
        # disables all buttons.
        self.answer_button_1.config(state=DISABLED)
        self.answer_button_2.config(state=DISABLED)
        self.answer_button_3.config(state=DISABLED)
        self.answer_button_4.config(state=DISABLED)

        # enable next round button.
        self.next_round.config(state=NORMAL)


        # checks to see if answer is correct
        if user_answer == self.info[0][1]:
            print('You answered correct')
            # Increase rounds won 
            self.rounds_won.set(self.rounds_won.get() + 1)
            print('Rounds Won: {}'.format(self.new_round))
            # adjust to show that you got correct and show player profile and change colour 
            self.results_label.config(text='You answered Correct. Player Profile: {} - {}'.format(self.info[0][0],self.info[0][2]), fg = '#008000')

        else:
            print('Sorry thats the wrong answer')
            # show that answer is not true and change colour
            self.results_label.config(text='You answered Incorrect. Player Profile: {} - {}'.format(self.info[0][0],self.info[0][2]), fg = '#FF0000')
        
        self.rounds_done +=1
        self.rounds_played.set(self.rounds_played.get() + 1)
        
        self.quiz_round_label.config(text='{}/{}'.format(self.rounds_done,self.total_rounds))
         # checks to see if game is finnshed
        if self.rounds_played.get() == self.total_rounds:
            self.end_game()

       




    def to_do(self, action):
        if action == 'get help':
            print('get help')
        if action == 'get stats':
            print('get stats')
        if action == 'start over':
            self.close_play()

    def end_game(self):
        self.results_label.config(text = 'Congratulations youve finnshed the game with a total score of : {} out of {}'.format(self.rounds_won.get(), self.total_rounds), fg = '#FFFFFF')
        self.next_round.config(state=DISABLED)
        


    def close_play(self):
        # reshow root (ie: choose rounds) and end current 
        # game / allow new game to start
        root.deiconify()
        self.play_box.destroy()



        
            




# main routine

if __name__ == '__main__':
    root = Tk()
    root.title('Hall Of Fame Quiz')
    # calling class
    Start_Page()
    root.mainloop()