def emj_converter(message):
    word = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😒"
    }
    output = ""
    for words in word:
        output += emojis.get(words, words) + " "
    return output


message = input(">")
print(emj_converter(message))