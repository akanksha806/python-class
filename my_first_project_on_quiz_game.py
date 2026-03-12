## Quiz game using Python basics
questions = ["Python kis type ki language hai?",
             "List mutable hoti hai ya immutable?",
             "Python mein input lene ke liye kaunsa function use hota hai?",
             "Kya Python case sensitive language hai?"]

answers = ["interpreted",
           "mutable",
            "input",
            "yes"]

marks = 0
que_count = 0

while que_count < len(questions):
    print(questions[que_count])
    user_answer = input("Answer: ").strip().lower()

    if user_answer == answers[que_count]:
        print("Right answer\n")
        marks = marks + 1
    else:
        print("Wrong answer\n")

    que_count = que_count + 1

print("Your total marks is:", marks)
