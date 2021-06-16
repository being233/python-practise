import random
class Poke():
    SUIT=['♣','♦','♥','♠']
    RANK=list('3456789')
    RANK.append('10')
    RANK.extend(list('JQKA2'))
    poker=[]
    NUM=[]
    gamer1=[]
    gamer2=[]
    gamer3=[]
    gamer_1=[]
    gamer_2=[]
    gamer_3=[]
    HIDE=[]
    HIDE_1=[]
    #def __init__(self):
    for r in RANK:
        for s in SUIT:
            poker.append(r+s+' ')
    poker.append('♛ ')
    poker.append('♚ ')
            #装牌
    def wash(self):
        for i in range(0,len(self.poker)):
            self.NUM.append(i)      
        random.shuffle(self.NUM)
            #开启一个牌堆并洗牌
    def deal(self):
        self.HIDE=random.sample(self.NUM,3)
        for i in range(0,len(self.HIDE)):
            if self.HIDE[i] in self.NUM:
                self.NUM.remove(self.HIDE[i])
            #从牌堆中移除底牌       
        for i in range(0,int(len(self.NUM)/3)):
            self.gamer1.append(self.NUM.pop())
            self.gamer2.append(self.NUM.pop())
            self.gamer3.append(self.NUM.pop())
            #将剩下的牌分给三位玩家
    def sort_(self):
            for i in range(1, len(self.gamer1)):
                for j in range(0, len(self.gamer1)-i):
                    if self.gamer1[j] > self.gamer1[j+1]:
                        self.gamer1[j] , self.gamer1[j+1] = self.gamer1[j+1], self.gamer1[j]
            for i in range(1, len(self.gamer2)):
                for j in range(0, len(self.gamer2)-i):
                    if self.gamer2[j] > self.gamer2[j+1]:
                        self.gamer2[j] , self.gamer2[j+1] = self.gamer2[j+1], self.gamer2[j]
            for i in range(1, len(self.gamer3)):
                for j in range(0, len(self.gamer3)-i):
                    if self.gamer3[j] > self.gamer3[j+1]:
                        self.gamer3[j] , self.gamer3[j+1] = self.gamer3[j+1], self.gamer3[j]
            #将三位玩家的牌分别排序
    def show(self):
        for i in range(0,int(len(self.gamer1))):
            self.gamer_1.append(self.poker[self.gamer1[i]])
        for i in range(0,int(len(self.gamer2))):
            self.gamer_2.append(self.poker[self.gamer2[i]])
        for i in range(0,int(len(self.gamer3))):
            self.gamer_3.append(self.poker[self.gamer3[i]])
        for i in range(0,len(self.HIDE)):
            self.HIDE_1.append(self.poker[self.HIDE[i]])
        print('玩家1的手牌为',end=' ')
        for i in range(0,len(self.gamer_1)):
            print(self.gamer_1[i],end='')
        print('')
        print('玩家2的手牌为',end=' ')
        for i in range(0,len(self.gamer_2)):
            print(self.gamer_2[i],end='')
        print('')
        print('玩家3的手牌为',end=' ')
        for i in range(0,len(self.gamer_3)):
            print(self.gamer_3[i],end='') 
        print('')   
        print('剩余的三张底牌为',end=' ')
        for i in range(0,len(self.HIDE)):
            print(self.HIDE_1[i],end='')
            #显示所有玩家牌面
def main():        
    poke1=Poke()
    print(poke1.poker)
    poke1.wash()
    poke1.deal()
    poke1.sort_()
    poke1.show()
main()








