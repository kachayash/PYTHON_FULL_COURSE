# aa java na jevu switch case jevu chhe
 
x = int(input("Enter number:- "))
match x:
    # case a check kare jo c ni value 0 hase to 
    case 0:
        print("X in Zero")
    case 4:
        print("X is Four")
    #_ aa atale else jevu 0 and 4 no hoi and biju kaijk hoi to su op apavu 
    case _:
        print("X is ",x)
