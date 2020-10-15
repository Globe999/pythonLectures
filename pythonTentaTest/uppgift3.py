class Tree:    
    def __init__(self,node,trees):
        self.root = node
        self.subtrees = trees
    def getParts(self):
        return self.root, self.subtrees


royal = Tree("CarlGustaf", [Tree("Victoria", ["Estelle"])])