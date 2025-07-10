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
            "option": ["A)HTML", "B) Python", "C) CSS", "D) Excel"],
            "answer": "B"
        },
        {
            "question": "What does IDE stand for??",
            "option": ["A)  Internet Development Editor", "B) Integrated Development Environment", "C) Internal Debugging Extension", "D) Input Data Engine"],
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


def ask_user(q):
    ques_numb = 1
    score = 0
    print(f"Question{ques_numb}: {q["question"]}")

    for opt in q["option"]:
        print(opt)

    user_ans = input("Your answer: ").lower()
    if user_ans == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect❌")
        print(f"Correct answer: {q["option"]}")

    ques_numb += 1


def serial(quiz):
    random.shuffle(quiz)


if __name__ == "__main__":
    ask = input("Do you want play?(y/n): ").lower()
    if ask == "n":
        quit()

    print("Welcome to Computer Quiz!")
    print("Choose your Category:")
    print("1. Software Development\n2. Software Design & Architecture\n3. SDLC (Software Development Life Cycle")

    category = {1: "Software Development", 2: "Software Design & Architecture",
                3: "SDLC (Software Development Life Cycle)"}

    choice = int(input("Enter your choice: "))

    if choice in category:
        print(category[choice].upper())

        if choice == 1:
            software_development()
