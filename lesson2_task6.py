###################################################################################################################
# TASK 6

while True:
    try:
        user_input_1 = input("Введите наименования товара, затем через ПРОБЕЛ его стоимость, количество,"
                             " и единицу измерения (шт, литров, см)").split()
        user_input_1 = (
        user_input_1[0].split(), user_input_1[1].split(), user_input_1[2].split(), user_input_1[3].split(), )
        break
    except IndexError:
        print("Вы ошиблись")
while True:
    try:
        user_input_2 = input("Введите наименования ещё одного товара, затем через ПРОБЕЛ его стоимость, количество,"
                             " и единицу измерения (шт, литров, см)").split()
        user_input_2 = (
        user_input_2[0].split(), user_input_2[1].split(), user_input_2[2].split(), user_input_2[3].split(), )
        break
    except IndexError:
        print("Вы ошиблись")
while True:
    try:
        user_input_3 = input("Введите наименования последнего товара, затем через ПРОБЕЛ его стоимость, количество,"
                             " и единицу измерения (шт, литров, см)").split()
        user_input_3 = (
        user_input_3[0].split(), user_input_3[1].split(), user_input_3[2].split(), user_input_3[3].split(), )
        break
    except IndexError:
        print("Вы ошиблись")
        break

product_list1 = [(1, ), (user_input_1[0], user_input_1[1], user_input_1[2], user_input_1[3], )]
product_list2 = [(2, ), (user_input_2[0], user_input_2[1], user_input_2[2], user_input_2[3], )]
product_list3 = [(3, ), (user_input_3[0], user_input_3[1], user_input_3[2], user_input_3[3], )]

product_names = dict({"Название": [user_input_1[0], user_input_2[0], user_input_3[0]]})
product_costs = dict({"Стоимость": [user_input_1[1], user_input_2[1], user_input_3[1]]})
product_quantity = dict({"Количество": [user_input_1[2], user_input_2[2], user_input_3[2]]})
product_unit = dict({"Единица": [user_input_1[3], user_input_2[3], user_input_3[3]]})

result_dict = {
    "Название": [user_input_1[0], user_input_2[0], user_input_3[0]],
    "Стоимость": [user_input_1[1], user_input_2[1], user_input_3[1]],
    "Количество": [user_input_1[2], user_input_2[2], user_input_3[2]],
    "Единица": [user_input_1[3], user_input_2[3], user_input_3[3]]
               }

###################################################################################################################

