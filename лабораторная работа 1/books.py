# TODO Найдите количество книг, которое можно разместить на дискете


pages = 100
lines_per_list = 50
chars_per_line = 25
v = 1.44 * 1024 * 1024

book_weight = 4 * chars_per_line * lines_per_list * pages

print("Количество книг, помещающихся на дискету:", int(v // book_weight))
