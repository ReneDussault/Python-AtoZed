"""
Interactive Python Quiz System
Run this script to take any of the quizzes interactively
"""

import json
import time

class PythonQuiz:
    def __init__(self):
        self.score = 0
        self.total_questions = 0
        self.start_time = None
        
    def start_quiz(self, quiz_name):
        print(f"\n{'='*50}")
        print(f"Welcome to {quiz_name}")
        print(f"{'='*50}")
        print("Instructions:")
        print("- Answer each question by typing a, b, c, or d")
        print("- Type 'quit' to exit at any time")
        print("- Good luck!\n")
        
        self.start_time = time.time()
        
    def ask_question(self, question, options, correct_answer):
        self.total_questions += 1
        print(f"Question {self.total_questions}:")
        print(question)
        print()
        
        for key, value in options.items():
            print(f"{key}) {value}")
        
        while True:
            answer = input("\nYour answer: ").lower().strip()
            
            if answer == 'quit':
                return False
                
            if answer in ['a', 'b', 'c', 'd']:
                if answer == correct_answer.lower():
                    print("✅ Correct!")
                    self.score += 1
                else:
                    print(f"❌ Incorrect. The correct answer is {correct_answer.upper()}")
                print()
                return True
            else:
                print("Please enter a, b, c, d, or 'quit'")
    
    def end_quiz(self):
        end_time = time.time()

        if self.start_time is None:
            print("Error: Quiz was not properly started!")
            return

        duration = int(end_time - self.start_time)
        
        print(f"\n{'='*50}")
        print("QUIZ COMPLETED!")
        print(f"{'='*50}")
        print(f"Score: {self.score}/{self.total_questions}")
        print(f"Percentage: {(self.score/self.total_questions)*100:.1f}%")
        print(f"Time taken: {duration//60}:{duration%60:02d}")
        
        # Grade assignment
        percentage = (self.score/self.total_questions)*100
        if percentage >= 90:
            grade = "A - Excellent!"
        elif percentage >= 80:
            grade = "B - Good!"
        elif percentage >= 70:
            grade = "C - Satisfactory"
        elif percentage >= 60:
            grade = "D - Needs Improvement"
        else:
            grade = "F - Needs Significant Review"
            
        print(f"Grade: {grade}")
        print(f"{'='*50}")

# Example usage for Section 1 Quiz
def section1_quiz():
    quiz = PythonQuiz()
    quiz.start_quiz("Section 1: Basic Syntax Quiz")
    
    questions = [
        {
            "question": "Which of the following is the correct way to create a comment in Python?",
            "options": {
                "a": "// This is a comment",
                "b": "# This is a comment", 
                "c": "/* This is a comment */",
                "d": "<!-- This is a comment -->"
            },
            "answer": "b"
        },
        {
            "question": "What will be the output of: print(10 // 3)?",
            "options": {
                "a": "3.33",
                "b": "3.0",
                "c": "3",
                "d": "4"
            },
            "answer": "c"
        }
        # Add more questions here
    ]
    
    for q in questions:
        if not quiz.ask_question(q["question"], q["options"], q["answer"]):
            break
    
    quiz.end_quiz()

if __name__ == "__main__":
    print("Python A-to-Z Quiz System")
    print("1. Section 1: Basic Syntax")
    print("2. Section 2: Data Structures") 
    print("3. Section 3: Flow Control")
    print("4. Section 4: Functions")
    print("5. Section 5: OOP")
    print("6. Section 6: Modules")
    print("7. Final Comprehensive Quiz")
    
    choice = input("Choose a quiz (1-7): ")
    
    if choice == "1":
        section1_quiz()
    # Add other quiz functions here
    else:
        print("Invalid choice!")