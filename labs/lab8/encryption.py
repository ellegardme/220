def encode(word, key):
    acc = " "
    for c in word:
        i = ord(c)
        i = i + key
        new_char = chr(i)
        acc = acc + new_char
    return acc


def encode_better(m, k):
    acc = " "
    for i in range(len(m)):
        c = ord(m[i])
        key = ord(k[i % len(k)])
        c = (c + key) - 97
        acc += chr(c)
    return acc
