from random import choice


EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке

for count in counts:
    val = [choice(coin) for i in range(count)]
    # TODO разделить минимальное число среди орлов и решек на максимальное число и сохранить результат
    e = val.count(EAGLE)
    o = val.count(TAILS)
    if e > o:
        list_freq.append(e/o)
    else:
        list_freq.append(o/e)
print(list_freq)
