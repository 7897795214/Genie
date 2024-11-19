import pandas as pd

# Define the dataset
data = {
    "Customer Query": [
        "Hi, I need help with my account.",
        "I forgot my password.",
        "My order hasn’t arrived yet.",
        "The app keeps crashing when I try to open it.",
        "Can I get a refund for my purchase?",
        "What are your working hours?",
        "How do I contact customer service?",
        "I need help with the payment process.",
        "Does your product come with a warranty?",
        "How can I track my order?",
        "The item I received is damaged.",
        "Do you ship internationally?",
        "Can I cancel my order?",
        "How do I update my contact details?",
        "Can I change the delivery address?",
        "Do you offer any discounts?",
        "Is my data secure with your platform?",
        "What is your return policy?",
        "The payment gateway is not working.",
        "How do I subscribe to your newsletter?",
        "Can I speak with a human representative?",
    ],
    "Genie's Response": [
        "Sure, Gaurav. Could you please provide more details about the issue you're facing?",
        "No problem. You can reset your password by clicking on 'Forgot Password' on the login page. Would you like further assistance?",
        "I’m sorry for the delay, Gaurav. Can you provide your order ID so I can check the status?",
        "I understand your concern. Have you tried updating the app to the latest version? If the issue persists, I can assist further.",
        "Refunds are processed based on our refund policy. May I know the order ID to verify your request?",
        "We are available 24/7 to assist you. Feel free to reach out anytime.",
        "You can contact our customer service through live chat, email, or our helpline number. Which method would you prefer?",
        "Could you please specify the issue you’re experiencing during payment, Gaurav?",
        "Yes, all our products come with a one-year warranty. Do you need help with a warranty claim?",
        "You can track your order by logging into your account and navigating to the 'My Orders' section. Let me know if you need further help.",
        "I apologize for the inconvenience, Gaurav. Could you share a photo of the damaged item and your order ID? We’ll assist you with a replacement or refund.",
        "Yes, we do ship internationally. Let me know your location, and I can provide specific shipping details.",
        "You can cancel your order within 24 hours of placing it. Please provide your order ID, and I’ll check for you.",
        "You can update your contact details in the account settings section. Let me know if you need guidance navigating there.",
        "Delivery address changes are allowed before the order is shipped. Could you provide your order ID to proceed?",
        "Yes, we offer discounts from time to time. You can check our website or subscribe to our newsletter for updates.",
        "Your data security is our top priority. We use advanced encryption to protect your information.",
        "Our return policy allows returns within 30 days of delivery. Let me know if you’d like assistance with a return.",
        "I apologize for the inconvenience. Could you please try again in a different browser? If the issue persists, I’ll escalate it to our technical team.",
        "You can subscribe by entering your email address in the subscription box at the bottom of our homepage.",
        "Of course, Gaurav. Let me connect you to one of our representatives. Please hold on for a moment.",
    ],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
file_name = "customer_support_dataset.csv"
df.to_csv(file_name, index=False)

print(f"Dataset has been saved as {file_name}")
