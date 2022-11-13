print("know your grades")
score=int(input("enter your score: "))
if score<25:
    print("you've been graded F, study hard")
elif score>25 and score<45:
    print("you've been graded E, you need to study more" )
elif score>45 and score<50:
    print("you've have been graded D, can do better ")
elif score>50 and score<75:
    print("you've been graded B, good but keep going")
elif score>75 and score<100:
    print(" you've been graded A, very good, be consistent")
else:
    print("invalid input")
 
