# break문
while True:
    response = input('숫자를입력하세요:')
    if int(response) % 10 == 0:
        print("10으로 나누었을 때 나머지가 0입니다.")
        break

#continue문
i = 0
j = 0
while True:
    i = j + 1
    response = input(f"숫자를 입력하세요(입력횟수[{j}]:")
    result = int(response) % 10
    if result == 0:
        continue
    i = i + 1
    print("10으로 나눈 나머지는 {}입니다.".format(result))
    print(f"반복횟수: {i}")