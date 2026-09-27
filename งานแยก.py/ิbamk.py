
try:
    score1 = float(input("เงินเริ่มต้น"))
    score2 = int(input("จำนวนเงินฝาก"))
    re = score1
    if score2 > 0:
        re = score1 + score2
    elif  score2 < 0:
        print("จำนวนเงินฝากต้องมากกว่า 0")
    print(f"ยอดเงินคงเหลือ: {re}")    
except ValueError:
    print(f"จำนวนเงินฝากต้องเป็นตัวเลขเท่านั้น ")          
finally:
    print("สิ้นสุดรายการฝากเงิน")                            