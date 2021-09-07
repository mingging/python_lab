class Fruit:
    def __init__(self):
        self.fruit = "귤이 먹고 싶어졌다."
    
    def get_apple(self):
        print("사과 한 상자를 배송했습니다.")

myfruit = Fruit()
myfruit.get_apple()
print(myfruit.fruit)