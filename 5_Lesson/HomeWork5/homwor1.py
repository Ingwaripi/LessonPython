# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
# in
# Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва
# in
# Number of words: -1
# out
# The data is incorrect




from random import sample



def list_rnd(count: int, alp: str = 'абв'):
    return " ".join("".join(sample(alp, 3)) for _ in range(count))

def simple_sentence(words: str) -> str:
    return " ".join(words.replace("абв","").split())

all_list = list_rnd(int(input("Enter number: ")))
print(all_list)
print(simple_sentence(all_list))
