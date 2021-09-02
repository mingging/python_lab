formmater = "{} {} {} {}"

print(formmater.format(1,2,3,4))
print(formmater.format("one", "two", "three", "four"))
print(formmater.format(True, False, True, False))
print(formmater.format(formmater, formmater, formmater, formmater))
print(formmater.format("I had this thing", "That you could type up right","But it didn't sing", "So I said goodnight"))

w = "이 문자열의 왼쪽 ..."
e = "이 문자열의 오른쪽."

print(w + e)