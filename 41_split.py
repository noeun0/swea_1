   # split 함수는 a.split()와 같은 꼴이고 괄호 안에 아무 값도 넣어주지 않으면 공백을 기준으로 문자열을 나누어준다
    # 만약 b.split(':')처럼 괄호 안에 특정 값이 있을 경우에는 괄호 안의 값을 구분자로 해서 문자열을 나눠준다
    # 이렇게 나눈 값은 리스트에 하나씩 들어가게 된다. 
num=input().split(", ")
q=int(num[0])
w=int(num[1])

print("fdsf")

def func1(a,b):
    print(f"square({a}) => {a**2}")
    print(f"square({b}) => {b**2}")

func1(q,w)