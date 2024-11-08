# Import necessary libraries
import tkinter as tk
from tkinter import messagebox
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample Data (for demo purposes, you can replace this with actual data)
data = pd.DataFrame({
    'text': ['How to reset password?', 'What is your return policy?', 'How to track my order?', 'Cancel my subscription'],
    'label': ['password', 'return_policy', 'order_tracking', 'subscription']
})

# Data Pre-processing
data['text'] = data['text'].str.lower()  # Convert text to lowercase
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

# Function to predict the response
def get_response(query):
    query_vectorized = vectorizer.transform([query])
    prediction = model.predict(query_vectorized)
    responses = {
        'password': "You can reset your password by going to the settings page.",
        'return_policy': "Our return policy allows you to return items within 30 days.",
        'order_tracking': "You can track your order in the 'My Orders' section.",
        'subscription': "To cancel your subscription, go to your account settings."
    }
    return responses.get(prediction[0], "I'm sorry, I don't understand that.")

# GUI Setup with Tkinter
root = tk.Tk()
root.title("Genie - Customer Support Chatbot")
root.geometry("500x600")

# Header
header_label = tk.Label(root, text="Welcome to Genie", font=("Helvetica", 18, "bold"))
header_label.pack(pady=10)

# Chat Display Frame
chat_frame = tk.Frame(root)
chat_frame.pack(pady=10)

chat_display = tk.Text(chat_frame, wrap="word", width=60, height=15, state="disabled", bg="#f4f4f4", fg="black")
chat_display.grid(row=0, column=0)

# Scrollbar for chat display
scrollbar = tk.Scrollbar(chat_frame, command=chat_display.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
chat_display.config(yscrollcommand=scrollbar.set)

# User Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

user_input = tk.Entry(input_frame, width=40, font=("Helvetica", 14))
user_input.grid(row=0, column=0, padx=10)

# Send Button
def send_message():
    query = user_input.get()
    if query:
        # Display user query
        chat_display.config(state="normal")
        chat_display.insert("end", f"User: {query}\n")
        
        # Get chatbot response
        response = get_response(query)
        chat_display.insert("end", f"Genie: {response}\n\n")
        chat_display.config(state="disabled")
        
        # Clear input box
        user_input.delete(0, "end")
    else:
        messagebox.showwarning("Input Error", "Please enter a message!")

send_button = tk.Button(input_frame, text="Send", command=send_message, width=10)
send_button.grid(row=0, column=1)

# Additional Feature: Data Visualization / EDA Button
def show_eda():
    word_freq = pd.Series(' '.join(data['text']).split()).value_counts().head(10)
    word_freq_df = pd.DataFrame(word_freq).reset_index()
    word_freq_df.columns = ['Word', 'Frequency']

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Frequency', y='Word', data=word_freq_df)
    plt.title("Top 10 Frequent Words in Customer Queries")
    plt.xlabel("Frequency")
    plt.ylabel("Words")
    plt.show()

eda_button = tk.Button(root, text="Show EDA", command=show_eda, width=15)
eda_button.pack(pady=10)

# Exit Button
def exit_chatbot():
    root.destroy()

exit_button = tk.Button(root, text="Exit", command=exit_chatbot, width=10)
exit_button.pack(pady=10)

# Run the application
root.mainloop()
