# Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code
# for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#
# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given
# value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the
# cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#
# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random
# bytes. The user would keep the encrypted message and the encryption key in different locations, and without both
# "halves", it is impossible to decrypt the message.
#
# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If
# the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
# The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
#
# Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt
# (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the
# plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the
# original text.

encrypted_ints = open('059_cipher.txt', 'r').read()
encrypted_ints = [int(number) for number in encrypted_ints.split(',')]

for a in range(24):
    for b in range(24):
        for c in range(24):
            # ASCII 97 == 'a'
            cipher = [97 + a, 97 + b, 97 + c]

            decrypted = []
            for i in range(len(encrypted_ints)):
                decrypted.append(encrypted_ints[i] ^ cipher[i % 3])

            decrypted_chars = [chr(char) for char in decrypted]
            decrypted_string = ''.join(decrypted_chars)
            if ' the ' in decrypted_string.lower():
                print(decrypted_string)
                print(''.join([chr(char) for char in cipher]))
                print('Char sum: {}'.format(sum(decrypted)))
                exit(0)
