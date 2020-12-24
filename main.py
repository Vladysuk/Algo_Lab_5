from rabin_karp import search_pattern
if __name__ == "__main__":
    with open('rabin_karp.in', 'r+') as fileIn:
        text = fileIn.readline()
        pattern = fileIn.readline()

    prime_number = 893
    digits_amount = 256

    with open('rabin_karp.out', 'w') as fileOut:
        fileOut.write('\n'.join('%s %s' % x for x in search_pattern(pattern, text, prime_number, digits_amount)))
