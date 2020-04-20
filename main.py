import random

class NumeronBrain():
    def __init__(self):
        #初期化処理
        self.call = [0, 0, 0, 0]
        self.cand = []
        for i in range(10000):
            self.cand.append(list(map(lambda x: (i // (10**(3-x))) % 10, range(4))))

    
    def call_number(self):
        self.call = list(map(lambda x: (random.randint(0,10000) // (10**(3-x))) % 10, range(4)))
        return self.call
    
    def numeron_algorithm(self, eat, bite):
        return 0
        #eat,bite入力からの処理

def main():
    numeron_brain = NumeronBrain()
    while True:
        print(numeron_brain.cand)
        numeron_brain.call_number()
        print("{}{}{}{}".format(numeron_brain.call[0], numeron_brain.call[1], numeron_brain.call[2], numeron_brain.call[3]))
        eat, bite = map(int, input().split())
        numeron_brain.numeron_algorithm(eat, bite)

if __name__ == '__main__':
    main()