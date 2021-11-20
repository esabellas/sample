from collections import Counter
def word_freq_count(fname):
    with open(fname) as inFile:
        return Counter(inFile.read().split())
fname=input("enter the file name:")
print("words and frequency")
print(word_freq_count(fname))
