
# total 5 quetion 
# 5 point
# 3 point to win

# first quetion



flag = 0 
point = 0 
# 1
q1 = ["Which is Big sate in india"]
opation1 = ["A = Gujrart","B = UP","C = MP","D = Maharastra"]
print(q1)
print(opation1)
Ans = input("Enter Your Ans:- ")
if (Ans  == "D"  or Ans == "d"):
    flag = flag+1
    point = point +1
    print("Ans is cerrect")

else:
    print("Ans Is wrong")
    flag = flag+1


# q2

    
q2 = ["Which is Big City in india"]
opation2 = ["A = Rajkot","B = Surat","C = Baroda","D = Delhi"]
print(q2)
print(opation2)
Ans = input("Enter Your Ans:- ")
if (Ans  == "D"  or Ans == "d"):
    point = point +1
    print("Ans is cerrect")

else:
    print("Ans Is wrong")
    flag = flag+1


# 3

    
q3 = ["Which is Big Curroncy in india"]
opation3 = ["A = 100","B = 200","C = 500","D = 50"]
print(q3)
print(opation3)
Ans = input("Enter Your Ans:- ")
if (Ans  == "C"  or Ans == "c"):
    point = point +1
    print("Ans is cerrect")

else:
    print("Ans Is wrong")
    flag = flag+1


# 4
    
q5 = ["Which is Big River in india"]
quetion5 = ["A = Ganga","B = Narmanda","C = Yamuna","D = Maheswari"]
print(q5)
print(quetion5)
Ans = input("Enter Your Ans:- ")
if (Ans  == "A"  or Ans == "a"):
    point = point +1
    print("Ans is cerrect")

else:
    print("Ans Is wrong")
    flag = flag+1

# 5
    
q5 = ["Who is PM of Indian"]
quetion5 = ["A = PM MODI","B = HU","C = TAME","D = TARA PAPA"]
print(q5)
print(quetion5)
Ans = input("Enter Your Ans:- ")
if (Ans  == "A"  or Ans == "a"):
    point = point +1
    print("Ans is cerrect")

else:
    print("Ans Is wrong")
    flag = flag+1

print(point)


if(point >= 3):
    print("\n ******** \n You win 7 corer \n ********")
else:
    print("Losse") 