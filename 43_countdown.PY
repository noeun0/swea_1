a = int(input())

def countdown(m):

    if a<=0:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
    else:
        for i in range(m, 0, -1):
            print(f"{i}")

countdown(a)
    