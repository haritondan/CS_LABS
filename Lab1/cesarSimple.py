def caesar_cipher(text, key, action):
    alphabet_dict = {}
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i, letter in enumerate(alphabet):
        alphabet_dict[letter] = i

    text = text.replace(" ", "").upper()

    # Initialize an empty string to store the result
    result_text = ''


    for char in text:
        if char in alphabet:
            # perform the key-based shift based
            if action == 'encrypt':
                shifted_index = (alphabet_dict[char] + key) % 26
            elif action == 'decrypt':
                shifted_index = (alphabet_dict[char] - key) % 26
            encrypted_char = alphabet[shifted_index]
            result_text += encrypted_char
        else:
            # error message
            print(f"Error: Character '{char}' is not in the alphabet.")
            return

    return result_text

user_action = input("Choose action (encrypt or decrypt): ").lower()
user_text = input("Enter the text: ")
user_key = int(input("Enter the key (an integer): "))


# Check if the user action is valid
if user_action not in ['encrypt', 'decrypt']:
    print("Invalid action. Please choose 'encrypt' or 'decrypt'.")
else:
    # Perform the requested action
    result_text = caesar_cipher(user_text, user_key, user_action)

    if result_text is not None:
        if user_action == 'encrypt':
            print("Encrypted:", result_text)
        else:
            print("Decrypted:", result_text)
