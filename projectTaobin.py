tealist = [{'เมนู' :"ชาเขียว" ,'ราคา' : 50 },{'เมนู':"ชาดำ",'ราคา':40},{'เมนู':"ชาเย็น" ,'ราคา':40},{'เมนู':"ชานม",'ราคา':40},{'เมนู':"ชากุหลาบ",'ราคา':50},{'เมนู':"ชามะลิ",'ราคา':50}]
milklist = [{'เมนู' :"นมโอวัลติน" ,'ราคา' : 30 },{'เมนู':"นมไวท์มอลต์",'ราคา':50},{'เมนู':"นมสด" ,'ราคา':30},{'เมนู':"นมชมพู",'ราคา':40}]
fruitlist = [{'เมนู' :"น้ำสตอเบอรี่" ,'ราคา' : 50 },{'เมนู':"น้ำกีวี",'ราคา':50},{'เมนู':"น้ำสัปปะรด" ,'ราคา':50},{'เมนู':"น้ำกระเจี๊ยบ",'ราคา':40},{'เมนู':"น้ำแตงโมง",'ราคา':40},{'เมนู':"น้ำส้ม",'ราคา':40}]
coffeelist = [{'เมนู' :"อเมริกาโน" ,'ราคา' : 60 },{'เมนู':"เอสเปซโซ",'ราคา':60},{'เมนู':"คาปูชิโน" ,'ราคา':60},{'เมนู':"กาแฟดำ",'ราคา':50},{'เมนู':"ลาเต้",'ราคา':55},{'เมนู':"มอคคา",'ราคา':60}]
smoothielist = [{'เมนู' :"สมูทตี้อะโวคาโดกล้วยมะนาว" ,'ราคา' : 40 },{'เมนู':"สมูทตี้สตอเบอร์รี่โยเกิร์ต",'ราคา':55},{'เมนู':"สมูทตี้ส้มมะม่วง" ,'ราคา':40}]
from datetime import*
def mainmenu():
    print("\n")
    now=datetime.today()
    print(now.strftime("%d/%m/%Y %H:%M"))
    print("[เมนูหลัก]")
    print("1.ชา")
    print("2.นม")
    print("3.น้ำผลไม้")    
    print("4.กาแฟ")    
    print("5.สมูตตี้") 
    print("0.ออกจากโปรแกรม")

def menu1():
    global cost
    cost = cost+0
    print("------------")
    print("[เมนูชา]")
    for i in range(len(tealist)):
        print(i+1,tealist[i]['เมนู'],tealist[i]['ราคา'])
    print("9.กลับเมนูหลัก")
    print("0.ออกจากโปรแกรม")
    try:
        print("-----------------")
        num = int(input("Choose : "))
        if num == 9:
            return 9 
        elif num == 0 :
            return 0
        if 1<= num <= len(tealist):   
            print("------------")
            cost = cost + tealist[num-1]['ราคา']
            print(tealist[num-1]['เมนู'],tealist[num-1]['ราคา'])   
            print("-----------------")
        else:
            print("ไม่มีเมนูลำดับนี้ เลือกใหม่") 
        
        cf = input("Continue y/n : ")
        if cf == "y":
            pass
        else:
            print("Amount" ,cost,"baht")
            return 0
    except (ValueError,KeyboardInterrupt):
        print("ขอร้องใส่ตัวเลขครับ")

def menu2():
    global cost
    cost = cost+0
    print("------------")
    print("[เมนูนม]")
    for i in range(len(milklist)):
        print(i+1,milklist[i]['เมนู'],milklist[i]['ราคา'])
    print("9.กลับเมนูหลัก")
    print("0.ออกจากโปรแกรม")
    try:
        print("-----------------")
        num = int(input("Choose : "))
        if num == 9:
            return 9 
        elif num == 0 :
            return 0
        if 1<= num <= len(milklist):   
            print("-----------------")
            cost = cost + milklist[num-1]['ราคา']
            print(milklist[num-1]['เมนู'],milklist[num-1]['ราคา'])   
            print("-----------------")
        else:
            print("ไม่มีเมนูลำดับนี้ เลือกใหม่") 
        
        cf = input("Continue y/n : ")
        if cf == "y":
            pass
        else :
            print("Amount" ,cost,"baht")
            return 0
    except (ValueError,KeyboardInterrupt):
        print("ขอร้องใส่ตัวเลขครับ")

