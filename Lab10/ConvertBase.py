from math import log, floor
import sys
def cvtr(num: str|int, cur: int, end: int, place: int =-1):

    if cur != 10: #convert to base 10 on first recursion
        newNum=[]
        num=list(num)
        for counter, i in enumerate(num):
            if i in 'abcdef':
                num[counter]=ord(i)-87
            else:
                num[counter]=int(i)
        num = num[::-1]
        for counter, i in enumerate(num):
            newNum.append(i*(cur**counter))
        num=sum(newNum)
        cur=10

    if place==0:
        return str(num)
    if place==-1:
        place = floor((log(num, end)))

    digit = num//(end**place)
    remainder = num%(end**place)
    return str(digit) + cvtr(remainder, cur, end, place-1)

def error(reason):
    print('\nError:', reason, '\n')


# if len(sys.argv)>1:
#     pass #arguments
def main():
    print('Welcome to the base conversion program! If you would like to quit this program, use C-d (like standard python shells).\n')
    while True:
        try:
            start = input('Source Base: ')
            num = input('Source Number: ')
            end = input('Destination Base: ')
        except EOFError:
            while True:
                inString = input('\nAre you sure you want to quit [y/n]? ')
                if 'y' in inString: 
                    exit()
                elif 'n' in inString:
                    break #go back to getting new numbers
                else:
                    pass
            continue

        chars = '0123456789abcdef'

        try:
            for i in start:
                assert 48<=ord(i)<=57, f'Expected base 10 number for starting base but received {start}' # make sure all chars are digits (no decimals or letters)
            for i in end:
                assert 48<=ord(i)<=57, f'Expected base 10 number for destination base but received {end}' # same thing
            start=int(start)
            end=int(end)

            assert 2<=start<=16, f'Expected starting base in [2, 16] but received {start}'
            assert 2<=end<=16, f'Expected destination base in [2, 16] but received {end}'

            num=num.lower()
            numList=list(num)
            for char in numList:
                assert char in chars[:start], f'Expected positive integer source number in base {start} but received {num}'
        except AssertionError as e:
            error(e)
            continue

        print(f'\nNEW NUMBER: {cvtr(num, start, end)}\n')


if __name__ == '__main__': main()
