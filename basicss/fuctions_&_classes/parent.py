class fruit:
    def __init__(self,name,size,flavour='sweet',color='red'):
        self.size = size
        self.name = name
        self.flavour = flavour
        self.color = color
        self.shape = shape
    
    def show(self):
        print('Name:',self.name)
        print('Shape:',self.shape)
        print('Color:',self.color)
        print('Size:',self.size)
        print('Flavour:',self.flavour)

if __name__ == "__main__":
    a1 = fruit('apple','small','pear-shape')
    a2 = f  ruit('orange','small','round',color='orange')
    a1.show()
    a2.show()
00000