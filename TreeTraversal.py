class Node:
    def __init__(self,val=0):
        self.val=val
        self.left = None
        self.right=None

def inorder(root,vals):
    if root is None:
        return
    inorder(root.left,vals)
    vals.append(root.val)
    inorder(root.right,vals)

def dfs(root):
    vals=[]
    q=[root]
    while q!=[]:
        k=q.pop(0)
        if(k.left is not None):
            q.append(k.left)
        if (k.right is not None):
            q.append(k.right)
        vals.append(k.val)

    return vals

def bfs(root):
    vals = []
    stack = [root]
    while stack != []:
        k = stack.pop()
        if (k.left is not None):
            stack.append(k.left)
        if (k.right is not None):
            stack.append(k.right)
        vals.append(k.val)

    return vals


'''   Tree Construction   '''
root=Node(3)
root.left=Node(5)
root.left.left=Node(8)
root.right=Node(1)
root.right.left=Node(55)

''' Tree in order Traversal using Recursion '''
vals=[]
inorder(root,vals)
print(vals)

''' Traversal using DFS and BFS  '''
print(dfs(root))
print(bfs(root))
