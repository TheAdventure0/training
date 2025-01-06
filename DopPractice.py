for n in range(3, 21):
    result = ''
    used_pairs = set()

    for i in range(1, 21):
        for a in range(i + 1, 21):
            pair_sum = i + a
            if n % pair_sum == 0 and (i, a) not in used_pairs and (a, i) not in used_pairs:
                result += str(i) + str(a)
                used_pairs.add((i, a))
                used_pairs.add((a, i))

    print(f'Число: {n}, Пароль: {result}')
