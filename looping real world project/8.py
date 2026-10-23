questions = [
    "1. Which language are we learning?\nA. Java\nB. Python\nC. C++",
    "2. Which function displays output in Python?\nA. print()\nB. input()\nC. scan()",
    "3. Which symbol is used for comments in Python?\nA. //\nB. #\nC. /* */",
    "4. Which loop is used to repeat a task?\nA. for\nB. print\nC. int",
    "5. Which data type stores True or False?\nA. int\nB. str\nC. bool"
]

answers = ["B", "A", "B", "A", "C"]
score = 0

for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Enter your answer (A/B/C): ").upper()

    if user_answer == answers[i]:
        print("Correct answer!")
        score = score + 1
    else:
        print("Wrong answer!")

percentage = (score / len(questions)) * 100

print("\n--- Quiz Result ---")
print("Score:", score, "/", len(questions))
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Excellent!")
elif percentage >= 60:
    print("Good!")
else:
    print("Keep Practicing!")