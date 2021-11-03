'''
Author: Reid Dye

A ISBN checker
run test.sh to test, you might have to chmod +x it
You also might have to replace the python path with your python path

'''

class Check():
    #muahahahaha
    #functions are allowed now
    #sorry, I mean methods are great
    def Valid(self, num): #a method to check if a number is valid
        num=list(num)#make it into a list of a digits, to make it mutable, and make it able to have multi-digit digits
        
        #get rid of x at the end if needed
        if num[-1].upper()=='X':
            num[-1]='10'
        
        #check each char
        for i in num:
            if not(i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0' or i=='10'):
                return False #return ends the function, so on the first invalid char, it just exits with False
        num=num[::-1] #so index is in same direction as coefficient in the formula
        total=0 #accumulator thing
        
        for i in range(len(num)): #for each character...
            total+=int(num[i])*(i+1) #multiply by the coef, which is i+1 because we reversed the direction of num
        if total%11==0:#check if output of multiplication and sum is divisible by 11
            return True
        return False

check=Check() #create checker object

#get file names
file=input('ISBN numbers filename: ')
outputFile=input('Output filename: ')

#read the input, then close the file
f=open(file)
lines=f.read().split('\n')
f.close()

#if there's nothing in the file, then just exit
if lines==['']:
    print('File is empty! Exiting.')
    exit() #do this before opening outFile to avoid overwriting it when not necesary


#open the output file
outFile=open(outputFile, 'w')


#*Section: remove comments and empty lines
numbers=[]
for l in lines:#for each line in the input
    if l=='': #if it's a blank line
        pass
    elif l[0]==';': #if it's a comment
        pass
    else:
        numbers.append(l) #add to the possible numbers!

#init lists
valid=[]
invalid=[]

#for each possible number, check its validity and append it to the right list
for n in numbers:
    if check.Valid(n):
        valid.append(n)
    else:
        invalid.append(n)

#print all the valid stuff plus title
print('Valid ISBNs: ', file=outFile)
for i in valid:
    print(i, file=outFile)

#print invalid title
print('\nInvalid ISBNs: ', file=outFile)


#figure out what the reason was for each invalid and print it
for i in invalid:
    reason='Formula did not work; output not divisible by 11.'
    for j in i:
        if not(j=='0' or j=='1' or j=='2' or j=='3' or j=='4' or j=='5' or j=='6' or j=='7' or j=='8' or j=='9' or j=='0' or j=='10'):
            reason='Invalid character'
    if len(i)!= 10:
        reason='Wrong length'
    
    print(i+', reason: '+reason, file=outFile)

#close the file
outFile.close()