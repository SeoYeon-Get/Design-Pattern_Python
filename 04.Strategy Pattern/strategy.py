#주의할 점: 'strategy.py' -> Strategy pattern 보다는 로직으로 생각할 것. 
#allUnique 함수는 allUniqueSort 함수와 allUniqueSet 함수를 필요에 따라 각각 상속함.

import time

SLOW = 3                        # in seconds
LIMIT = 5                       # in characters
WARNING = 'too bad, you picked the slow algorithm :('

def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]

def allUniqueSort(s):
   if len(s) > LIMIT:
       print(WARNING)
       time.sleep(SLOW)
   srtStr = sorted(s)
   for (c1, c2) in pairs(srtStr):
       if c1 == c2:
           return False
   return True

def allUniqueSet(s):
    if len(s) < LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    return True if len(set(s)) == len(s) else False # set() : 문자열에 중복된 문자는 제외. 

def allUnique(s, strategy): #allUniqueSet(), allUniqueSort() 두 함수 중 리턴에 해당하는 함수로 이동
    return strategy(s)

def main():
    while True:
        word = None
        while not word:
            word = input('Insert word (type quit to exit)> ')

            if word == 'quit':
                print('bye')
                return

            strategy_picked = None
            strategies = { '1': allUniqueSet, '2': allUniqueSort }
            while strategy_picked not in strategies.keys():
                strategy_picked = input('Choose strategy: [1] Use a set, [2] Sort and pair> ')

                try:
                    strategy = strategies[strategy_picked]
                    print('allUnique({}): {}'.format(word, allUnique(word, strategy)))
                except KeyError as err:
                    print('Incorrect option: {}'.format(strategy_picked))
            print()

if __name__ == '__main__':
    main()
