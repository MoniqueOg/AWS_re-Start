#Protein sequence of human insulin

import re

result = ""

with open("preproinsulin-seq-clean.txt",'r') as f:
    text = f.read()
    nospace = re.sub("\s", "", text)
    noOr = re.sub("ORIGIN", "", nospace)
    noSlash = re.sub("\/\/","",noOr)
    noNum = re.sub("[0-9]*","", noSlash)
    result = noNum
    
print("The cleaned file has: ", len(result), "characters")
    
with open("lsinsulin-seq-clean.txt", 'x') as file:
    file.write(result[0:24])
    print(result[0:24])
    print("lsinsulin-seq-clean.txt has: ", len(result[1:24]), "characters")
    
with open("binsulin-seq-clean.txt", 'x') as file:
    file.write(result[24:54])
    print(result[24:54])
    print("binsulin-seq-clean.txt has: ", len(result[24:54]), "characters")
    
with open("cinsulin-seq-clean.txt", 'x') as file:
    file.write(result[54:89])
    print(result[54:89])
    print("cinsulin-seq-clean.txt has: ", len(result[54:89]), "characters")
    
with open("ainsulin-seq-clean.txt", 'x') as file:
    file.write(result[89:110])
    print(result[89:110])
    print("ainsulin-seq-clean.txt", len(result[89:110]), "characters")