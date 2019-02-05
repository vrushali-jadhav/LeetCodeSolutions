
######### This problem is solved using dynamic programming #########
import numpy as np

def longestPalindrome(stringToAnalise):
    longestString = ""
    length = len(stringToAnalise)
    maxlength = 0
    startingIndex = 0
    traverseLength = 1
    
    #IMPORTANT: This is how you build a DS similar to 2 d array. The other way is to use numpy matrix.
    store = [[False for x in range(length)] for y in range(length)]
    print(store)
    #if emtpy string
    if not stringToAnalise:
        return None

    #for string length 1: set all the values to 1.
    i = 0
    while i <= length-1:
        store[i][i] = True
        i+=1
    maxlength = 1
    startingIndex = i
    
    #for strings with length 2
    i=0
    startingIndex = 0
    while i<= length-2:
        if stringToAnalise[i] == stringToAnalise[i+1]:
            store[i][i+1] = True
            maxlength = 2
            startingIndex = i
            traverseLength = 2
        i=i+1        
    
    print("max: {0}".format(maxlength))
    #for strings with length greater than 2
    traverseLength = 3 
    while traverseLength <= length:
        i=0
        while i<=(length - traverseLength):
            j= i+traverseLength-1 
            if store[i+1][j-1] and stringToAnalise[i] == stringToAnalise[j]:
                store[i][j]=True
                
                if traverseLength>maxlength:
                    startingIndex = i
                    maxlength = traverseLength   
            i = i+1
        traverseLength = traverseLength+1

    #print(store)
    return stringToAnalise[startingIndex:(maxlength+startingIndex)]

stringToAnalise = "aaaa"
print("Longest palindrome is: {0}".format(longestPalindrome(stringToAnalise)))