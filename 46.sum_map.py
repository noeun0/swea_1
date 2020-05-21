a = list("ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC")

result =list(map(lambda i: 4 if i == 'A' else 3 if  i =='B' else 2 if i =='C' else 1, a))

print(f"{sum(result)}")


# 합까지 한번에 map에서 구할 수 있나?
# 람다는... 함수를 선언하는 것!