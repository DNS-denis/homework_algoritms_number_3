'''
Сложность O(1), так как есть список
'''
def getDecimalValue(self, head):
    lst = ""
    while head:                    # если head не пустой, то в созданный нами список добавляем след. значение head в виде строки
        lst = lst + str(head.val)
        head = head.next
    return int(lst, 2)             # с помощью функции int можно перевести любое число в строковом представлении в десятичную СС