def fa(a,b):
    print("And:- ",(a+b)/2)
fa(90,2)

def fa2(a=20,b=10):
    print("And:- ",(a+b)/2)
fa2()
fa2(10,2)

def avg(*number):
    sum= 0 
    for i in number:
        sum = sum + i 
    print("Avg is " , sum/len(number))

avg(9,9,9,9,9,9,9,9,9,92,29,392,9)
