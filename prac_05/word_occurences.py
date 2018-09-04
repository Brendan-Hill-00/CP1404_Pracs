text = input("Text: ")
occurrences_in_text = {}
split_words = text.split()
for word in split_words:
    if word in occurrences_in_text:
        occurrences_in_text[word] += 1
    else:
        occurrences_in_text[word] = 1
#for occurrence in occurrences_in_text:

for occurence in sorted(occurrences_in_text):
    print("{}: {}".format(occurrences_in_text, occurrences_in_text[occurence]))