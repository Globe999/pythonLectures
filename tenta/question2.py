def code_words(text, dictionary):
    strList = text.split()
    newList = []
    for i in strList:
        if i in dictionary:
            newList.append(dictionary[i])
        else:
            newList.append(i)
    return " ".join(newList)