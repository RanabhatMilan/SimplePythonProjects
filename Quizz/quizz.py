# This is a simple quizz game
# Here we are using class and object concept
# We have a class defined in another file and we are going to create objects of that class
# At first we need to import that class to this file

from ques_ans_class import question_answer

# Now we create list(Array) of objects of class question_answer
questions = [
            question_answer("What is the color of Banana?\n a) Red\n b) Green\n c) Yellow \n d) White\n", "c"),
            question_answer("What is the color of Apple?\n a) Red\n b) Pink\n c) Yellow\n d) Blue\n", "a"),
            question_answer("What is the color of Cucumber?\n a) Red\n b) Pink\n c) Green\n d) Blue\n", "c")
]

def play_quizz(ques):
    score = 0
    for que in ques:
        ans = input(que.question)
        if ans == que.answer:
            score += 1
    print("You got "+str(score)+"/"+str(len(ques))+" correct!")
# Now we pass the questions array to the function
print(play_quizz(questions))
