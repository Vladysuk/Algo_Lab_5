def initial_hash(M, pattern, text, hash_pattern, hash_text, h, digits_amount, prime_number):
    for _ in range(M - 1):
        h = (h * digits_amount) % prime_number

    for i in range(M):
        hash_pattern = (digits_amount * hash_pattern + ord(pattern[i])) % prime_number
        hash_text = (digits_amount * hash_text + ord(text[i])) % prime_number

    return h, hash_text, hash_pattern


def next_characters_hash(i, N, M, digits_amount, hash_text, text, h, prime_number):
    if i < N - M:
        hash_text = (digits_amount * (hash_text - ord(text[i]) * h) + ord(text[i + M])) % prime_number

        if hash_text < 0:
            hash_text = hash_text + prime_number

    return hash_text


def search_pattern(pattern, text, prime_number, digits_amount):
    result = []
    M = len(pattern)
    N = len(text)
    j = 0
    hash_pattern = 0
    hash_text = 0
    h = 1

    h, hash_text, hash_pattern = initial_hash(M, pattern, text, hash_pattern, hash_text, h, digits_amount, prime_number)

    for i in range(N - M + 1):
        if hash_pattern == hash_text:
            for j in range(M):
                if text[i + j] != pattern[j]:
                    break
                else:
                    j += 1

            if j == M:
                result.append((str(i), str(i + j - 1)))

        hash_text = next_characters_hash(i, N, M, digits_amount, hash_text, text, h, prime_number)

    print(result)
    return result
