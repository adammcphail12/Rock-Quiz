import csv
# this opens the file and retrieves all the questions and adds them to a list
file = open('rrhof.csv', 'r')
all_questions = list(csv.reader(file, delimiter= ','))
file.close()

# delete the header line of the file
all_questions.pop(0)
# prints length of items for reference
print('Length {}'.format(len(all_questions)))
