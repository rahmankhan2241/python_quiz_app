import json
##
Quiz = {
    "Q": [],
    "O": [],
    "A": [],
    }
#comment
#bdkfjdl
##
print("Press 1 to play and 2 for add Question")
inp = int(input("let me know ur choice: "))

if inp == 2:
    
    while True:
        inp_str = []
        qus = input("Enter a Question : ")
        Quiz["Q"].append(qus)
        for i in range(1,5):
            opt = input(f"Option {i} : ")
            inp_str.append(opt)
        Quiz["O"].append(inp_str)
        ans = int(input("Enter the correct answer : "))
        correct_ans = Quiz["A"].append(ans)
        play = input("Do You Want To Add More question : ")
        if play == "no" or play == "n":
            break
    json_data = json.dumps(Quiz , indent = 3)
    with open("quizGame.json" , "w") as file:
        file.write(json_data)
        
##
elif inp == 1:
    with open("quizGame.json", 'r') as file:
        data = json.load(file)
    
    len_for_loop = len(data['Q'])
    score = 0
    wrong = 0
    right = 0
    for i in range(0,len_for_loop):
        print(f'Question {i+1} : {data["Q"][i]}')
        print(f'Option 1 :{data["O"][i][0]} ')
        print(f'Option 2 :{data["O"][i][1]} ')
        print(f'Option 3 :{data["O"][i][2]}')
        print(f'Option 4 :{data["O"][i][3]}')
        ans = int(input("Enter The correct option : "))
        if ans < 1 or ans > 4:
            print("[ ! ] : Invalid Option")
            if input("Do you want to continue :") == "no":
                break
        elif data["A"][i] == ans:
            print("Bravo")
            score = score +1000
            right += 1
        else:
            print("OOPS!")
            score = score -100
            wrong += 1
            
print(f"Your Score is {score} ")
show = input("Do You Want to Show Your result : ")
if show == "yes" or show == "y":
    print(f"You have entered {wrong} wrong answer and ofcourse {right} correct answer")


        
        

            
