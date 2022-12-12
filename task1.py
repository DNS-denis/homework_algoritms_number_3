'''
Сложность O(n)
'''
def isPalindrome(self, head):
    lst = []
    while head:               # если входной список head не пустой, то мы добавляем в созданный нами список значение из head
        lst.append(head.val)
        head = head.next      # затем берём след. элемент из head и так далее
    if lst == lst[::-1]:      # если наш конечный список равен ему же перевёрнутому, то он палиндромен, в остальных случаях нет
        return True
    return False