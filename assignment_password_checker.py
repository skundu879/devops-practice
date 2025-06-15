

def check_password_strength(password):
    if len(password) < 8:
        return False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    special_chars = ".!@#$%"

    for char in password:
        if char >= 'A' and char <= 'Z':
            has_uppercase = True
        elif char >= 'a' and char <= 'z':
            has_lowercase = True
        elif char >= '0' and char <= '9':
            has_digit = True
        else:
            for special_char in special_chars:
                if char == special_char:
                    has_special = True
                    break
    return has_uppercase and has_lowercase and has_digit and has_special


def main():

    password = input("Enter a password to check its strength: ")
    if check_password_strength(password):
        print("Strong password! Your password meets all criteria.")
    else:
        print(
            "Weak password. Ensure it is at least 8 characters long and contains "
            "uppercase and lowercase letters, a digit, and a special character."
        )

if __name__ == "__main__":
    main()
