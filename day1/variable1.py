types_of_people = 10
x = f"세상에는 {types_of_people}종류의 사람이 있다."

binary = "이진수"
do_not = "모르는"
y = f"{binary}를 아는 사람과 {do_not} 사람."

print(x)
print(y)

print(f"{x}라고 했어요")
print(f"'{y}'라고도 했죠")

hilarious = False
joke_evaluation = "웃기는 농담 아니에요 {}"

print(joke_evaluation.format(hilarious))
