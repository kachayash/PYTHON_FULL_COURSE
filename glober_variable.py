x = 10 # gloabla variable
def my ():
    global x
    x= 4
    y = 5 #local variable
    print(y)

my()
print(x)

