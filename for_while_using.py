def summ_of_even_from_one_to_one_hundred():
    even_summ = 0
    for n in range(1, 100+1): #  от 1 до 100 включительно
        if n % 2 ==0:
            even_summ += n
    print("2 + 4 + 6 + ... + 100 =", even_summ)


def summ_of_squares_of_odd_from_one_to_ten():
    square_list = [x*x for x in range(1, 10+1) if x % 2 != 0]
    print(square_list)


def input_and_counting_of_the_entered_numbers_stops_by_entering_a_negative_number():
    count = 0
    number = 0
    while number >= 0:  #   Отрицательное число, введённое последним, тоже считается
        try:
            number = float(input("Введите число: ").strip())
            count += 1 #  Успешный ввод засчитывается
        except ValueError:
            print('''Ввод не засчитан, пожалуйста, введите целое число 
или десятичную дробь, положительное число, отрица-
тельное число или 0(ноль). Используйте только циф-
ры, а также (при необходимости) точку и знак минус''')
    print("Количество введённых чисел = ", count)


summ_of_even_from_one_to_one_hundred()
summ_of_squares_of_odd_from_one_to_ten()
input_and_counting_of_the_entered_numbers_stops_by_entering_a_negative_number()