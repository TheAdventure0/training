def password(n):
    pairs = []
    used = set()

    for i in range(1, n + 1):
        if i in used:
            continue

        for a in range(i, n + 1):
            if a in used:
                continue

            if (i + a) != 0 and n % (i + a) == 0:
                pairs.append((i, a))
                used.add(i)
                used.add(a)
                break

    passw_ = ""
    for i, a in pairs:
        passw_ += str(i) + str(a)

    return passw_

# print(password(3))
# print(password(4))
# print(password(5))
# print(password(6))
# print(password(7))

