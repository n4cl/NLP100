sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
first_string = [1, 5, 6, 7, 8, 9, 15, 16, 19]

# index の値を調整
first_string = list(map(lambda x: x - 1, first_string))

sentence = sentence.replace(".", "")
words = sentence.split()

element = {}
for index, word in enumerate(words):
    if index in first_string:
        element[index] = word[:1]
    else:
        element[index] = word[:2]

print(element)
