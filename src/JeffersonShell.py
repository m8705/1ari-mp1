import  sys     #For debug purposes
import  random
from    collections import Counter

FILEPATH    = "../MP-1ARI.txt"
#FILENL      = 15 #createCylinder(->n)

def     convertLetter(text):
    tmp_str = ""

    for letter in text:
        if letter.isalpha() and ord(letter) <= 123:
            tmp_str += letter
    return (tmp_str.upper())

def     mix():
    buf_str = ""

    while (len(buf_str) < 26):
        buf_char = chr(random.randint(0, 25) + 65)
        if buf_char not in buf_str:
            buf_str += buf_char
    return (buf_str)

def     createCylinder(file, n):
    file_ = open(file, "w")

    for i in range(0, n):
        file_.write(mix() + "\n")
    file_.close()

def     ft_getnewlinesnb(str_):
    count = 0

    for i in range(0, len(str_)):
        if (str_[i] == '\n'):
            count += 1
    return (count)

def     loadCylinder(file):
    content = open(file, "r").read()
    lines_dict = {}
    i = 0
    buf = ""

    for i in range(0, ft_getnewlinesnb(content)):
        for j in range(0, 26):
            buf += content[(i * 27) + j]
        lines_dict[i + 1] = buf
        buf = ""
    return (lines_dict)

def     keyOK(key ,n):
    for i in range(1, n+1):
        if i not in key:
            return (False)
    return (True)

def     createKey(n):
    tmp_str = ""
    while (n != 0):
        tmp_str += str(n)
        n -= 1
    return (''.join(random.sample(tmp_str,len(tmp_str))))

def     find(letter, alphabet):
    for i in range(len(alphabet)):
        if letter == alphabet[i]:
            return (i)

def     shift(i):
    return ((-1), ((i + 6) % 26))[(i <= 25 and i >= 0)]

def     unshift(i):
    return ((-1), ((i - 6) % 26))[(i <= 25 and i >= 0)]

def     cipherLetter(letter, alphabet):
    return (shift(find(letter, alphabet)))

def     uncipherLetter(letter, alphabet):
    return (unshift(find(letter, alphabet)))

def cipherText(cylinder,key,text):
    k = 0
    c = ''

    if len(cylinder) != len(key):
        return('The key is invalid')
    text = convertLetter(text)
    for t in text:
        n = cipherLetter(t,cylinder.get(key[k]))
        c += cylinder.get(key[k])[n]
        k += 1
    return c

def uncipherText(cylinder,key,text):
    k = 0
    c = ''

    if len(cylinder) != len(key):
        return ('The key is invalid')
    text = convertLetter(text)
    for t in text:
        n = uncipherLetter(t, cylinder.get(key[k]))
        c += cylinder.get(key[k])[n]
        k += 1
    return c

#cylinder = loadCylinder(FILEPATH)
#h = 'supinfo'
#key = [7, 4, 19, 13, 17, 18, 12, 15, 16, 10, 11, 2, 5, 20, 9, 8, 1, 14, 6, 3]

#print(cipherText(cylinder,key,h))
