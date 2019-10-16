from ch1_05 import generate_n_gram
x = set(generate_n_gram(2, "paraparaparadise"))
y = set(generate_n_gram(2, "paragraph"))

print(x | y)
print(x & y)
print("se" in x)
print("se" in y)
