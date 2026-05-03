import random
from Question import QUESTIONS

print("Welcome !")
print("        🎯 COMPUTER SCIENCE QUIZ")
print("=" * 40)
print("   1. 🎮 Play")
print("   2. 🏅 Leaderboard")
print("=" * 40)

score = 0
name=input("enter your name:")
random.shuffle(QUESTIONS)
for i, q in enumerate(QUESTIONS, start=1):
    print(f"\nQuestion {i} / 30 : {q['question']}")

    for choix in q["choix"]:
        print(choix)

    while True:
        user = input("Your answer : ")
        if user.upper() in ["A", "B", "C", "D"]:
            break                          # ✅ sort dès que valide
        print("⚠️ Invalid ! Enter A B C or D.")

    if user.upper() == q["reponse"]:
        print("Great ! ✅")
        score += 1
    else:
        print(f"Wrong ! ❌  →  {q['explication']}")

print(f"\nYour final score is : {score} / 30")

if score == 30:
    print(f"🎖️  Perfect ! You are a genius {name}!")
elif score >= 20:
    print(f"👏 Very good ! Keep it up {name}!")
elif score >= 10:
    print(f"📚 Keep practicing {name}!")
else:
    print(f"😅 Don't give up ! Try again {name} !")
