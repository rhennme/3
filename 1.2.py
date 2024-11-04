def generate_vigenere_table():
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    table = []
    for i in range(len(alphabet)):
        row = alphabet[i:] + alphabet[:i]
        table.append(row)
    return table


def encrypt_vigenere(text, key):
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    text = text.upper()
    key = key.upper()
    table = generate_vigenere_table()

    encrypted_text = []
    key_length = len(key)

    for i, char in enumerate(text):
        if char in alphabet:
            row = alphabet.index(key[i % key_length])
            col = alphabet.index(char)
            encrypted_char = table[row][col]
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)


def decrypt_vigenere(encrypted_text, key):
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    encrypted_text = encrypted_text.upper()
    key = key.upper()
    table = generate_vigenere_table()

    decrypted_text = []
    key_length = len(key)

    for i, char in enumerate(encrypted_text):
        if char in alphabet:
            row = alphabet.index(key[i % key_length])
            col = table[row].index(char)
            decrypted_char = alphabet[col]
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)


def display_vigenere_table():
    table = generate_vigenere_table()
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    print("Таблица Виженера:")
    print("   ", end="")
    for letter in alphabet:
        print(f"{letter} ", end="")
    print()

    for i, row in enumerate(table):
        print(f"{alphabet[i]}  ", end="")
        for char in row:
            print(f"{char} ", end="")
        print()



original_text = input("Бастапқы хабарлама:")
key = input("Кілтсөз еңгізініз:")

encrypted = encrypt_vigenere(original_text, key)
decrypted = decrypt_vigenere(encrypted, key)

print(f"Бастапқы хабарлама: {original_text}")
print(f"Шифрланған бағдарлама: {encrypted}")
print(f"Дешифрланған бағдарлама: {decrypted}")

# Виженер кесте көрсету
display_vigenere_table()
