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


def print_grid(grid):
    for row in grid:
        print(" | ".join(row))
    print()


# Пайдаланушыдан енгізу
message = input("Хабарламаны енгізіңіз: ")
rows = int(input("Жолдар санын енгізіңіз: "))
cols = int(input("Бағандар санын енгізіңіз: "))

# Шифрлау
encrypted_message, grid = encrypt_message(message, rows, cols)

# Нәтижелерді көрсету
print("Кесте:")
print_grid(grid)
print("Шифрланған хабарлама:", encrypted_message)
