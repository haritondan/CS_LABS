def validate_input(input_text):
    input_text = input_text.upper()
    valid_characters = set('AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ')
    if not all(char in valid_characters for char in input_text):
        invalid_chars = ''.join(char for char in input_text if char not in valid_characters)
        suggestions = ''.join(char if char.isalpha() or char in 'ĂÎÂȘȚ' else ' ' for char in input_text)
        return False, f"Invalid characters: {invalid_chars}\nSuggested input: {suggestions}"
    return True, input_text


def create_matrix(key):  # 5x6 matrix
    matrix = [['' for _ in range(6)] for _ in range(5)]
    key = key.replace(' ', '').upper()
    key += 'AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ'
    key = ''.join(dict.fromkeys(key))  # Remove duplicate characters
    key_index = 0

    for i in range(5):
        for j in range(6):
            matrix[i][j] = key[key_index]
            key_index += 1

    return matrix


def find_char(matrix, char):
    for i in range(5):
        for j in range(6):
            if matrix[i][j] == char:
                return i, j
    return None


def playfair_encrypt(plaintext, key):
    matrix = create_matrix(key)
    for line in matrix:
        print(line)
    plaintext = plaintext.replace(' ', '').upper()
    ciphertext = []
    i = 0

    # If the characters are in the same row, it replaces to their right, wrapping around to the start of the row if necessary.
    # If the characters are in the same column, it replaces below them, wrapping around to the top of the column if necessary.
    # If the characters are not in the same row or column, it forms a rectangle with the characters as corners and replaces them with the characters on the same row but in the other pair's column.
    while i < len(plaintext):
        if i + 1 < len(plaintext):
            if plaintext[i] == plaintext[i + 1]:
                plaintext = plaintext[:i + 1] + 'X' + plaintext[i + 1:]

        char1 = plaintext[i]
        char2 = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'

        row1, col1 = find_char(matrix, char1)
        row2, col2 = find_char(matrix, char2)

        if row1 == row2:
            ciphertext.append(matrix[row1][(col1 + 1) % 6])
            ciphertext.append(matrix[row2][(col2 + 1) % 6])
        elif col1 == col2:
            ciphertext.append(matrix[(row1 + 1) % 5][col1])
            ciphertext.append(matrix[(row2 + 1) % 5][col2])
        else:
            ciphertext.append(matrix[row1][col2])
            ciphertext.append(matrix[row2][col1])

        i += 2

    return ''.join(ciphertext)


def playfair_decrypt(ciphertext, key):
    matrix = create_matrix(key)
    print(matrix)
    ciphertext = ciphertext.replace(' ', '').upper()
    plaintext = []

    # If the characters are in the same row, it replaces to left, wrapping around to the end of the row if necessary.
    # If the characters are in the same column, it replaces to above them, wrapping around to the bottom of the column if necessary.
    # If the characters are not in the same row or column, it forms a rectangle with the characters as corners and replaces them with the characters on the same row but in the other pair's column.
    i = 0
    while i < len(ciphertext):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]

        row1, col1 = find_char(matrix, char1)
        row2, col2 = find_char(matrix, char2)

        if row1 == row2:
            plaintext.append(matrix[row1][(col1 - 1) % 6])
            plaintext.append(matrix[row2][(col2 - 1) % 6])
        elif col1 == col2:
            plaintext.append(matrix[(row1 - 1) % 5][col1])
            plaintext.append(matrix[(row2 - 1) % 5][col2])
        else:
            plaintext.append(matrix[row1][col2])
            plaintext.append(matrix[row2][col1])

        i += 2

    plaintext = ''.join(plaintext).replace('X', '')  # Remove any 'X' added during encryption
    return plaintext


def main():
    def main():
        while True:
            operation = input("Choose operation (encrypt/decrypt): ").strip().lower()
            if operation not in ('encrypt', 'decrypt'):
                print("Invalid operation. Please choose 'encrypt' or 'decrypt'.")
                continue

            key = input("Enter the key (must be at least 7 characters long): ").strip()
            if len(key) < 7:
                print("Key must be at least 7 characters long.")
                continue

            message = input("Enter the message or cryptogram: ").strip()

            if operation == 'encrypt':
                encrypted_message = playfair_encrypt(message, key)
                print("Encrypted message:", encrypted_message)
            else:
                decrypted_message = playfair_decrypt(message, key)
                print("Decrypted message:", decrypted_message)

            another = input("Do you want to perform another operation? (yes/no): ").strip().lower()
            if another != 'yes':
                break

    if __name__ == "__main__":
        main()


if __name__ == "__main__":
    main()
