import random 
import string as str

def generate_password(length, complexity):
    # Define the character sets for different complexities
    letters = str.ascii_letters
    digits = str.digits
    special_chars = str.punctuation

    # Select character set based on complexity level
    if complexity == 'low':
        char_set = letters
    elif complexity == 'medium':
        char_set = letters + digits
    elif complexity == 'high':
        char_set = letters + digits + special_chars
    else:
        raise ValueError("Invalid complexity level. Choose 'low', 'medium', or 'high'.")

    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def main():
    # Get the user's input for password length and complexity level
    length = int(input("Enter the desired password length: "))
    if length <= 0:
                print("Length must be a positive number.")
                
    while True:
        complexity = input("Enter password complexity (low, medium, high): ").lower()
        if complexity in ["low", "medium", "high"]:
            break
        else:
            print("Invalid complexity. Please choose 'low', 'medium', or 'high'.")
    
   
    password = generate_password(length, complexity)
    print("Generated password:", password)

if __name__ == "__main__":
    main()


