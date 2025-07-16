import random


def software_development():
    quiz = [
        {
            "question": "What is the full form of OOP?",
            "option": ["A) Object-Oriented Programming", "B) Operational Output Processing", "C) Object-Origin Principle", "D) Oriented Object Processor"],
            "answer": "A"
        },
        {
            "question": "Which language is commonly used for backend web development??",
            "option": ["A) HTML", "B) Python", "C) CSS", "D) Excel"],
            "answer": "B"
        },
        {
            "question": "What does IDE stand for??",
            "option": ["A) Internet Development Editor", "B) Integrated Development Environment", "C) Internal Debugging Extension", "D) Input Data Engine"],
            "answer": "B"
        },
        {
            "question": "Why is Git used in software development?",
            "option": ["A) To design user interfaces", "B) To run the application", "C) To track and manage code changes", "D) To test programs"],
            "answer": "C"
        },
        {
            "question": "Which software model is based on short, iterative cycles?",
            "option": ["A) Waterfall Model", "B) Spiral Model", "C) V-Model", "D) Agile Model"],
            "answer": "D"
        },
    ]
    serial(quiz)
    ask_user(quiz)


def Software_Design_Architecture():
    quiz = [
        {
            "question": "What is the purpose of UML diagrams?",
            "option": ["A) To test the program", "B) To write code", "C) To document project cost", "D) To visually represent software design"],
            "answer": "D"
        },
        {
            "question": "MVC stands for:",
            "option": ["A) Model-View-Controller", "B) Main-Version-Code", "C) Machine-Visual-ComponentS", "D) Model-Version-Component"],
            "answer": "A"
        },
        {
            "question": "Which design pattern ensures only one instance of a class?",
            "option": ["A) Factory Pattern", "B) Adapter Pattern", "C) Singleton Pattern", "D) Observer Pattern"],
            "answer": "C"
        },
        {
            "question": "What is a module in programming?",
            "option": ["A) A part of hardware", "B) A reusable piece of code", "C) A bug", "D) A test tool"],
            "answer": "B"
        },
        {
            "question": "Main benefit of modular programming is:",
            "option": ["A) Increased code length", "B) Less testing", "C) Improved maintainability and reuse", "D) Faster typing"],
            "answer": "C"
        },
    ]
    serial(quiz)
    ask_user(quiz)


def SDLC():
    quiz = [
        {
            "question": "What is the first phase of SDLC?",
            "option": ["A) Coding", "B) Deployment", "C) Requirement Analysis", "D) Maintenance"],
            "answer": "C"
        },
        {
            "question": "SDLC stands for:",
            "option": ["A) Software Debugging and Logic Cycler", "B) Structured Design Life Code", "C) Software Development Life Cycle", "D) System Development Long Cycle"],
            "answer": "C"
        },
        {
            "question": "Which SDLC model is strictly linear?",
            "option": ["A) Agile", "B) Waterfall", "C) Spiral", "D) V-model"],
            "answer": "B"
        },
        {
            "question": "In Agile, a short development period is called a:",
            "option": ["A) Loop", "B) Break", "C) Sprint", "D) Stage"],
            "answer": "C"
        },
        {
            "question": "Which phase comes after implementation?",
            "option": ["A) Deployment", "B) Testing", "C) Planning", "D) Maintenance"],
            "answer": "B"
        },
    ]
    serial(quiz)
    ask_user(quiz)


# user input function
def ask_user(quiz):
    score = 0
    '''i: the question number starting from 1 (because of start=1)
        q: the actual question dictionary (e.g., q["question"], q["option"], etc.'''
    for i, q in enumerate(quiz, start=1):
        print(f"Question{i}: {q["question"]}")

        for opt in q["option"]:
            print(opt)

        user_ans = input("Your answer: ").upper()
        if user_ans == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect❌")
            print(f"Correct answer: {q["answer"]}\n")

    print(f"Your final score: {score}/{len(quiz)}")


# suffle serial function
def serial(quiz):
    random.shuffle(quiz)


# user function
def user():
    print("\nWelcome to Computer Quiz!")
    print("\nChoose your Category:")
    print("1. Software Development\n2. Software Design & Architecture\n3. SDLC (Software Development Life Cycle")

    category = {1: "Software Development", 2: "Software Design & Architecture",
                3: "SDLC (Software Development Life Cycle)"}

    choice = int(input("\nEnter your choice: "))

    if choice in category:
        print(f"\n{category[choice].upper()}")

        if choice == 1:
            software_development()
        elif choice == 2:
            Software_Design_Architecture()
        else:
            SDLC()


# main function
if __name__ == "__main__":
    while True:  # ask user again & again
        ask = input("Do you want play?(y/n): ").lower()
        if ask == "n":
            quit()
        user()

        again = input("Want to try again?[y/n]: ").lower()
        if again == "n":
            print("Thanks for playing!")
            quit()
        else:
            user()
