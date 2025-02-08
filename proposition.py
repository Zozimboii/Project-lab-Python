P=[True,False]
Q=[True,False]
R=[True,False]
W=[0,1]
X=[0,1]
Y=[0,1]
Z=[0,1]

def mainmenu():
    print("1.Proposition")
    print("2.Booleanexpression")
    print("0.Exit")

def exit():
    print("\n")
    print(" Exit Program")

def Proposition():
    print("\tp\t \tq\t   \tr\t   \tp^q\t    ((p^q)v r')\t       (pvq')\t   (p^q)v r')<->(pvq')\t")
    print("..........................................................................................................................")
    for p in P:
        for q in Q:
            for r in R:
                print(f"\t{p}\t\t{q}\t\t{r}\t\t{p and q}\t\t{(p and q) or not r}\t\t{p or not q}\t\t{((p and q) or not r)==(p or not q)}\t")
    print("\n")
    print("1.Mainmenu")
    print("2.exit")
    t=True
    while t:
        try:
            Nummain=(int(input("enter choice:")))
            print("\n")
            if Nummain==1:
                t=False
                return mainmenu()
            elif Nummain==2:
                print("Exit Program")
                return 0
        except IndexError:
            print("\n")
            print("please enter number in choice")
        except (ValueError , ZeroDivisionError):
            print("\n")
            print("please enter number in choice")



def Booleanexpression():
    #(* = and)
    #(+ = or)
    #(' = not)
    print("w\t x\t y\t z\t        xw\t      (x'z)'\t      (yz')\t  xw+(x'z)'+(yz')\t")
    print(".............................................................................................................................")
    for w in W:
        for x in X:
            for y in Y:
                for z in Z:
                    func1=(x and w)
                    func2=not(not x and z)
                    if func2 ==True:
                        expression1=1
                    elif func2 ==False:
                        expression1=0
                    func3=(y and not z)
                    if func3 == True:
                        expression2=1
                    else:
                        expression2=0
                    Allexpression=(x and w)or not(not x and z)or(y and not z)
                    if Allexpression==True:
                        expression3=1
                    else:
                        expression3=0
                    print(f"{w}\t {x}\t {y}\t {z}\t \t{func1}\t \t{expression1}\t \t{expression2}\t \t{expression3}")
    print("\n")
    print("1.Mainmenu")
    print("2.exit")
    t=True
    while t:
        try:
            Nummain=(int(input("enter choice:")))
            print("\n")
            if Nummain==1:
                t=False
                return mainmenu()
            elif Nummain==2:
                print("Exit Progarm")
                return 0
                    
        except IndexError:
            print("\n")
            print("please enter number in choice")
        except (ValueError , ZeroDivisionError):
            print("\n")
            print("please enter number in choice")



while True:
    try:
        print("Pruksakorn Saiweal")
        print("6530200720")
        print(mainmenu())
        N=int(input("enter number"))
        if N==1:
            w= Proposition()
            break
        elif N==2:
            w= Booleanexpression()           
            break
        elif N==0:
            w= exit()

            break
    except IndexError:
        print("\n")
        print("please enter number in choice")
    except (ValueError , ZeroDivisionError):
        print("\n")
        print("please enter number in choice")

    