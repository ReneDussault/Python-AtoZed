import time
import json
import os
import random

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
        print("- For True/False questions, type 'a' for True and 'b' for False")
        print("- Type 'quit' to exit at any time")
        print("- Good luck!\n")
        
        self.start_time = time.time()
        
    def ask_question(self, question_data):
        self.total_questions += 1
        print(f"Question {self.total_questions}:")
        
        # Display question text
        print(question_data["question"])
        
        # Display code if present
        if question_data.get("code"):
            code_display = question_data["code"].replace("\\n", "\n")
            print(code_display)
        
        print()
        
        # Display options
        for key, value in question_data["options"].items():
            if value:  # Only show non-empty options
                print(f"{key}) {value}")
        
        while True:
            answer = input("\nYour answer: ").lower().strip()
            
            if answer in ["quit", "exit"]:
                return False
                
            if answer in ["a", "b", "c", "d"]:
                correct_answer = question_data["correct_answer"].lower()
                if answer == correct_answer:
                    print("✅ Correct!")
                    self.score += 1
                else:
                    print(f"❌ Incorrect. The correct answer is {question_data['correct_answer'].upper()}")
                    print(f"Explanation: {question_data['explanation']}")
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
        
        if self.total_questions > 0:
            percentage = (self.score/self.total_questions)*100
            print(f"Percentage: {percentage:.1f}%")
            
            if percentage >= 100:
                grade = "A++ - Perfect Score!"
            elif percentage >= 95:
                grade = "A+ - Outstanding!"
            elif percentage >= 90:
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
        
        print(f"Time taken: {duration//60}:{duration%60:02d}")
        print(f"{'='*50}")


class JSONQuizLoader:
    @staticmethod
    def load_quiz_from_json(file_path):
        """Load quiz data from JSON file"""
        if not os.path.exists(file_path):
            print(f"Error: Quiz file not found: {file_path}")
            return None
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                quiz_data = json.load(file)
            return quiz_data
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON file: {e}")
            return None
        except Exception as e:
            print(f"Error loading quiz file: {e}")
            return None
    
    @staticmethod
    def extract_questions(quiz_data):
        """Extract all questions from quiz data"""
        all_questions = []
        
        if not quiz_data or 'sections' not in quiz_data:
            return all_questions
        
        for section in quiz_data['sections']:
            if 'questions' in section:
                all_questions.extend(section['questions'])
        
        return all_questions
    
    @staticmethod
    def select_questions(all_questions, num_questions, mode="random"):
        """Select a subset of questions based on mode"""
        if not all_questions:
            return []
        
        if num_questions >= len(all_questions):
            return all_questions
        
        if mode == "random":
            return random.sample(all_questions, num_questions)
        elif mode == "first":
            return all_questions[:num_questions]
        else:
            return all_questions[:num_questions]


def run_json_quiz(file_path, quiz_name, num_questions=None, mode="random"):
    """Run quiz from JSON file with specified number of questions"""
    
    # Load quiz data
    quiz_data = JSONQuizLoader.load_quiz_from_json(file_path)
    if not quiz_data:
        return
    
    # Extract all questions
    all_questions = JSONQuizLoader.extract_questions(quiz_data)
    if not all_questions:
        print("No questions found in the quiz file.")
        return
    
    # Select questions based on mode
    if num_questions:
        selected_questions = JSONQuizLoader.select_questions(all_questions, num_questions, mode)
        actual_quiz_name = f"{quiz_name} ({len(selected_questions)} Questions)"
    else:
        selected_questions = all_questions
        actual_quiz_name = f"{quiz_name} (Complete - {len(selected_questions)} Questions)"
    
    # Run the quiz
    quiz = PythonQuiz()
    quiz.start_quiz(actual_quiz_name)
    
    for question_data in selected_questions:
        if not quiz.ask_question(question_data):
            break
    
    quiz.end_quiz()


