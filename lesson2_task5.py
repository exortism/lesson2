my_rating_list = [1, 2, 3, 4, 5]
def sortInAscendingOrder(sort_input):
    return max(my_rating_list[0])

while True:
    try:
        user_input = int(input('Введите новый элемент "рейтинга"'))
        my_rating_list.append(user_input)
        sortInAscendingOrder(sort_input)
        print(my_rating_list)
        if user_input == "quit":
            break



    except ValueError:
        print('Запрашиваемые данные необходимо ввести числом')


