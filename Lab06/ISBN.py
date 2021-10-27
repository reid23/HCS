def fakeInput(prompt, userInput):
    print(prompt+userInput)
    return userInput

def checkValid(num):
    num=list(num)
    if num[-1].upper()=='X':
        num[-1]='10'
    for i in num:
        if not(i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0' or i=='10'):
            return False
    num=num[::-1] #so index is in same direction as coefficient
    total=0
    for i in range(len(num)):
        total+=int(num[i])*(i+1)
    if total%11==0:
        return True
    return False

file=input('ISBN numbers filename: ')
#file=fakeInput('ISBN file: ', 'testData')
outputFile=input('Output filename: ')
#outputFile=fakeInput('Output file: ', 'outputData.txt')
outFile=open(outputFile, 'w')
f=open(file)
lines=f.read().split('\n')
f.close()

if lines=='':
    print('File is empty! Exiting.')
    exit()

#*Section: remove comments
numbers=[]
for i in range(len(lines)):
    l=lines[i].split(';')
    if l[0]=='':
        pass
    else:
        numbers.append(l[0])

valid=[]
invalid=[]
for n in numbers:
    if checkValid(n):
        valid.append(n)
    else:
        invalid.append(n)

print('Valid ISBNs: ', file=outFile)
for i in valid:
    print(i, file=outFile)

print('\nInvalid ISBNs: ', file=outFile)


for i in invalid:
    reason='Formula did not work; output not divisible by 11.'
    for j in i:
        if not(j=='0' or j=='1' or j=='2' or j=='3' or j=='4' or j=='5' or j=='6' or j=='7' or j=='8' or j=='9' or j=='0' or j=='10'):
            reason='Invalid character'
    if len(i)!=10:
        reason='Wrong length'
    
    print(i+', reason: '+reason, file=outFile)


outFile.close()