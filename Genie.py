import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import time

# Sample Data (replace with actual data)
data = pd.DataFrame({
    'text': [
        'How do I reset my password?',
        'Can you explain your return policy?',
        'How do I track my order?',
        'I want to cancel my subscription',
    ],
    'label': ['password', 'return_policy', 'order_tracking', 'subscription']
})

# Preprocessing
data['text'] = data['text'].str.lower()
X = data['text']
y = data['label']

# Feature Extraction
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Model Training
model = MultinomialNB()
model.fit(X_train, y_train)

# Response Function
def get_response(query):
    query_vectorized = vectorizer.transform([query.lower()])
    prediction = model.predict(query_vectorized)
    responses = {
        'password': "Reset your password via the settings page or contact support for help.",
        'return_policy': "Our return policy allows returns within 30 days of purchase.",
        'order_tracking': "Track your order in the 'My Orders' section or use the tracking ID.",
        'subscription': "Cancel your subscription in account settings or contact support."
    }
    return responses.get(prediction[0], "I'm sorry, I couldn't understand your query.")

# Login Screen
def login_screen():
    def verify_credentials():
        username = username_entry.get()
        password = password_entry.get()
        if username == "admin" and password == "password123":  # Example credentials
            login_window.destroy()
            chatbot_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")

    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("400x300")
    login_window.config(bg="#1e293b")

    tk.Label(login_window, text="Login", font=("Helvetica", 18, "bold"), bg="#1e293b", fg="#facc15").pack(pady=20)

    tk.Label(login_window, text="Username:", font=("Helvetica", 12), bg="#1e293b", fg="white").pack(pady=5)
    username_entry = tk.Entry(login_window, font=("Helvetica", 12))
    username_entry.pack(pady=5)

    tk.Label(login_window, text="Password:", font=("Helvetica", 12), bg="#1e293b", fg="white").pack(pady=5)
    password_entry = tk.Entry(login_window, font=("Helvetica", 12), show="*")
    password_entry.pack(pady=5)

    tk.Button(login_window, text="Login", command=verify_credentials, bg="#3b82f6", fg="white", font=("Helvetica", 12, "bold")).pack(pady=20)

    login_window.mainloop()

# Chatbot Screen
def chatbot_screen():
    # GUI Setup
    root = tk.Tk()
    root.title("Genie - Customer Support Chatbot")
    root.geometry("700x800")
    root.config(bg="#1e293b")

    # Header
    header_label = tk.Label(root, text="Welcome to Genie", font=("Helvetica", 22, "bold"), bg="#1e293b", fg="#facc15")
    header_label.pack(pady=10)

    # Chat Display Frame
    chat_frame = tk.Frame(root, bg="#374151")
    chat_frame.pack(pady=10, fill="both", expand=True)

    chat_display = scrolledtext.ScrolledText(
        chat_frame, wrap="word", width=70, height=20, state="disabled", bg="#f3f4f6", fg="#111827", font=("Helvetica", 14)
    )
    chat_display.pack(padx=10, pady=10, fill="both", expand=True)

    # User Input Frame
    input_frame = tk.Frame(root, bg="#1e293b")
    input_frame.pack(pady=10, fill="x")

    user_input = tk.Text(input_frame, width=50, height=3, font=("Helvetica", 14), bg="#f3f4f6", fg="#111827")
    user_input.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

    # Buttons Frame
    buttons_frame = tk.Frame(root, bg="#1e293b")
    buttons_frame.pack(pady=5, fill="x")

    # Clear Chat Functionality
    def clear_chat():
        chat_display.config(state="normal")
        chat_display.delete("1.0", "end")
        chat_display.config(state="disabled")

    # Send Button
    def send_message():
        query = user_input.get("1.0", "end").strip()
        if query:
            # Display user query
            chat_display.config(state="normal")
            chat_display.insert("end", f"User: {query}\n")
            
            # Get chatbot response
            response = get_response(query)
            chat_display.insert("end", f"Genie: {response}\n\n")
            chat_display.config(state="disabled")
            
            # Clear input box
            user_input.delete("1.0", "end")
        else:
            messagebox.showwarning("Input Error", "Please enter a message!")

    send_button = tk.Button(buttons_frame, text="Send", command=send_message, width=12, bg="#3b82f6", fg="white", font=("Helvetica", 12, "bold"))
    send_button.grid(row=0, column=0, padx=5)

    clear_button = tk.Button(buttons_frame, text="Clear Chat", command=clear_chat, width=12, bg="#ef4444", fg="white", font=("Helvetica", 12, "bold"))
    clear_button.grid(row=0, column=1, padx=5)

    # Additional Feature: Data Visualization / EDA Button
    def show_eda():
        loading = tk.Toplevel(root)
        loading.title("Processing EDA")
        loading.geometry("300x150")
        loading.config(bg="#1e293b")

        tk.Label(loading, text="Loading EDA...", font=("Helvetica", 12), bg="#1e293b", fg="#facc15").pack(pady=20)
        progress = ttk.Progressbar(loading, orient="horizontal", length=250, mode="determinate")
        progress.pack(pady=10)

        for i in range(101):
            time.sleep(0.02)  # Simulating processing
            progress['value'] = i
            loading.update_idletasks()

        loading.destroy()
        display_eda_chart()

    def display_eda_chart():
        word_freq = pd.Series(' '.join(data['text']).split()).value_counts().head(5)
        plt.figure(figsize=(8, 8))
        plt.pie(word_freq, labels=word_freq.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
        plt.title("Top 5 Frequent Words in Customer Queries", fontsize=16)
        plt.show()

    eda_button = tk.Button(buttons_frame, text="Show EDA", command=show_eda, width=12, bg="#10b981", fg="white", font=("Helvetica", 12, "bold"))
    eda_button.grid(row=0, column=2, padx=5)

    # Exit Button
    def exit_chatbot():
        root.destroy()

    exit_button = tk.Button(buttons_frame, text="Exit", command=exit_chatbot, width=12, bg="#1e293b", fg="white", font=("Helvetica", 12, "bold"))
    exit_button.grid(row=0, column=3, padx=5)

    root.mainloop()

# Start the application
login_screen()