def section1_quiz():
    """Section 1: Basic Syntax Quiz with different modes"""
    file_path = "quizzes/section1_basic_syntax_quiz.json"
    base_name = "Section 1: Basic Syntax Quiz"
    
    print(f"\n🎯 {base_name}")
    print("="*50)
    print("Choose your quiz mode:")
    print("1. Flash Quiz (5 questions) - Quick review")
    print("2. Practice Quiz (10 questions) - Focused practice") 
    print("3. Standard Quiz (20 questions) - Comprehensive review")
    print("4. In-Depth Quiz (All 30 questions) - Complete assessment")
    print("="*50)
    
    choice = input("Select mode (1-4): ").strip()
    
    quiz_modes = {
        "1": (5, "Flash Quiz"),
        "2": (10, "Practice Quiz"),
        "3": (20, "Standard Quiz"),
        "4": (None, "In-Depth Quiz")  # None means all questions
    }
    
    if choice in quiz_modes:
        num_questions, mode_name = quiz_modes[choice]
        quiz_name = f"{base_name} - {mode_name}"
        run_json_quiz(file_path, quiz_name, num_questions, "random")
    else:
        print("❌ Invalid choice! Please select 1-4.")


def section2_quiz():
    file_path = "quizzes/section2_data_structures_quiz.json"  
    base_name = "Section 2: Data Structures Quiz"
    
    print(f"\n🎯 {base_name}")
    print("="*50)
    print("Choose your quiz mode:")
    print("1. Flash Quiz (5 questions) - Quick review")
    print("2. Practice Quiz (10 questions) - Focused practice") 
    print("3. Standard Quiz (20 questions) - Comprehensive review")
    print("4. In-Depth Quiz (All 30 questions) - Complete assessment")
    print("="*50)
    
    choice = input("Select mode (1-4): ").strip()
    
    quiz_modes = {
        "1": (5, "Flash Quiz"),
        "2": (10, "Practice Quiz"),
        "3": (20, "Standard Quiz"),
        "4": (None, "In-Depth Quiz")  # None means all questions
    }
    
    if choice in quiz_modes:
        num_questions, mode_name = quiz_modes[choice]
        quiz_name = f"{base_name} - {mode_name}"
        run_json_quiz(file_path, quiz_name, num_questions, "random")
    else:
        print("❌ Invalid choice! Please select 1-4.")


def section3_quiz():
    file_path = "quizzes/Section3_Flow_Control_Quiz.md"  
    print("📝 Section 3 quiz coming soon! (Will use MD format for now)")


def section4_quiz():
    file_path = "quizzes/Section4_Functions_Quiz.md"  
    print("📝 Section 4 quiz coming soon! (Will use MD format for now)")


def section5_quiz():
    file_path = "quizzes/Section5_OOP_Quiz.md"  
    print("📝 Section 5 quiz coming soon! (Will use MD format for now)")


def section6_quiz():
    file_path = "quizzes/Section6_Modules_Libraries_Quiz.md"  
    print("📝 Section 6 quiz coming soon! (Will use MD format for now)")


def final_quiz():
    file_path = "quizzes/Final_Comprehensive_Quiz.md"  
    print("📝 Final quiz coming soon! (Will use MD format for now)")


if __name__ == "__main__":
    print()
    print()
    print()
    print("Welcome to the Python A-to-Z Interactive Quiz System!")
    print("🐍 Python A-to-Z Quiz System 🐍")
    print("="*40)
    print("1. Section 1: Basic Syntax (JSON)")
    print("2. Section 2: Data Structures (JSON)") 
    print("3. Section 3: Flow Control (Coming Soon)")
    print("4. Section 4: Functions (Coming Soon)")
    print("5. Section 5: OOP (Coming Soon)")
    print("6. Section 6: Modules (Coming Soon)")
    print("7. Final Comprehensive Quiz (Coming Soon)")
    print("="*40)
    
    choice = input("Choose a quiz (1-7): ").strip()
    
    quiz_functions = {
        "1": section1_quiz,
        "2": section2_quiz,
        "3": section3_quiz,
        "4": section4_quiz,
        "5": section5_quiz,
        "6": section6_quiz,
        "7": final_quiz
    }
    
    if choice in quiz_functions:
        quiz_functions[choice]()
    else:
        print("❌ Invalid choice! Please select 1-7.")