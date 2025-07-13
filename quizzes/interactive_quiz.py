"""
Interactive Python Quiz System
Run this script to take any of the quizzes interactively
"""

import json
import time
import re
import os

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
            if value:  # Only show non-empty options
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
        
        if self.total_questions > 0:
            print(f"Percentage: {(self.score/self.total_questions)*100:.1f}%")
            
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
        
        print(f"Time taken: {duration//60}:{duration%60:02d}")
        print(f"{'='*50}")

class QuizParser:
    """Parses markdown quiz files into question dictionaries"""
    
    @staticmethod
    def parse_quiz_file(file_path):
        """Parse a markdown quiz file and return list of questions"""
        if not os.path.exists(file_path):
            print(f"Error: Quiz file not found: {file_path}")
            return []
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        questions = []
        answer_key = QuizParser._extract_answer_key(content)
        
        # Split content into sections
        sections = content.split('###')
        
        for i, section in enumerate(sections[1:], 1):  # Skip first empty section
            if 'Answer Key' in section:
                break
                
            question_data = QuizParser._parse_question_section(section, i, answer_key)
            if question_data:
                questions.append(question_data)
        
        return questions
    

    @staticmethod
    def _extract_answer_key(content):
        """Extract answer key from markdown content"""
        answer_key = {}
        
        # Find answer key section
        answer_section_match = re.search(r'## Answer Key\s*(.*?)(?=##|$)', content, re.DOTALL)
        if answer_section_match:
            answer_section = answer_section_match.group(1)
            
            # Extract individual answers - handle multiple formats
            lines = answer_section.strip().split('\n')
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                    
                # Format: "8. b) explanation" 
                match1 = re.match(r'(\d+)\.\s*([a-d])\)', line, re.IGNORECASE)
                if match1:
                    question_num, answer = match1.groups()
                    answer_key[int(question_num)] = answer.lower()
                    continue
                
                # Format: "8. True" or "8. False" 
                match2 = re.match(r'(\d+)\.\s*(True|False)', line, re.IGNORECASE)
                if match2:
                    question_num, answer_text = match2.groups()
                    # Map True/False to a/b
                    answer_letter = 'a' if answer_text.lower() == 'true' else 'b'
                    answer_key[int(question_num)] = answer_letter
                    continue
                    
                # Format: "8. False (explanation)"
                match3 = re.match(r'(\d+)\.\s*(True|False)\s*\(', line, re.IGNORECASE)
                if match3:
                    question_num, answer_text = match3.groups()
                    # Map True/False to a/b
                    answer_letter = 'a' if answer_text.lower() == 'true' else 'b'
                    answer_key[int(question_num)] = answer_letter
                    continue
        
        return answer_key
    

    @staticmethod
    def _parse_question_section(section, question_num, answer_key):
        """Parse individual question section"""
        lines = section.strip().split('\n')
        
        if not lines:
            return None
        
        # Extract question text (can be multiple lines)
        question_lines = []
        option_start = None
        
        # Find where options start
        for i, line in enumerate(lines):
            line_stripped = line.strip()
            
            # Stop if we hit a section header (##)
            if line_stripped.startswith('##'):
                break
                
            if line_stripped.startswith(('a)', 'b)', 'c)', 'd)')) or re.match(r'^[a-d]\)\s', line_stripped):
                option_start = i
                break
            question_lines.append(line)
        
        # Join all question lines
        question_text = '\n'.join(question_lines).strip()
        
        # Remove question number if present
        if question_text.startswith(f'{question_num}.'):
            question_text = question_text[len(f'{question_num}.'):].strip()
        
        # Clean up markdown artifacts
        question_text = re.sub(r'^#{1,6}\s*', '', question_text, flags=re.MULTILINE)  # Remove headers
        question_text = re.sub(r'```python\s*\n', '', question_text)  # Remove ```python
        question_text = re.sub(r'```\s*\n', '', question_text)       # Remove closing ```
        question_text = re.sub(r'```', '', question_text)            # Remove any remaining ```
        question_text = question_text.strip()
        
        # Extract options
        options = {'a': '', 'b': '', 'c': '', 'd': ''}
        
        if option_start is not None:
            for line in lines[option_start:]:
                line = line.strip()
                
                # Stop if we hit a section header
                if line.startswith('##'):
                    break
                    
                if line.startswith(('a)', 'b)', 'c)', 'd)')):
                    option_letter = line[0].lower()
                    option_text = line[2:].strip()
                    options[option_letter] = option_text
                elif re.match(r'^[a-d]\)\s', line):
                    option_letter = line[0].lower()
                    option_text = line[2:].strip()
                    options[option_letter] = option_text
        
        # Get correct answer
        correct_answer = answer_key.get(question_num, 'a')
        
        return {
            'question': question_text,
            'options': options,
            'answer': correct_answer
        }


def run_quiz_from_file(file_path, quiz_name):
    """Run a quiz from a markdown file"""
    questions = QuizParser.parse_quiz_file(file_path)
    
    if not questions:
        print(f"No questions found in {file_path}")
        return
    
    quiz = PythonQuiz()
    quiz.start_quiz(quiz_name)
    
    for q in questions:
        if not quiz.ask_question(q["question"], q["options"], q["answer"]):
            break
    
    quiz.end_quiz()


def section1_quiz():
    file_path = "quizzes/Section1_Basic_Syntax_Quiz.md"  
    run_quiz_from_file(file_path, "Section 1: Basic Syntax Quiz")


def section2_quiz():
    file_path = "quizzes/Section2_Data_Structures_Quiz.md"  
    run_quiz_from_file(file_path, "Section 2: Data Structures Quiz")


def section3_quiz():
    file_path = "quizzes/Section3_Flow_Control_Quiz.md"  
    run_quiz_from_file(file_path, "Section 3: Flow Control Quiz")


def section4_quiz():
    file_path = "quizzes/Section4_Functions_Quiz.md"  
    run_quiz_from_file(file_path, "Section 4: Functions Quiz")


def section5_quiz():
    file_path = "quizzes/Section5_OOP_Quiz.md"  
    run_quiz_from_file(file_path, "Section 5: OOP Quiz")


def section6_quiz():
    file_path = "quizzes/Section6_Modules_Libraries_Quiz.md"  
    run_quiz_from_file(file_path, "Section 6: Modules and Libraries Quiz")


def final_quiz():
    file_path = "quizzes/Final_Comprehensive_Quiz.md"  
    run_quiz_from_file(file_path, "Final Comprehensive Quiz")


if __name__ == "__main__":
    print("🐍 Python A-to-Z Quiz System 🐍")
    print("="*40)
    print("1. Section 1: Basic Syntax")
    print("2. Section 2: Data Structures") 
    print("3. Section 3: Flow Control")
    print("4. Section 4: Functions")
    print("5. Section 5: OOP")
    print("6. Section 6: Modules")
    print("7. Final Comprehensive Quiz")
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