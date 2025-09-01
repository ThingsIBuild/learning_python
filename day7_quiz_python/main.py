# Quiz Application in Python

def run_quiz(questions):
    score = 0
    for question, options, correct in questions:
        print("\n" + question)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        
        try:
            answer = int(input("Enter your answer (1-4): "))
            if options[answer - 1].lower() == correct.lower():
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {correct}")
        except (ValueError, IndexError):
            print("⚠️ Invalid input. Skipping question.")
    
    print(f"\nYour final score: {score}/{len(questions)}")

# Questions: (question, options, correct answer)
quiz_questions = [
    ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris"),
    ("Which language is used for web apps?", ["Python", "HTML", "C++", "Java"], "HTML"),
    ("Who developed Python?", ["Guido van Rossum", "Elon Musk", "Mark Zuckerberg", "Dennis Ritchie"], "Guido van Rossum"),
]

run_quiz(quiz_questions)
