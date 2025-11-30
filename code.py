import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length check
    if len(password) < 8:
        feedback.append("Password is too short (minimum 8 characters).")
    elif len(password) >= 12:
        score += 2
    else:
        score += 1
    
    # Character variety checks
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")
    
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")
    
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add digits.")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters.")
    
    # Common weaknesses
    if password.islower() or password.isupper():
        score -= 1
        feedback.append("Mix uppercase and lowercase letters.")
    
    if re.search(r'(.)\1{2,}', password):  # Repeated characters
        score -= 1
        feedback.append("Avoid repeated characters.")
    
    if re.search(r'(012|123|234|345|456|567|678|789|abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', password.lower()):
        score -= 1
        feedback.append("Avoid sequential characters.")
    
    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    elif score <= 6:
        strength = "Strong"
    else:
        strength = "Very Strong"
    
    return strength, feedback, score

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to check: ")
    strength, feedback, score = check_password_strength(password)
    print(f"Password Strength: {strength} (Score: {score}/8)")
    if feedback:
        print("Suggestions:")
        for item in feedback:
            print(f"- {item}")
