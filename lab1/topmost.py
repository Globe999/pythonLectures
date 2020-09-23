import wordfreq as w
import sys
import urllib.request

def main():
    #Add all stopwords to a List
    stop_file = open(sys.argv[1], encoding="utf-8")
    stop_words = []
    for stop in stop_file:
        stop_words.append(stop.strip())
    stop_file.close()

    inp_file = ""
    #Check if file points to local dir or http
    if (str(sys.argv[2]).startswith('http://') or str(sys.argv[2]).startswith('https://')):
        response = urllib.request.urlopen(sys.argv[2])
        inp_file = response.read().decode("utf8").splitlines()
    else:
        local_file = open(sys.argv[2], encoding="utf-8")
        inp_file = local_file.read().splitlines()
        local_file.close()
        
    #Split all words
    t_file = w.tokenize(inp_file)
    #Count words
    countDic = w.countWords(t_file, stop_words)
    #Print top N
    w.printTopMost(countDic, int(sys.argv[3]))
    

main()