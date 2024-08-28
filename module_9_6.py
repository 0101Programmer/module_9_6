def all_variants(text):
    n = 0
    while n < len(text):
        i = text[n]
        yield i
        n += 1

    a = 0
    b = 1
    for i in range(len(text)):
        while a < len(text) and b < len(text):
            i = text[a]
            j = text[b]
            yield i + j
            a += 1
            b += 1

    yield text


gen = all_variants('Scooby')
for _ in gen:
    print(_)
