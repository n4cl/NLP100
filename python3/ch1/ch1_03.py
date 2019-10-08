sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
symboles = ".,"

for symble in symboles:
    sentence = sentence.replace(symble, "")

print(sentence.split())
