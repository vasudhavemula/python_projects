import random

def generate_password(length):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'  
    uppercase = lowercase.upper()             
    digits = '0123456789'
    chars = digits + lowercase + uppercase
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password
def main():
    print("How many passwords do you want to generate?", end=' ')
    num = int(input())
    print(f"Generating {num} passwords")
    print("Minimum length of password should be 3")

    for i in range(num):
        while True:
            print(f"Enter length for Password #{i+1}: ", end="")
            length = int(input())
            if length >= 3:
                break
            print("Password must be at least 3 characters!")
        
        print(f"Password #{i+1} = {generate_password(length)}")

if __name__ == "__main__":
    main()