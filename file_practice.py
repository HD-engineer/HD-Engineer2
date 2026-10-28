category = input("분류를 입력하세요: ")
amount = int(input("금액을 입력하세요: "))
with open("expense.txt", "a", encoding="utf-8") as file:
    file.write(f"\n{category} {amount}원")

print("지출이 저장됐습니다!")

with open("expense.txt", "r", encoding="utf-8") as file:
    content = file.read()


print("=== 저장된 지출 ===")
print(content)