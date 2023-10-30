# Initial Permutation Table
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]


def find_L1(message):
    # Convert message to binary
    binary = ''.join(format(ord(c), '08b') for c in message)

    # Apply initial permutation
    permuted = ''.join(binary[IP[i] - 1] for i in range(64))

    # Split into two halves
    L0, R0 = permuted[:32], permuted[32:]

    # L1 is equal to R0
    L1 = R0

    return L1


if __name__ == "__main__":
    message = input("Enter an 8-character message: ")
    L1 = find_L1(message)
    print(f"L1: {L1}")

#Convert the 8-character message into binary. Each character is represented by 8 bits, so you'll end up with a 64-bit binary string.
#Apply the initial permutation (IP) to the 64-bit binary string. The IP rearranges the bits of the message according to a predefined table.
#Split the permuted message into two equal halves, L0 and R0. Each half will be 32 bits long.
#L1 is simply equal to R0, the right half of the initial permutation output.