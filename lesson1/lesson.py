def words_freq(line):
    for word in line.split():
        freq[word] = freq.get(word, 0) + 1

    words = sorted(freq.keys())

    return words, freq

freq = {}
line = input()

words, freq = words_freq(line)

for w in words:
    print("%s:%d" % (w, freq[w]))