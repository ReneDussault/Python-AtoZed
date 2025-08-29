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
        
        # Handle both old and new option formats
        options = question_data["options"]
        if isinstance(options, dict):
            # Old format: {"a": "option1", "b": "option2", ...}
            for key, value in options.items():
                if value:  # Only show non-empty options
                    print(f"{key}) {value}")
        elif isinstance(options, list):
            # New format: ["option1", "option2", "option3", "option4"]
            option_keys = ['a', 'b', 'c', 'd']
            for i, option in enumerate(options):
                if i < len(option_keys) and option:
                    print(f"{option_keys[i]}) {option}")
        
        while True:
            answer = input("\nYour answer: ").lower().strip()
            
            if answer in ["quit", "exit"]:
                return False
                
            if answer in ["a", "b", "c", "d"]:
                correct_answer = question_data["correct_answer"]
                
                # Handle both string and integer correct answers
                if isinstance(correct_answer, str):
                    correct_answer_key = correct_answer.lower()
                elif isinstance(correct_answer, int):
                    # Convert 0-based index to letter (0->a, 1->b, etc.)
                    option_keys = ['a', 'b', 'c', 'd']
                    correct_answer_key = option_keys[correct_answer] if correct_answer < len(option_keys) else 'a'
                else:
                    correct_answer_key = 'a'  # fallback
                
                if answer == correct_answer_key:
                    print("✅ Correct!")
                    self.score += 1
                else:
                    print(f"❌ Incorrect. The correct answer is {correct_answer_key.upper()}")
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
        """Extract all questions from quiz data - handles both old and new JSON formats"""
        all_questions = []
        
        if not quiz_data:
            return all_questions
        
        # New format: direct questions array
        if 'questions' in quiz_data:
            return quiz_data['questions']
        
        # Old format: sections with nested questions
        if 'sections' in quiz_data:
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


def create_quiz_mode_selector(section_name, file_path, total_questions=30):
    """Generic quiz mode selector for quiz.JSON"""
    print(f"\n🎯 {section_name}")
    print("="*50)
    print("Choose your quiz mode:")
    print("1. Flash Quiz (5 questions) - Quick review")
    print("2. Practice Quiz (10 questions) - Focused practice") 
    print("3. Standard Quiz (15 questions) - Balanced review")
    print(f"4. In-Depth Quiz (All {total_questions} questions) - Complete assessment")
    print("="*50)
    
    choice = input("Select mode (1-4): ").strip()
    
    quiz_modes = {
        "1": (5, "Flash Quiz"),
        "2": (10, "Practice Quiz"),
        "3": (15, "Standard Quiz"),
        "4": (None, "In-Depth Quiz")  # None means all questions
    }
    
    if choice in quiz_modes:
        num_questions, mode_name = quiz_modes[choice]
        quiz_name = f"{section_name} - {mode_name}"
        run_json_quiz(file_path, quiz_name, num_questions, "random")
    else:
        print("❌ Invalid choice! Please select 1-4.")


def section1_quiz():
    """Section 1: Basic Syntax Quiz"""
    file_path = "./section1_basic_syntax_quiz.json"
    section_name = "Section 1: Basic Syntax Quiz"
    create_quiz_mode_selector(section_name, file_path, 30)


def section2_quiz():
    """Section 2: Data Structures Quiz"""
    file_path = "./section2_data_structures_quiz.json"  
    section_name = "Section 2: Data Structures Quiz"
    create_quiz_mode_selector(section_name, file_path, 30)


def section3_quiz():
    """Section 3: Flow Control Quiz"""
    file_path = "./section3_flow_control_quiz.json"  
    section_name = "Section 3: Flow Control Quiz"
    create_quiz_mode_selector(section_name, file_path, 30)


def section4_quiz():
    """Section 4: Functions Quiz"""
    file_path = "./section4_functions_quiz.json"  
    section_name = "Section 4: Functions Quiz"
    create_quiz_mode_selector(section_name, file_path, 30)


def section5_quiz():
    """Section 5: OOP Quiz"""
    file_path = "./section5_oop_quiz.json"  
    section_name = "Section 5: Object-Oriented Programming Quiz"
    create_quiz_mode_selector(section_name, file_path, 30)


def section6_quiz():
    """Section 6: Modules & Libraries Quiz"""
    file_path = "./section6_modules_libraries_quiz.json"  
    print("📝 Section 6 quiz coming soon! (Converting to JSON format)")


def final_quiz():
    """Final Comprehensive Quiz"""
    file_path = "./final_comprehensive_quiz.json"  
    print("📝 Final quiz coming soon! (Converting to JSON format)")


if __name__ == "__main__":
    print()
    print()
    print()
    print("Welcome to the Python A-to-Z Interactive Quiz System!")
    print("🐍 Python A-to-Z Quiz System 🐍")
    print("="*40)
    print("1. Section 1: Basic Syntax (JSON)")
    print("2. Section 2: Data Structures (JSON)") 
    print("3. Section 3: Flow Control (JSON)")
    print("4. Section 4: Functions (JSON)")
    print("5. Section 5: OOP (JSON)")
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