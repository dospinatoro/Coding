# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 12:17:12 2021

@author: dany9
"""

import sys
import math

def supDigits(ed,digitos):
    #print(digitos,":")
    aux=1;
    tdig=0;
    while aux<=digitos:
        if aux==1:
            tdig+=10
        else:
            tdig=tdig+(9*(10**(aux-1))*aux)
     #   print(tdig,"*")
        aux+=1
    tdig=tdig-((10**(digitos)-ed-1))*(digitos)
    #print(tdig," ",digitos)
    return tdig

def infDigits(st,tdig,digitos):
    #print(digitos,":s")
    aux=1;
    aux1=0;
    while aux<=digitos-1:
        if aux==1:
            aux1-=10;
        else:
            aux1-=(9*(10**(aux-1))*aux)
        aux+=1;
    tdig=tdig-(st*digitos-aux1)
    #print(tdig,"##")
    return tdig;

def division(st,tdig):
    tdig=int(tdig/2);
    dig=len(str(st))
    aux=st-1;
    while tdig>=dig:
        if aux<10**(dig)-1:
            tdig=tdig-1*dig;
            aux=aux+1
        else:
            dig=dig+1
        #print("Resp: ",aux," ",tdig)
    #print(digitos,"((((")
    return aux
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    st, ed = [int(j) for j in input().split()]
    #print(st," ",ed)
    digitos=len(str(ed));
    tdig=supDigits(ed,digitos)
    digitos=len(str(st));
    tdig=infDigits(st,tdig,digitos)
    aux=division(st,tdig)
    print(aux)