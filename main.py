from secrets import choice, SystemRandom

#Создаем мини-базу для создания пароля
nums = "1234567890"
spec_chars = r"""!?.,:;"'()[]{}<>+-*/=~^|\@#$%&_"""
low_let = "abcdefghijklmnopqrstuvwxyz"
big_let = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
all_chars = nums + spec_chars + low_let + big_let



#Организуем основную функцию
def main():
    pas = ""



    #Узнаем какую длину пароля требует пользователь и даем ему рекомендации
    len_pass = int(input("Какой длины вам нужен пароль?(Запишите используя цифры, а не слова) "
                         "Для данной программы минимальное количество символов 4.\n"
                         "Учтите, надежным считается пароль, состоящий минимум из 12–16 символов\n"))

    #Проверка условия на минимальное количество символов
    if len_pass < 4:
        print("Длина пароля не должна быть меньше 4 символов!!!")
        return main()

    ans = str(input(f"Вы уверены, что хотите установить пароль"
                    f" с длиной {len_pass} Да/Нет?\n"))

    #Проверка условия подстверждения длины пароля
    if ans.lower() == "да":


        #---КРИПТОГРАФИЧЕСКОЕ СОЗДАНИЕ ПАРОЛЯ---

        pas_list = [
            choice(nums),
            choice(spec_chars),
            choice(low_let),
            choice(big_let),
        ]
        #Добавляем изначально все виды символов для надежности
        pas += pas_list[0] + pas_list[1] + pas_list[2] + pas_list[3]
        mod_len = len_pass - 4

        #Доводим пароль до определенной длины, добавляя различные символы
        for _ in range(mod_len):
            pas += (choice(all_chars))

        #Перемешиваем состовляющие пароля для полной надежности, т.к. до этого было произведено недальновидное действие,
        #а именно добавление в начало пароля 4 разных символа
        mix_pas = SystemRandom().sample(pas, k=len(pas))
        final_pas = "".join(mix_pas)
        print(f"Ваш надежный сгенерированный пароль: {final_pas}")
    else:
        main()

main()
