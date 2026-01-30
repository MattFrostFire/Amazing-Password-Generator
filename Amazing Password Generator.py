import random
import string
import os
from datetime import datetime

class PasswordGenerator:
    def __init__(self, filename='top_english_nouns_lower_100000.txt'):
        # Get the folder where this script is actually saved
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        
        # Create directories inside that same folder
        self.memorable_dir = os.path.join(self.base_path, "Memorable")
        self.random_dir = os.path.join(self.base_path, "Random")
        os.makedirs(self.memorable_dir, exist_ok=True)
        os.makedirs(self.random_dir, exist_ok=True)
        
        self.word_list = []
        full_word_path = os.path.join(self.base_path, filename)
        try:
            with open(full_word_path, 'r') as f:
                self.word_list = [line.strip() for line in f.readlines() if line.strip()]
            print(f"Loaded {len(self.word_list)} words from: {full_word_path}")
        except FileNotFoundError:
            print(f"ERROR: {filename} not found at {full_word_path}")

    def log_password(self, password, p_type):
        """Saves password and timestamp to the specific directory file"""
        # Select the correct directory path
        folder_path = self.memorable_dir if p_type == "memorable" else self.random_dir
        file_path = os.path.join(folder_path, "Generated_Passwords.txt")
        
        # Format: Day, Date, and Time
        timestamp = datetime.now().strftime("%A, %B %d, %Y %I:%M:%S %p")
        
        with open(file_path, "a") as f:
            f.write(f"Password: {password} | Created: {timestamp}\n")

    def generate_memorable(self, num_words=3, case="lower"):
        """Selecting n words + 1-digit number each + hyphenated"""
        if not self.word_list: return "Error"
        selected = random.choices(self.word_list, k=num_words)
        
        parts = []
        for word in selected:
            if case == "upper": word = word.upper()
            elif case == "title": word = word.capitalize()
            parts.append(f"{word}{random.randint(0, 9)}")
            
        password = "-".join(parts)
        self.log_password(password, "memorable")
        return password

    def generate_random(self, length=12, include_punctuation=True, exclude_chars=""):
        """Selecting n characters from mixed types"""
        pool = string.ascii_letters + string.digits
        if include_punctuation: pool += string.punctuation
        pool = "".join([c for c in pool if c not in exclude_chars])
        
        password = "".join(random.choices(pool, k=length))
        self.log_password(password, "random")
        return password

def run_simulation():
    """Confirm functionality by generating 1000 random/memorable passwords"""
    gen = PasswordGenerator()
    if not gen.word_list:
        print("Simulation aborted: Word list is empty or missing.")
        return

    print("Generating 1000 passwords...")
    for _ in range(1000):
        choice = random.choice(["memorable", "random"])
        if choice == "memorable":
            gen.generate_memorable(num_words=random.randint(2, 4))
        else:
            gen.generate_random(length=random.randint(12, 20))
    print("Done! Check your 'Memorable' and 'Random' folders for Generated_Passwords.txt.")

if __name__ == "__main__":
    run_simulation()