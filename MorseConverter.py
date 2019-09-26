import dictionaries as de


def converterMPerWord(text):
    newText = []
    for w in text:
        if w in de.ListOfSpecialMarkskey:
            replacement = de.SpecialMarks.get(w)
        else:
            replacement = de.dictionaryAtoM.get(w)
        newText.append(replacement)
    return " ".join(newText)

def Val2Key (word):
    for key,value in de.dictionaryAtoM.items():
        if value == word:
            return key
        else:
            for key,value in de.SpecialMarks.items():
                if value==word:
                    return key
#if the code are SOS or something special information that has highest importance
def specialConverter2(word):
    for key,value in de.SpecialMarks.items():
        if value == word:
            return key

#if the code are SOS or something special information that has highest importance
def specialConverter(word):
    return de.SpecialMarks.get(word)

def morseConverterPerWord(text):
    newText=[]
    splitted = text.split(" ")
    for k in splitted:
        newText.append(Val2Key(k))
    return "".join(newText)

def Text2Morse(text):
    UpperCasing = text.upper()
    splitted = UpperCasing.split(sep=" ")
    if splitted.__len__()<2:
        word = splitted[0]
        if word in de.ListOfSpecialMarkskey:
            return specialConverter(word)
        else:
            return converterMPerWord(word)
    else:
        temps = []
        for w in splitted:
            if w in de.ListOfSpecialMarkskey:
                temps.append(specialConverter(w))
            else:
                temps.append(converterMPerWord(w))
        return "  ".join(temps)

def Morse2Text(text):
    splitted = text.split(sep="  ")
    if splitted.__len__()<2:
        word = splitted[0]
        if word in de.ListOfSpecialMarksval:
            return specialConverter2(word)
        else:
            return morseConverterPerWord(word)
    else:
        temps = []
        for w in splitted:
            if w in de.ListOfSpecialMarksval:
                temps.append(specialConverter2(w))
            else:
                temps.append(morseConverterPerWord(w))
        return " ".join(temps)
