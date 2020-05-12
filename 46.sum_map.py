a = list("ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC")

result =list(map(lambda i: 4 if i == 'A' else 3 if  i =='B' else 2 if i =='C' else 1, a))

print(f"{sum(result)}")