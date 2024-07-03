import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Lowercase check
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Digit check
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # Special character check
    if re.search(r'[@$!%*?&#]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character (@, $, !, %, *, ?, &, #).")

    # Feedback based on strength
    if strength == 5:
        feedback.append("Password is very strong.")
    elif strength == 4:
        feedback.append("Password is strong.")
    elif strength == 3:
        feedback.append("Password is moderate.")
    elif strength == 2:
        feedback.append("Password is weak.")
    else:
        feedback.append("Password is very weak.")

    return strength, feedback

# Example usage
password = input("Enter a password to assess: ")
strength, feedback = assess_password_strength(password)

print(f"Password Strength: {strength}/5")
for comment in feedback:
    print(comment)
