
def morse_code(morse):

# morse = input("Enter an english alphabet digit or punctuation characters to convert to morse code: ")
    morse_dic = {"space":"space",
                    ",":"--..--",
                    "?":"..--..",
                    ".":".-.-.-",
                    "o":"-----","1":".----","2":"..---",
                    "3":"...--","4":"....-","5":".....",
                    "6":"-....","7":"--...","8":"---..",
                    "9":"----.","A":".-","B":"-...","C":"-.-.",
                    "D":"-..","E":".","F":"..-.","G":"--.",
                    "H":"....","I":"..","J":".---","K":"-.-",
                    "L":".-..","M":"--","N":"-.","O":"---",
                    "P":".--.","Q":"--.-","R":".-.","S":"...",
                    "T":"-","U":"..--","V":"...-","W":".--",
                    "X":"-..-","Y":"-.-","Z":"--.."
             
             }
    arr = []
    for element in morse:
        if element.isalpha():
            arr.append(morse_dic[element.upper()])
        else:
            arr.append(morse_dic[element])
    return " ".join(arr)

print(morse_code("a,B,C"))