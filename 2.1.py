def encrypt_message(message, rows, cols):
    # Хабарламаны кестеге орналастыру
    message = message.replace(" ", "")  # Бос орындарды алып тастаймыз
    message += " " * (rows * cols - len(message))  # Кесте көлеміне дейін толықтыру

    # Кестені құру
    grid = [['' for _ in range(cols)] for _ in range(rows)]
    index = 0

    for col in range(cols):
        for row in range(rows):
            if index < len(message):
                grid[row][col] = message[index]
                index += 1

    # Шифрлау
    encrypted_message = ""
    for row in grid:
        encrypted_message += "".join(row)

    return encrypted_message, grid


def decrypt_message(encrypted_message, rows, cols):
    # Дешифрлау процесі: шифрланған хабарламаны кестеге орналастыру
    grid = [['' for _ in range(cols)] for _ in range(rows)]
    index = 0

    for row in range(rows):
        for col in range(cols):
            if index < len(encrypted_message):
                grid[row][col] = encrypted_message[index]
                index += 1

    # Кестеден жолдар бойынша оқимыз
    decrypted_message = ""
    for col in range(cols):
        for row in range(rows):
            decrypted_message += grid[row][col]

    # Алынған хабарламадан бос орындарды алып тастаймыз
    decrypted_message = decrypted_message.replace(" ", "")

    return decrypted_message


def print_grid(grid):
    for row in grid:
        print(" | ".join(row))
    print()


# Пайдаланушыдан енгізу (шифрлау)
message = input("Хабарламаны енгізіңіз: ")
rows = int(input("Жолдар санын енгізіңіз: "))
cols = int(input("Бағандар санын енгізіңіз: "))

# Шифрлау
encrypted_message, grid = encrypt_message(message, rows, cols)

# Нәтижелерді көрсету (шифрлау)
print("Кесте:")
print_grid(grid)
print("Шифрланған хабарлама:", encrypted_message)

# Алушыдан енгізуді сұрау (дешифрлау)
print("\nШифрланған хабарламаны алған алушыдан:")
rows_received = int(input("Жолдар санын енгізіңіз: "))
cols_received = int(input("Бағандар санын енгізіңіз: "))

# Дешифрлау
decrypted_message = decrypt_message(encrypted_message, rows_received, cols_received)
print("Дешифрланған хабарлама:", decrypted_message)
