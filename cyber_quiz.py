import tkinter as tk
from tkinter import messagebox

# Sample Questions and Answers
questions = [
    {
        "question": "What does 'phishing' typically involve?",
        "options": ["Hacking into a network", "Sending deceptive emails to steal data", "Physically stealing a device", "None of these"],
        "answer": "Sending deceptive emails to steal data"
    },
    {
        "question": "A strong password should include:",
        "options": ["Your birthdate", "Simple numbers", "Upper, lower case, numbers & symbols", "Just your name"],
        "answer": "Upper, lower case, numbers & symbols"
    },
    {
        "question": "Which is a safe practice online?",
        "options": ["Click unknown links", "Ignore software updates", "Use same password everywhere", "Use 2FA (Two Factor Authentication)"],
        "answer": "Use 2FA (Two Factor Authentication)"
    },
    {
        "question": "What is malware?",
        "options": ["Software that protects your PC", "An app store", "A malicious software", "None of these"],
        "answer": "A malicious software"
    },
    {
        "question": "Which of the following is a social engineering attack?",
        "options": ["Firewall breach", "Antivirus scan", "Phishing email", "Malware injection"],
        "answer": "Phishing email"
    }
]

# ------------------- QUIZ APP -------------------
class QuizApp:
    def __init__(self, root, user_data):
        self.root = root
        self.root.title("Cyber Security Awareness Quiz")
        self.root.geometry("800x600")
        self.root.config(bg="#f0f8ff")
        self.user_data = user_data

        self.q_index = 0
        self.score = 0
        self.selected_option = tk.StringVar()

        self.title_label = tk.Label(root, text="Cyber Security Awareness Quiz", font=("Helvetica", 24, "bold"), bg="#f0f8ff", fg="#002855")
        self.title_label.pack(pady=20)

        self.question_label = tk.Label(root, text="", font=("Arial", 18, "bold"), wraplength=700, justify="center", bg="#f0f8ff")
        self.question_label.pack(pady=20)

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.selected_option, value="", font=("Arial", 14), bg="#f0f8ff", anchor="w", width=60, justify="left")
            rb.pack(pady=5, anchor="w", padx=150)
            self.radio_buttons.append(rb)

        self.submit_btn = tk.Button(root, text="Submit", command=self.check_answer, font=("Arial", 14, "bold"), bg="#002855", fg="white", width=15)
        self.submit_btn.pack(pady=20)

        self.status_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f8ff")
        self.status_label.pack(pady=10)

        self.load_question()

    def load_question(self):
        self.selected_option.set(None)
        q = questions[self.q_index]
        self.question_label.config(text=f"Q{self.q_index + 1}: {q['question']}")
        for i, option in enumerate(q["options"]):
            self.radio_buttons[i].config(text=option, value=option)

    def check_answer(self):
        selected = self.selected_option.get()
        if selected == "":
            messagebox.showwarning("No option selected", "Please select an answer before submitting.")
            return

        correct = questions[self.q_index]["answer"]
        if selected == correct:
            self.score += 1
            self.status_label.config(text="Correct!", fg="green")
        else:
            self.status_label.config(text=f"Wrong! Correct answer was: {correct}", fg="red")

        self.q_index += 1
        if self.q_index >= len(questions):
            self.show_result()
        else:
            self.root.after(1000, self.load_question)

    def show_result(self):
        msg = f"🎉 Quiz Completed!\n\nLeaderboard:\nName: {self.user_data['name']}\nEmail: {self.user_data['email']}\nScore: {self.score} / {len(questions)}"
        messagebox.showinfo("Quiz Completed", msg)
        self.root.destroy()

# ------------------- REGISTRATION PAGE -------------------
def show_registration():
    reg_window = tk.Tk()
    reg_window.title("Register for Cyber Quiz")
    reg_window.geometry("400x500")
    reg_window.config(bg="#e6f2ff")

    def start_quiz():
        name = entry_name.get()
        email = entry_email.get()
        contact = entry_contact.get()
        age = entry_age.get()
        gender = gender_var.get()

        if not name or not email or not contact or not age or not gender:
            messagebox.showerror("Incomplete Form", "Please fill in all fields.")
            return

        user_data = {
            "name": name,
            "email": email,
            "contact": contact,
            "age": age,
            "gender": gender
        }

        reg_window.destroy()
        root = tk.Tk()
        app = QuizApp(root, user_data)
        root.mainloop()

    tk.Label(reg_window, text="Cyber Awareness Quiz", font=("Arial", 20, "bold"), bg="#e6f2ff", fg="#003366").pack(pady=20)
    tk.Label(reg_window, text="Enter your details below:", font=("Arial", 14), bg="#e6f2ff").pack(pady=10)

    tk.Label(reg_window, text="Name:", font=("Arial", 12), bg="#e6f2ff").pack(anchor="w", padx=50)
    entry_name = tk.Entry(reg_window, font=("Arial", 12), width=30)
    entry_name.pack(pady=5)

    tk.Label(reg_window, text="Email:", font=("Arial", 12), bg="#e6f2ff").pack(anchor="w", padx=50)
    entry_email = tk.Entry(reg_window, font=("Arial", 12), width=30)
    entry_email.pack(pady=5)

    tk.Label(reg_window, text="Contact Number:", font=("Arial", 12), bg="#e6f2ff").pack(anchor="w", padx=50)
    entry_contact = tk.Entry(reg_window, font=("Arial", 12), width=30)
    entry_contact.pack(pady=5)

    tk.Label(reg_window, text="Age:", font=("Arial", 12), bg="#e6f2ff").pack(anchor="w", padx=50)
    entry_age = tk.Entry(reg_window, font=("Arial", 12), width=30)
    entry_age.pack(pady=5)

    tk.Label(reg_window, text="Gender:", font=("Arial", 12), bg="#e6f2ff").pack(anchor="w", padx=50)
    gender_var = tk.StringVar()
    tk.Radiobutton(reg_window, text="Male", variable=gender_var, value="Male", bg="#e6f2ff").pack(anchor="w", padx=60)
    tk.Radiobutton(reg_window, text="Female", variable=gender_var, value="Female", bg="#e6f2ff").pack(anchor="w", padx=60)
    tk.Radiobutton(reg_window, text="Other", variable=gender_var, value="Other", bg="#e6f2ff").pack(anchor="w", padx=60)

    tk.Button(reg_window, text="Start Quiz", command=start_quiz, font=("Arial", 12, "bold"), bg="#003366", fg="white", width=20).pack(pady=20)

    reg_window.mainloop()

# ------------------- MAIN -------------------
if __name__ == "__main__":
    show_registration()
