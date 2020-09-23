def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            while line[start].isspace():
                start += 1
                #Check if we reached end of line, if so break from loop
                if start >= len(line):
                    break
            end = start
            #Check if we reached end of line, if so break from loop
            if start >= len(line):
                break
            #Check characters
            if line[start].isalpha():
                while end < len(line) and line[end].isalpha():
                    end += 1
                words.append(line[start:end].lower())
            #Check numbers 
            elif line[start].isdigit():
                while end < len(line) and line[end].isdigit():
                    end+= 1
                words.append(line[start:end])
            else:
                words.append(line[start])
                end += 1
            start = end
    return words

def countWords(words, stopWords):
    wordDic = {}
    for word in words:
        if word not in stopWords:
            if word not in wordDic:
                wordDic[word] = 1
            else:
                wordDic[word] = wordDic.get(word) + 1
    return wordDic

def printTopMost(frequencies, n):
    #Först sortera listan
    srt = sorted(frequencies.items(), key = lambda x: -x[1])[:n]
    for word, s in srt:
        print(word.ljust(20) + str(s).rjust(5))