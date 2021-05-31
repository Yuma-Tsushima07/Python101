print("Challenge 22: Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies.")

text = "Like sharks, snakes, and spiders, piranhas are widely feared. Although most people consider piranhas to be quite dangerous, they are, for the most part, entirely harmless. Piranhas rarely feed on large animals; they eat smaller fish and aquatic plants. When confronted with humans, piranhas’ first instinct is to flee, not attack. Their fear of humans makes sense. Far more piranhas are eaten by people than people are eaten by piranhas. If the fish are well-fed, they won’t bite humans."
print(text)
lists = list(text.split(" "))

for word in lists:
    print(str(word) + ": " + str(lists.count(word)))