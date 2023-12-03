import csv
import random
# this opens the file and retrieves all the questions and adds them to a list
file = open('rrhof.csv', 'r')
all_questions = list(csv.reader(file, delimiter= ','))
file.close()

# delete the header line of the file
all_questions.pop(0)
# prints length of items for reference
print('Length {}'.format(len(all_questions)))

# next we pick a random item from the list
random_question = random.choice(all_questions)
# this tells us what item this is within our list
index_question = all_questions.index(random_question)

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
    choosen_answer = random.choice(all_questions)
    if choosen_answer[0] != random_question[0] and choosen_answer[1] != random_question[1]:
        # now check that the same band is not in the list
        if choosen_answer[1] not in answer_list:
            answer_list.append(choosen_answer[1])

# now add the questions answer to the list

answer_list.append(random_question[1])

# remove the question from the master list so we get no repeats
all_questions.pop(index_question)

# shuffles the list into a new order
random.shuffle(answer_list)
print(answer_list)

print(random_question)



