# encrypt.py - Run this ONCE to encrypt your token
token = ""
key = ""

print("Original token:", token)

# Encrypt the token
encrypted_chars = []
for i, char in enumerate(token):
    key_char = key[i % len(key)]
    encrypted_chars.append(chr(ord(char) ^ ord(key_char)))

encrypted_token = ''.join(encrypted_chars)
print("\nEncrypted token (copy this):")
print('"' + encrypted_token + '"')
