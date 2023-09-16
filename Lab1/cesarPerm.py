def shuffle_alphabet(key, alphabet):
    # Ensure the permutation key is at least 7 characters long
    if len(key) < 7:
        raise ValueError("Permutation key must be at least 7 characters.")

    # Remove any duplicate characters from the key and convert to uppercase
    key = ''.join(sorted(set(key.upper()), key=lambda x: key.upper().index(x)))

    # Create the shuffled alphabet by placing unique characters from the key at the beginning
    shuffled_alphabet = key + ''.join(sorted(set(alphabet) - set(key)))
    print(shuffled_alphabet)
    # Create a dictionary for the shuffled alphabet
    alphabet_dict = {}
    for i, letter in enumerate(shuffled_alphabet):
        alphabet_dict[letter] = i

    return alphabet_dict


def caesar_cipher(text, main_key, permutation_key, action):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_dict = {}
    for i, letter in enumerate(alphabet):
        alphabet_dict[letter] = i

    # Shuffle the alphabet dictionary based on the permutation key
    shuffled_dict = shuffle_alphabet(permutation_key, alphabet)

    # Remove spaces from the input text and convert to uppercase
    text = text.replace(" ", "").upper()

    # Initialize an empty string to store the result
    result_text = ''

    # Iterate through each character in the input text
    for char in text:
        if char in alphabet:
            # If the character is in the alphabet, perform the key-based shift based on the action
            if action == 'encrypt':
                tmp = alphabet_dict[char]
                shifted_index = (tmp + main_key) % 26
                encrypted_char = list(shuffled_dict.keys())[list(shuffled_dict.values()).index(shifted_index)]
                result_text += encrypted_char
            elif action == 'decrypt':
                tmp = shuffled_dict[char]
                shifted_index = (tmp - main_key) % 26
                encrypted_char = list(alphabet_dict.keys())[list(alphabet_dict.values()).index(shifted_index)]
                result_text += encrypted_char
        else:
            # If the character is not in the alphabet (e.g., punctuation), leave it unchanged
            result_text += char

    return result_text

# Input from the user
user_text = input("Enter the text: ")
user_main_key = int(input("Enter the main key (an integer): "))
user_permutation_key = input("Enter the permutation key (at least 7 characters): ").upper()
user_action = input("Choose action (encrypt or decrypt): ").lower()

# Check if the user action is valid
if user_action not in ['encrypt', 'decrypt']:
    print("Invalid action. Please choose 'encrypt' or 'decrypt'.")
else:
    try:
        # Perform the requested action
        result_text = caesar_cipher(user_text, user_main_key, user_permutation_key, user_action)

        if user_action == 'encrypt':
            print("Encrypted:", result_text)
        else:
            print("Decrypted:", result_text)
    except ValueError as e:
        print(e)
