import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# -----------------------------------------
# 1. Basic Input Validation
# -----------------------------------------

def validate_input(text):
    text = text.strip()

    if not text:
        return False, "Input cannot be empty."

    if len(text) > 500:
        return False, "Input is too long."

    # Block common suspicious patterns
    suspicious_patterns = [
        r"<\s*script\b",
        r"\bDROP\s+TABLE\b",
        r"\bUNION\s+SELECT\b",
        r"\bOR\s+1\s*=\s*1\b",
        r"--",
    ]

    for pattern in suspicious_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return False, "Suspicious input detected."

    return True, "Input is valid."


# -----------------------------------------
# 2. Small Training Dataset
# -----------------------------------------

training_texts = [
    "Congratulations! You won a free prize. Click here to claim.",
    "You have won a free gift card. Claim your reward now.",
    "URGENT! Your account has been selected for a cash prize.",
    "Click this link to receive your free money.",
    "You are the lucky winner of a free vacation.",
    "Your bank account needs immediate verification. Click the link.",
    "Urgent security alert! Verify your account immediately.",
    "Your password has expired. Login now to avoid account suspension.",
    "Congratulations, you have won a lottery. Send your details now.",
    "Verify your account by clicking this suspicious link.",

    "Hi, are we still meeting for lunch tomorrow?",
    "Please send me the project report when you have time.",
    "The class will start at 10 AM tomorrow.",
    "Thank you for your help with the assignment.",
    "Can you please call me when you are available?",
    "The meeting has been moved to Monday.",
    "I have attached the documents for your review.",
    "Don't forget to submit your homework today.",
    "Hope you are having a great day.",
    "Please let me know if you need any help."
]

# 1 = spam/phishing
# 0 = normal
training_labels = [
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0
]


# -----------------------------------------
# 3. Convert Text into Numerical Features
# -----------------------------------------

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)

X_train = vectorizer.fit_transform(training_texts)


# -----------------------------------------
# 4. Train Classifier
# -----------------------------------------

classifier = LogisticRegression()

classifier.fit(X_train, training_labels)


# -----------------------------------------
# 5. Test Messages
# -----------------------------------------

test_messages = [
    "Congratulations! Click here to claim your free prize.",
    "Can you send me the notes from today's class?",
    "URGENT! Verify your bank account immediately."
]

print("SECURITY-AWARE TEXT CLASSIFIER")
print("==============================")

for message in test_messages:

    valid, validation_message = validate_input(message)

    print("\nMessage:", message)
    print("Validation:", validation_message)

    if not valid:
        print("Classification: BLOCKED")
        continue

    # Convert message into TF-IDF features
    X_test = vectorizer.transform([message])

    # Predict class
    prediction = classifier.predict(X_test)[0]

    # Get confidence
    probabilities = classifier.predict_proba(X_test)[0]
    confidence = max(probabilities)

    if prediction == 1:
        label = "SPAM / PHISHING"
    else:
        label = "NORMAL"

    print("Classification:", label)
    print(f"Confidence: {confidence:.2f}")


# -----------------------------------------
# 6. Interactive User Input
# -----------------------------------------

print("\n\nINTERACTIVE CLASSIFIER")
print("======================")

user_message = input("Enter a message to classify: ")

valid, validation_message = validate_input(user_message)

print("\nValidation:", validation_message)

if not valid:
    print("Message blocked for security reasons.")
else:
    X_user = vectorizer.transform([user_message])

    prediction = classifier.predict(X_user)[0]
    confidence = max(classifier.predict_proba(X_user)[0])

    if prediction == 1:
        print("Classification: SPAM / PHISHING")
    else:
        print("Classification: NORMAL")

    print(f"Confidence: {confidence:.2f}")