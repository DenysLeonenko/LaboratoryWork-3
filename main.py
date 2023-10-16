input_value = input("Введіть ціле число = ")
input_char = input("Введіть символ, яким ви хочите виводити діаграму: ")

if input_value.isdigit():
    number_array = [int(number) for number in input_value]
    print(*number_array)
    print("_ " * len(input_value))
    max_value = max(number_array)
    for row_value in range(max_value, 0, -1):
        row_str = ""
        for num in number_array:
            if num >= row_value:
                row_str += input_char + " "
            else:
                row_str += "  "
        print(row_str)
else:
    print("Вводиме значення має бути цілим числом")
    input_value = input("Введіль ціле число, ще раз = ")
