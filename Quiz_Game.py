import random
title = "WELCOME TO THE QUIZ GAME CODE"
print(title.center(68, "="))


prize_money_list=[0,10000,50000,100000,2000000,5000000,10000000,70000000]
def correct_answer(i):
    x=print("That's the right answer!!✅🥳🙌")
    points=prize_money_list[i]
    print("Your prize money right now:", points)
    if points==70000000:
        print("This was the last question!!\n You have reached the top ----> 70000000\n\n\tThe Game Ends Here")
    return x

# def details():
#     print("Prize money you won= ", points)

choice=int(input("Enter the subject number for quiz:\n1.Mathematics\n2.Science : "))
Ques_ans_dict_math={
    '''The value of (x + 3)(x + 3) is:
A) xx + 6x + 9
B) xx + 9
C) xx + 3x + 9
D) xx + 6x + 6''':"a",

'''5x + 7 = 32

Find the value of x:
A) 3
B) 4
C) 5
D) 6''':'c',

'''The distance between points (1, 2) and (4, 6) is:
A) 4
B) 5
C) sqrt(20)
D) 6''':"b",

'''If sin(theta) = 1/2, then theta equals:
A) 30 degrees
B) 45 degrees
C) 60 degrees
D) 90 degrees''':"a",

'''The sum of first 20 natural numbers is:
A) 200
B) 210
C) 220
D) 400''':"b",

'''What is the value of 3x + 5 when x = 4?
A) 12
B) 15
C) 17
D) 20''':"c",

'''Find the value of (a + b)(a - b) when a = 6 and b = 2:
A) 8
B) 16
C) 32
D) 36''':"c"

}

Ques_ans_dict_sci={
    '''Which of the following correctly represents the law of conservation of mass?
A. Mass can be created but not destroyed
B. Mass can be destroyed but not created
C. Total mass remains constant during a chemical reaction
D. Mass increases in every chemical reaction''':"c",

'''If the speed of a body is doubled, its kinetic energy becomes:
A. Twice
B. Three times
C. Four times
D. Half''' : "c",

'''Which of the following is responsible for the bending of light in a prism?
A. Reflection
B. Diffraction
C. Dispersion
D. Refraction''':"d",

'''A substance has a pH value of 3. It is:
A. Strongly acidic
B. Weakly acidic
C. Neutral
D. Basic''':"a",

'''Which part of the nephron is mainly responsible for reabsorption of useful substances?
A. Bowman's capsule
B. Glomerulus
C. Proximal convoluted tubule
D. Collecting duct''':"c",

'''Which part of the cell controls all activities of the cell?
A) Mitochondria
B) Nucleus
C) Ribosome
D) Cytoplasm''':"b",

'''Which metal is liquid at room temperature?
A) Iron
B) Aluminium
C) Mercury
D) Copper''':"c"



}
if choice==1:
    print("\nOkay! Here is a quick recap of the rules:\n1.You should answer in the option's letter format only\n2.Avoid entering empty inputs\n")
    print("So, Here starts the quiz\n")
    keys = list(Ques_ans_dict_math.keys())
    random.shuffle(keys)

    for i in range(7):
        present_ques = keys[i]
        print(present_ques)

        ans = input("Enter Your Answer: ")
        if ans.lower()==Ques_ans_dict_math[present_ques]:
            correct_answer(i+1)
        else:
            print("\nOops! Its the wrong answer❌😔")
            print("Your prize money = ", prize_money_list[i],"\n\tThe Game Ends")
            break
elif choice==2:
    print("\nOkay! Here is a quick recap of the rules:\n1.You should answer in the option's letter format only\n2.Avoid entering empty inputs\n3.You have exactly only 2 hints which you can pick for any 2 questions\n")
    print("So, Here starts the quiz\n")
    keys = list(Ques_ans_dict_sci.keys())
    random.shuffle(keys)

    for i in range(7):
        present_ques = keys[i]
        print(present_ques)

        ans = input("Enter Your Answer: ")
        if ans.lower()==Ques_ans_dict_sci[present_ques]:
            correct_answer(i+1)
        else:
            print("\nOops! Its the wrong answer❌😔")
            print("Your prize money = ", prize_money_list[i],"\n\tThe Game Ends")
            break

else:
    print("Invalid input")
