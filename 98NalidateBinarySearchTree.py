# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        pre_order = []

        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            pre_order.append(root.val)
            dfs(root.right)
            return

        dfs(root)

        N = len(pre_order)
        for i in range(1, N):
            if pre_order[i - 1] >= pre_order[i]:
                return False

        return True

class Solution02(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        post_order = []
        def dfs(root):
            if root is None:
                return
            dfs(root.right)
            post_order.append(root.val)
            dfs(root.left)
            return

        dfs(root)
        N = len(post_order)
        for i in range(1, N):
            if post_order[i-1] <= post_order[i]:
                return False
        return True










if __name__ == '__main__':
    solution = Solution()

    node5 =  TreeNode(5)
    node1 = TreeNode(1)
    node4 = TreeNode(4)
    node3 = TreeNode(3)
    node6 = TreeNode(6)

    node5.left = node1
    node5.right = node4
    node4.left = node3
    node4.right = node6

    print(solution.isValidBST(node5))
    solution = Solution02()
    print(solution.isValidBST(node5))



