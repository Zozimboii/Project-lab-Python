def calculate_change(money): # สร้าง dict เพื่อเก็บจำนวนเงินของแต่ละหน่วย
    coins = {20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    for coin in coins: # วนลูปเพื่อหาจำนวนเหรียญแต่ละหน่วย
        while money >= coin:
            money -= coin
            coins[coin] += 1

    return coins.items() # return จำนวนเงินและหน่วยเป็น tuple

# เรียกใช้ function และแสดงผลลัพธ์
money = int(input("กรุณาใส่จำนวนเงิน: "))
change = calculate_change(money)
for coin, num in change:
    print(f"{coin} บาท - {num} เหรียญ")
