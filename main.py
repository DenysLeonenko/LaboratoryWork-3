input_value = input("Введіть ціле число = ")

if not input_value.isdigit():
    print("Вводиме значення має бути цілим числом")
    input_value = input("Введіль ціле число, ще раз")

number_array = [int(number) for number in input_value]
print(*number_array)
print("_ " * len(input_value))
max_value = max(number_array)
for row_value in range(max_value, 0, -1):
    row_str = ""
    for num in number_array:
        if num >= row_value:
            row_str += "# "
        else:
            row_str += "  "
    print(row_str)