def menu3():
    global cost
    cost = cost+0
    print("------------")
    print("[เมนูน้ำผลไม้]")
    for i in range(len(fruitlist)):
        print(i+1,fruitlist[i]['เมนู'],fruitlist[i]['ราคา'])
    print("9.กลับเมนูหลัก")
    print("0.ออกจากโปรแกรม")
    try:
        print("-----------------")
        num = int(input("Choose : "))
        if num == 9:
            return 9 
        elif num == 0 :
            return 0
        if 1<= num <= len(fruitlist):   
            print("------------")
            cost = cost + fruitlist[num-1]['ราคา']
            print(fruitlist[num-1]['เมนู'],fruitlist[num-1]['ราคา'])   
            print("-----------------")
        else:
            print("ไม่มีเมนูลำดับนี้ เลือกใหม่") 
        
        cf = input("Continue y/n : ")
        if cf == "y":
            pass
        else:
            print("Amount" ,cost,"baht")
            return 0
    except (ValueError,KeyboardInterrupt):
        print("ขอร้องใส่ตัวเลขครับ")

def menu4():
    global cost
    cost = cost+0
    print("------------")
    print("[เมนูกาแฟ]")
    for i in range(len(coffeelist)):
        print(i+1,coffeelist[i]['เมนู'],coffeelist[i]['ราคา'])
    print("9.กลับเมนูหลัก")
    print("0.ออกจากโปรแกรม")
    try:
        print("-----------------")
        num = int(input("Choose : "))
        if num == 9:
            return 9 
        elif num == 0 :
            return 0
        if 1<= num <= len(coffeelist):   
            print("------------")
            cost = cost + coffeelist[num-1]['ราคา']
            print(coffeelist[num-1]['เมนู'],coffeelist[num-1]['ราคา'])   
            print("-----------------")
        else:
            print("ไม่มีเมนูลำดับนี้ เลือกใหม่") 
        
        cf = input("Continue y/n : ")
        if cf == "y":
            pass
        else:
            print("Amount" ,cost,"baht")
            return 0
    except (ValueError,KeyboardInterrupt):
        print("ขอร้องใส่ตัวเลขครับ")

def menu5():
    global cost
    cost = cost+0
    print("------------")
    print("[เมนูสมูดตี้]")
    for i in range(len(smoothielist)):
        print(i+1,smoothielist[i]['เมนู'],smoothielist[i]['ราคา'])
    print("9.กลับเมนูหลัก")
    print("0.ออกจากโปรแกรม")
    try:
        print("-----------------")
        num = int(input("Choose : "))
        if num == 9:
            return 9 
        elif num == 0 :
            return 0
        if 1<= num <= len(smoothielist):   
            print("------------")
            cost = cost + smoothielist[num-1]['ราคา']
            print(smoothielist[num-1]['เมนู'],smoothielist[num-1]['ราคา'])   
            print("-----------------")
        else:
            print("ไม่มีเมนูลำดับนี้ เลือกใหม่") 
        
        cf = input("Continue y/n : ")
        if cf == "y":
            pass
        else:
            print("Amount" ,cost,"baht")
            return 0
    except (ValueError,KeyboardInterrupt):
        print("ขอร้องใส่ตัวเลขครับ")
cost = 0
while True :
    try:
        mainmenu()
        work=int(input("เลือกเมนูที่ต้องการ : "))
        if work == 0 :
            break
        elif work==1:
            if menu1() == 0:
                break
                
        elif work==2:
            if menu2() == 0:
                break
                
        elif work==3:
            if menu3() == 0:
                break
                
        elif work==4:
            if menu4() == 0:
                break

        elif work==5:
            if menu5() == 0:
                break
                
        else :
            print("โปรดใส่เลขที่ระบุบนหน้าจอ")
    except (ValueError,KeyboardInterrupt):
        print(end="")
        print("ขอร้องใส่ตัวเลขครับ")