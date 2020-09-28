def pepLineLength(file):
    f = open(file, encoding="utf8")
    lines = f.readlines()
    f.close()
    maxLen = 79
    counter = 0
    for i in lines:
        if len(i) > maxLen:
            print("line " +  str(lines.index(i) + 1) + " too long: " + str(len(i)))
            counter += 1
    if 1 <= counter:
        print(str(counter) + " line(s) were too long out of " + str(len(lines)) + " lines.")
    else:
        print("No lines were too long, good job!")