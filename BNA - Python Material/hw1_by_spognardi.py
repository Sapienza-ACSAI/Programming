# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:27:27 2022

@author: Studente
"""
def ex1(seq, subtotal):
    seq = list(map(int, seq.split(',')))
    
    i, j, counter = 0, 0, 0
    
    for i in range(len(seq)):
        for j in range (i, len(seq)):
            if sum(seq[i:j+1]) == subtotal:
                counter += 1
    return counter


def ex1b(seq, subtotal):
    seq = list(map(int, seq.split(',')))
    
    i, j, counter = 0, 0, 0
    
    for i in range(len(seq)):
        for j in range (i, len(seq)):
            s = sum(seq[i:j+1])
            if s ==subtotal:
                counter += 1
            elif s > subtotal:
                break
    return counter


def ex1p(seq, subtot):
    seq = list(map(int, seq.split(',')))
    
    partial = seq[0]
    i, j, counter = 0, 0, 0
    
    if partial == subtot:
        counter += 1
#        print(seq[i:j+1])
   
    j, partial, counter = move_j_fw(seq, i, j, partial, subtot, counter)
    j, partial = move_j_bw(seq, j, partial, subtot)
    for i in range(len(seq)):
        partial -= seq[i]
        if partial == subtot:
            counter += 1
#            print("ex", seq[i+1:j+1])
        j, partial, counter = move_j_fw(seq, i+1, j, partial, subtot, counter)
        j, partial = move_j_bw(seq, j, partial, subtot)
    return counter
    
def move_j_fw(seq, i, j, partial, subtot, counter):
    while partial <= subtot and j < len(seq)-1:
        j += 1
        partial += seq[j]
        if partial == subtot:
            counter += 1
#            print("fw", seq[i:j+1])
    return j, partial, counter
    
            
def move_j_bw(seq, j, partial, subtot):    
    while partial >= subtot:
        partial -= seq[j]
        j -= 1
        
    return j, partial
        
        
        
        
        
        
        
        
        
        
    