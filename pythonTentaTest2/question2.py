def computeKCals(path):
    kCals = {
    "ägg": 137,
    "socker": 405,
    "kött": 155,
    "potatis": 59,
    "vetemjöl": 352,
    "vatten": 0
}
    txt = open(path, encoding="utf-8")
    txtLines = txt.readlines()
    txt.close()

    totalCals = 0

    for i in txtLines:
        l = i.split()
        totalCals += (float(l[0])*float(kCals[l[1]]))
    return totalCals

