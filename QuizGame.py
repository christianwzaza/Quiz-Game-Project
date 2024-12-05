def display_question(question):
    print("\n" + question["question"])
    for i, option in enumerate(question["options"], start=1):
        print(f"{i}. {option}")

def get_user_answer():
    try:
        answer = int(input("Your answer (1-4): "))
        if answer in range(1, 5):
            return answer
        else:
            print("Invalid option. Please enter a number between 1 and 4.")
            return get_user_answer()
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_user_answer()

def main():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
            "answer": 3
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": 2
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["CO2", "H2O", "O2", "NaCl"],
            "answer": 2
        }
    ]

    score = 0

    for question in questions:
        display_question(question)
        user_answer = get_user_answer()
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong. The correct answer was:", question["options"][question["answer"] - 1])

    print(f"\nYour total score is: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
