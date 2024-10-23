print("GoodLuck on your quiz")

playing=input("Do you want to start? \n     yes/no \n").lower()

if playing== "no":
    quit()
elif playing== "yes":
    print("ok let us begin.")
    score=0

    answer=input("what does CPU stands for?\n").lower()
    if answer=="central processing unit":
        score=score+1
        print ("correct,yes")
    else:
         print("Incorrect answer")

    answer=input("what does RAM stands for?\n").lower()
    if answer=="random access memory":
        score=score+1
        print ("correct")
    else:
        print("Incorrect answer")

    answer=input("what does ROM stands for?\n").lower()
    if answer=="read only memory":
         score=score+1
         print ("correct")
    else:
        print("Incorrect answer")

    print(f"you have got "+ str(score)+" of 3")
else:
    quit()