class node:
    def __init__(self,data,level,fval):
        """初始化结点、层数、f值"""
        self.data = data
        self.level = level
        self.fval = fval

    def find(self,puz,x):
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if puz[i][j] == x:
                    return i,j

    def copy(self,root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp
                
    def move(self,puz,x1,y1,x2,y2):
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        
        else:
            return None
                
    def gen_chi(self):
        """生成子节点"""
        x,y = self.find(self.data,'_')
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            child = self.move(self.data,x,y,i[0],i[1])
            if child is not None:
                child_node = node(child,self.level+1,0)
                children.append(child_node)
        return children
def to_1d(l):
    a = []
    for i in range(0,len(l)):
        for j in l[i]:
            if j != "_":
                a.append(int(j))
            else: a.append(len(l) * len(l))
    return a
def reverse_num(l):
    n = 0
    for i in range(0,len(l)-1):
        for j in range(i,len(l)):
            if l[i] > l[j]:
                n += 1
    return n
class puzzle():
    def __init__(self,size):
        self.n = size
        self.open = []
        self.closed = []

    def inputs(self):
        puz = []
        for i in range(0,self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz
    
    def f(self,start,goal):
        return self.h(start.data,goal) + start.level

    def h(self,start,goal):
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp
    
    def process(self):
        print("Please input the start matrix: \n")
        start = self.inputs()
        print("Please input the goal matrix: \n")
        goal = self.inputs()
        
        a_1 = to_1d(start)
        b_1 = reverse_num(a_1) % 2
        a_2 = to_1d(goal)
        b_2 = reverse_num(a_2) % 2
        

        if (b_1 != b_2):
            print("There is no solution!")
        else:
            start = node(start,0,0)
            start.fval = self.f(start,goal)
            self.open.append(start)
            print("\n")

            while True:
                cur = self.open[0]
                print(" \t |")
                print(" \t | ")
                print(" \t\|/ \n")

                print("_" * ((self.n + 1) * 8 + 1))
                for i in cur.data:
                    print("|",end = "\t")
                    for j in i:
                        print(j,end = "\t")
                    print("|")
                print("¯" * ((self.n + 1) * 8 + 1))
                print("\t(\__/) ||")
                print("\t(^ω^) ||")
                print("\t/    ╯")
                if(self.h(cur.data,goal) == 0):
                    break
                for i in cur.gen_chi():
                    i.fval = self.f(i,goal)
                    self.open.append(i)
                self.closed.append(cur)
                del self.open[0]

                #sort the opne list based on f value 
                self.open.sort(key = lambda x:x.fval,reverse=False)
 

puz = puzzle(4)
puz.process()
        
