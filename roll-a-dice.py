import random
res= "y"
def rolladice(res):
    while res == "y":
        num=random.randint(1,6)
        if num == 1 :
            print("[- - -]")
            print("[- 0 -]")
            print("[- - -]")
        if num == 2 :
            print("[- - -]")
            print("[0 - 0]")
            print("[- - -]")
        if num == 3 :
            print("[- - 0]")
            print("[- 0 -]")
            print("[0 - -]")   
        if num == 4 :
            print("[0 - 0]")
            print("[- - -]")
            print("[0 - 0]")
        if num == 5 :
            print("[0 - 0]")
            print("[- 0 -]")
            print("[0 - 0]")
        if num == 6 :
            print("[0 - 0]")
            print("[0 - 0]")
            print("[0 - 0]")  
        res=input("PRESS (y) TO ROLL AGAIN AND PRESS (n) TO EXIT")          
        print("\n")
    #print(num)
rolladice(res)
