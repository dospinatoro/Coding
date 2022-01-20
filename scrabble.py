# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 09:33:13 2021

@author: dany9
"""

import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
words=[]
for i in range(n):
    w = input() 
    words.append(w) #Todas las palabras
letters = input() #Letras que se tienen
dicl={e:letters.count(e) for e in set(letters)}
dicl=dict(sorted(dicl.items()))
#Puntaje por cada letra
dic={1:["e","a", "i", "o", "n", "r", "t", "l", "s", "u"], 2:["d","g"], 3:["b","c","m","p"],4:["f", "h", "v", "w", "y"],5:"k",8:["j","x"],10:["q","z"]}
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
candidates=[]
for i in words:
    errores=7-len(i); #Cuenta los errores
    cont=0; r1=0;r2=0;
    dici={e:letters.count(e) for e in set(i)}
    dico={e:i.count(e) for e in set(i)}
    dici=dict(sorted(dici.items()))
    dico=dict(sorted(dico.items()))
    #print(i,"\n",dici,"\n",dico)
    #print(dici.keys(),"\n",dico.keys(),"\n",dici.values(),"\n",dico.values())
    if dici==dico: #Se comparan las letras con la palabra
        candidates.append(i)
#print(words,"\n",letters,"\n",candidates)
if len(candidates)==1:
    print(candidates[0])
else:
    final=0; palabra="";
    for i in candidates:
        puntaje=0;
        for j in i:
            for k in dic.values():
                if j in k:
                    indice=list(dic.keys())[list(dic.values()).index(k)]
                    puntaje=puntaje+int(indice);
                    break;
        if puntaje>final:
            final=puntaje;
            palabra=i;
            #print("%s %d %d" % (palabra,puntaje,final))
    #print(any('a' in val for val in dicl.values()))
    print(palabra);