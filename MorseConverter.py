import dictionaries as de
def Text2Morse(text):
    uppercaseText = text.upper()
    listsText = uppercaseText.split(" ")
    for g in listsText:
        if g.isnumeric()==True:
            temp = ""
            for w in g:
                temp+=de.dictionaryAtoM.get(chr(w))
        else:
            for k in g:

    return " ".join(listsText)







print(Text2Morse("ping"))