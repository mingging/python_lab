# 함수와 변수
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"치즈가 {cheese_count}개나 있어요!")
    print(f"크래커가 {boxes_of_crackers}상자나 있어요!")
    print("파티를 열기에는 충분하네요!")

cheese_and_crackers(20, 30)

amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

cheese_and_crackers(10 + 20, 5 + 6)

cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)