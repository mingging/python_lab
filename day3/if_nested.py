print("""
    두 갈래 길이 있습니다. 어디로 갈래요?
""")
door = input("> ")

if door == "1":
    print("선택하세요")
    print("1. 하늘")
    print("2. 땅")
    bear = input("> ")
    if bear == "1":
        print("곰을 만났습니다. 곰은 공격하지 않았지만 당신을 경계하는 듯 보입니다.")
    elif bear == "2":
        print("곰이 당신을 공격합니다! 공격받는 당신은 죽은척하기를 택합니다.")
    else:
        print(f"잘못된 길로 간 당신은 길을 잃어 미아가 되었습니다.")
elif door == "2":
    print("토끼는 당신에게 세 가지 물건을 내밀었습니다.")
    print("1. 토끼의 모자를 가져갑니다.")
    print("2. 토끼의 노란 자켓을 가져갑니다.")
    print("3. 토끼의 시계를 가쟈갑니다.")
    oz = input("> ")

    if oz == "1" or oz == "2":
        print("당신이 2대 토끼가 되었습니다! 앨리스를 데려와주세요!")
    else:
        print("토끼의 시계로 시간을 되돌렸습니다.")

else:
    print("당신은 잘못된 길을 택했습니다. 다시는 빠져나올 수 없는 미궁에 갇혀 누군가 오기만을 기다려야할 것입니다.")