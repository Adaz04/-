import random
num = random.randint(1,10)
guess_num = int(input("输入你猜的数字:"))
if guess_num == num:
    print("恭喜，结果正确")
else:
    if guess_num > num:
        print("比你这个数字小")
    else:
        print("比你猜的数字大")
    guess_num = int(input("再输入一次:"))
    if guess_num == num:
        print("恭喜，结果正确")
    else:
        if guess_num > num:
            print("比你这个数字小")
        else:
            print("比你猜的数字大")
        guess_num = int(input("错了，再给你最后一次机会:"))
        if guess_num == num:
            print("恭喜，结果正确")
        else:
            print(f"正确答案为:{num}")