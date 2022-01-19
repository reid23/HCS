'''
Author: Reid Dye

This file contains my answers for test 3.
'''

#%%
#* ========== Prob 01 ==========

def collatz(start: int):
    vals = [start]
    while vals[-1] != 1: #while most recent value isn't 1
        if vals[-1] % 2 == 0: #even case
            vals.append(int(vals[-1] * 0.5))
        else:                 #odd case
            vals.append(int((vals[-1] * 3)+1))
    return vals
        
# %%
#* ========== Prob 02 ==========


def dayOfYear(month, day):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    valid=''

    try:
        dayYear = sum(months[:month-1])+day
        #now to make it throw an error if the day is wrong, because we have to use a try:except to catch the error
        if day>months[month-1]: a=[][0] #doesn't catch if day is 0, but we're assuming input is positive int
    except IndexError:
        dayYear = -1
        valid = 'The numbers entered do not represent a valid date.'
    return dayYear, valid

# %%
#* ========== Prob 03 ==========

def computeGPA():
    allowedGrades=['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']
    file=input('file with grades: ')
    grades=[]
    with open(file, 'r') as f: #to prevent not closing files if theres an exception
        for line in f:
            capLine=line.upper()[:-1] #remove newline char, make always capital
            if not (capLine in allowedGrades): continue #input validation, just in case
            
            grade = 69-ord(capLine[0]) #convert letter to number
            
            if '+' in capLine:
                grade+=0.3
            elif '-' in capLine:
                grade-=0.3
            print(capLine, grade)
            grades.append(grade)
    try:
        return round(sum(grades)/len(grades), 2)
    except ZeroDivisionError:
        return -1.0 #no valid grades or empty file
# %%
