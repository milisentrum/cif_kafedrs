numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90,
           -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

sum = 0
nul_ind = 0
for index, value in enumerate(numbers):
    if value is None:
        nul_ind = index
    else:
        sum += value

skipped = sum / len(numbers)

numbers[nul_ind] = skipped

print("Измененный список:", numbers)
