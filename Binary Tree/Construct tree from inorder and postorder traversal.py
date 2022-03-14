class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution:
    def buildTree(self, inorder, postorder):
        def helper(in_left, in_right):
            # if there is no elements to construct subtrees
            if in_left > in_right:
                return None

            # pick up the last element as a root
            val = postorder.pop()
            root = Node(val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[val]

            # build right subtree
            root.right = helper(index + 1, in_right)
            # build left subtree
            root.left = helper(in_left, index - 1)
            return root

        # build a hashmap value -> its index
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)

obj=Solution()
print (obj.buildTree([9,3,15,20,7],[9,15,7,20,3]))