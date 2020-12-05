class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

# fill tree via reverse post order traversal
def buildtree(h, nums):
    if h == 1:
        return Node(nums.pop())

    node = Node()
    node.val = nums.pop()
    node.right = buildtree(h-1, nums)
    node.left = buildtree(h-1, nums)

    return node

# make a lookup dictionary for root values
def Postorderlookup(root, last=-1):
    if root:
        global look
        look[root.val]=last

        last = root.val
        Postorderlookup(root.left, last) 
        Postorderlookup(root.right, last)

def solution(h,q):
    global look
    look = {}
    nums = list(range(1, 2 ** h))

    tree = buildtree(h, nums)
    Postorderlookup(tree)

    # lookup q input
    ls = []
    for i in q:
        ls.append(look[i])
    
    return ls

print(solution(4, [7, 3, 5, 1]))
print(solution(5, [19, 14, 28]))