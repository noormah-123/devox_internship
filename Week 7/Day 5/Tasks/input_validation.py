import re


def validate_input(user_input):
    # Remove unnecessary spaces
    user_input = user_input.strip()

    # Check for empty input
    if not user_input:
        return False, "Input cannot be empty."

    # Check maximum length
    if len(user_input) > 100:
        return False, "Input is too long."

    # Block common SQL injection patterns
    sql_patterns = [
        r"\bOR\s+1\s*=\s*1\b",
        r"\bAND\s+1\s*=\s*1\b",
        r"\bDROP\s+TABLE\b",
        r"\bDELETE\s+FROM\b",
        r"\bUNION\s+SELECT\b",
        r"--"
    ]

    for pattern in sql_patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            return False, "Suspicious SQL-like input detected."

    # Block HTML/JavaScript tags
    if re.search(r"<\s*script\b", user_input, re.IGNORECASE):
        return False, "Suspicious script input detected."

    # Block common command injection characters
    dangerous_characters = [";", "|", "`", "$(", "&&"]

    for character in dangerous_characters:
        if character in user_input:
            return False, "Suspicious characters detected."

    return True, "Input is valid."


# Test inputs
test_inputs = [
    "Hello, my name is Ali.",
    "This is a normal message.",
    "",
    "OR 1=1",
    "' UNION SELECT username, password FROM users --",
    "<script>alert('Hello')</script>",
    "hello; rm -rf /",
    "This is a valid input!"
]

print("INPUT VALIDATION RESULTS")
print("------------------------")

for text in test_inputs:
    valid, message = validate_input(text)

    print(f"\nInput: {text}")
    print(f"Result: {'ALLOWED' if valid else 'BLOCKED'}")
    print(f"Message: {message}")