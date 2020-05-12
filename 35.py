a = input()
b = input()
c = input()
d = input()


def func(c,d):
    if c == "가위" : 
        if d =="가위":
            print("비겼습니다.")
        if d =="바위":
            print(f"{d}가 이겼습니다!")
        if d =="보":
            print(f"{a}가 이겼습니다!")        

    if c == "바위" : 
        if d =="가위":
            print(f"{a}가 이겼습니다!")
        if d =="바위":
            print("비겼습니다.")
        if d =="보":
            print(f"{b}가 이겼습니다!")        


    if c == "보" : 
        if d =="가위":
            print(f"{b}가 이겼습니다!")
        if d =="바위":
            print(f"{a}가 이겼습니다!")
        if d =="보":
            print("비겼습니다.")        
func(c,d)            