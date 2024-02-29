message = input(">")
word = message.split(' ')
emojis = {
    ":)": "😊",  # emj in windows by shift + > and for MAC ctrl + Cmd + space.
    ":(": "😒"
}
output = ""
for words in word:
    output += emojis.get(words, words) + " "
print(output)
