
# create a function that inputs a number and checks that it matches up with specifictaions

def question_input(user_input):
    # set a variable to define if the user's input 'has errors' or not
    has_errors = 'no'

    error_msg = 'Please input a whole number between 1 and 687'

    # runs a try function to see if the functions has errors

    try:
        user = int(user_input)

        if user < 1 or user > 687:
            has_errors = 'yes'

    except ValueError:
        has_errors = 'yes'
    
    if has_errors == 'yes':
        print('num not valid')
    else: 
        print('num is valid')

for item in range(0,6):
    question_input(input('test input:'))



        
