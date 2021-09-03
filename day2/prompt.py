from sys import argv

script, user_name = argv
prompt = '> '

print(f"안녕 {user_name}, 나는 {script} 스크립트야")
print("질문 몇가지 해도 될까?")
print(f"{user_name}, 나 좋아해?")
likes = input(prompt)

print(f"{user_name}, 어디 살아?")
lives = input(prompt)

print("어떤 컴퓨터 가지고 있어?")
computer = input(prompt)

print(f"""
좋아, 날 좋아하냐는 물음이 {likes}라고 대답했지,
넌 {lives}에 사는구나
{computer}를 가졌다니 멋진걸""")