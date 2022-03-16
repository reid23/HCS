from math import log, floor

def toTen(num: str, cur: int): #for explanation of how the one in cvtr works
    return sum([({
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
            }[char] 
            if char in 'abcdef' 
            else int(char))*(cur**counter) 
                for counter, char in enumerate(num[::-1])])

def toStr(num): return str(num) if num<10 else chr(num-87)

def toTenR(num: str, cur: int):
    digit = ord(num[-1])-87 if num[-1] in 'abcdef' else int(num[-1])
    return digit*(cur**(len(num)-1)) + toTenR(num[:-1], cur) if len(num)>1 else digit
def cvtrBig(num: str|int, cur: int, end: int, place: int = -1):
    if place == -1: 
        num = toTenR(num[::-1], cur)
        place = floor(log(num, end))
    return toStr(num) if place==0 else toStr(num//(end**place)) + cvtrBig(num%(end**place), 10, end, place-1)


def cvtr(num: str|int, cur: int, end: int, place: int =-1): return (lambda num: str(num) if num<10 else chr(num-87))((sum([(ord(char)-87 if char in 'abcdef' else int(char))*(cur**counter) for counter, char in enumerate(num[::-1])]) if isinstance(num, str) else num)) if (place if place != -1 else floor(log((sum([(ord(char)-87 if char in 'abcdef' else int(char))*(cur**counter) for counter, char in enumerate(num[::-1])]) if isinstance(num, str) else num), end)))==0 else (lambda num: str(num) if num<10 else chr(num-87))((sum([(ord(char)-87 if char in 'abcdef' else int(char))*(cur**counter) for counter, char in enumerate(num[::-1])]) if isinstance(num, str) else num)//(end**(place if place != -1 else floor(log((sum([(ord(char)-87 if char in 'abcdef' else int(char))*(cur**counter) for counter, char in enumerate(num[::-1])]) if isinstance(num, str) else num), end))))) + cvtr((sum([(ord(char)-87 if char in 'abcdef' else int(char))*(cur**counter) for counter, char in enumerate(num[::-1])]) if isinstance(num, str) else num)%(end**(place if place != -1 else floor(log((sum([(ord(char)-87 if char in 'abcdef' else int(char))*(cur**counter) for counter, char in enumerate(num[::-1])]) if isinstance(num, str) else num), end)))), 10, end, (place if place != -1 else floor(log((sum([(ord(char)-87 if char in 'abcdef' else int(char))*(cur**counter) for counter, char in enumerate(num[::-1])]) if isinstance(num, str) else num), end)))-1)

def main():
    print('Welcome to the base conversion program! If you would like to quit this program, use C-d (like standard python shells).\n')
    chars = '0123456789abcdef'
    while True:
        try:
            start = input('Source Base: ')
            num = input('Source Number: ')
            end = input('Destination Base: ')
        except EOFError:
            while True:
                inString = input('\nAre you sure you want to quit [y/n]? ')
                if 'y' in inString: exit()
                elif 'n' in inString: break #go back to getting new numbers
                else: pass
            continue

        try:
            for i in start: assert 48<=ord(i)<=57, f'Expected base 10 number for starting base but received {start}' # make sure all chars are digits (no decimals or letters)
            for i in end: assert 48<=ord(i)<=57, f'Expected base 10 number for destination base but received {end}' # same thing
            start, end=int(start), int(end) #convert str to int

            assert 2<=start<=16, f'Expected starting base in [2, 16] but received {start}'
            assert 2<=end<=16, f'Expected destination base in [2, 16] but received {end}'

            numList=list(num.lower())
            for char in numList:
                assert char in chars[:start], f'Expected positive integer source number in base {start} but received {num.lower()}'
        except AssertionError as e:
            print('\nError:', e, '\n')
            continue

        print(f'\nNEW NUMBER: {cvtr(num.lower(), start, end)}\n')


if __name__ == '__main__': main()

# %%
