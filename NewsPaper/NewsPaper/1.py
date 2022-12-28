text = "Новости спорта — Сегодня у нас в России проходят матчи Лиги Чемпионов. " \
       "Напомню, что «Зенит», «Краснодар» и «Локомотив» продолжают борьбу за выход в 1/8 финала. " \
       "«Валенсия», «Тоттенхэм», «РБ Лейпциг», «Лион» и ЦСКА продолжают борьбу в Лиге Европы."


def censor(text):
    censor_list = ["погибло", "ограбить", "борьбу"]

    for i in text:
        text = text.split()
        if i in censor_list:
            reword = i[0] + ((len(i) - 1) * "*")
            text = str(text.join(" "))
            text = text.replace(i, reword)

    return print(text)


c = "матчи"
k = 1
censor(text)
# print(text.split())
