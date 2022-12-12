'''
Сложность O(log(n))
'''
def averageOfLevels(self, root):
    q, ans = [root], []        # q - queue, ans - answer
    while len(q):
        qlen, row = len(q), 0  # row - строка
        for _ in range(qlen):
            curr = q.pop(0)    # curr(current) - текущий
            row += curr.val
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        ans.append(row/qlen)
    return ans