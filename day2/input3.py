# 표준 실수 입력
data = input("실수를 입력하시오 : ")
print(data, type(data))
# print(data, type(data), data + 1.2) 에러
# 문자열과 실수는 더하기를 할 수 없다.

data = eval(input("실수를 입력하시오 : "))
print(data, type(data), data + 1.2)

data = float(input("실수를 입력하시오 : "))
print(data, type(data), data + 1.2)
