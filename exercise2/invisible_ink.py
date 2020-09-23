import sys
import binaryconv as bc

def txt2bin(txt):
    bin = []
    for c in txt:
        bin.append(bc.padzero(bc.dec2bin(ord(c)),8))
    return "".join(bin)

def bin2invisible(bin):
    inv = []
    for b in bin:
        if b=='0':
            inv.append(' ')
        else:
            inv.append('\t')
    return "".join(inv)

def txt2invisible(txt):
    return bin2invisible(txt2bin(txt))

def invisible2bin(inv):
    #' ' = 0, \t = 1
    bin = []
    for i in inv:
        if i == ' ':
            bin.append('0')
        else:
            bin.append('1')
    return "".join(bin)

def bin2txt(bin):
    txt = []
    n = 0
    while n < len(bin):
        txt.append(chr(bc.bin2dec(bin[n:n+8])))
        n +=8
    return "".join(txt)

def invisible2txt(inv):
    return bin2txt(invisible2bin(inv))

def main():
    #Import file
    txt_file = open(sys.argv[2], encoding="utf-8")
    txt = txt_file.read()
    txt_file.close()

    if sys.argv[1] == "encode":
        #Encode file
        e_file = txt2invisible(txt)
        if sys.argv[3]:
            output_file = open(sys.argv[3] , "w")
            output_file.write(e_file)
            output_file.close()
        else:
            print(e_file)

    elif sys.argv[1] == "decode":
        #decode the file f = open("myfile.txt", "x")
        d_file = bin2txt(invisible2bin(txt))
        if sys.argv[3]:
            output_file = open(sys.argv[3] , "w")
            output_file.write(d_file)
            output_file.close()
        else:
            print(d_file)
        
    else:
        return(print("Invalid arguments. Please try again..."))


    
main()
