"""
Пример: BANANA.
Слова на B: BANANA, BANAN, BANA, BAN, BA, B - всего 6
Слова на A: ANANA, ANAN, ANA, AN, A - всего 5
Слова на N: NANA, NAN, NA, N - всего 4
Слова на A: ANA, AN, A - всего 3
Слова на N: NA, N - всего 2
Слова на A: A - всего 1

Видим здесь арифметическую прогрессию, формула суммы: Sn = (a1 + an) * n / 2.
У нас a1 всегда равно 1, an = n = len(входная строка),
поэтому общее число слов в этом примере: 6 * (6 + 1) / 2 = 21

Теперь осталось отнести все слова, начинающиеся на гласную к kevin_score,
а на согласную - к stuart_score.
Заметим, что скор по конкретной букве равен len(входная строка) - i,
где i - питоновский индекс буквы в строке (0 <= i <= длина строки - 1)

Поэтому пройдемся по всем буквам в строке, если буква гласная - то отнесем длину строки - i
к kevin_score, иначе - к stuart_score.
"""

def minion_game(s):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    size = len(s)

    for i in range(size):
        if s[i] in vowels:
            kevin_score += size - i
        else:
            stuart_score += size - i

    if stuart_score > kevin_score:
        return f'Stuart {stuart_score}'
    elif kevin_score > stuart_score:
        return f'Kevin {kevin_score}'
    else:
        return 'Draw'


if __name__ == '__main__':
    s = input()
    print(minion_game(s))a