class Tree(object):

    def __init__(self, name, parent, size = -1):
        self.name = name
        self.children = []
        self.size = size
        self.parent = id(parent)

    def createChild(self,name, size):
            self.chilrend.append(Tree(name, size))
    
    def count_size(self):
        for element in self.children:
            if element.size<0:
                element.count_size()
            self.size += element.size




with open('Day7_input.txt') as f:
    f.readline()

    #for line in f:
     #   print(line)
      #  break

#%%
A=[1, 2, 3, [4, 5, 6]]
print(id(A))
A[0] = 'a'
print(A)
print(id(A))