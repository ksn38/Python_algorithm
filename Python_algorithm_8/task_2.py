'''Закодируйте любую строку по алгоритму Хаффмана.'''

from binarytree import bst

def search(binstree, number, path=''):
    if binstree.value == number:
        return f'число {number} обнаружено по следующему пути:\nroot {path}'

    if number < binstree.value and binstree.left != None:
        return search(binstree.left, number, path=f'{path}\nleft step')

    if number > binstree.value and binstree.right != None:
        return search(binstree.right, number, path=f'{path}\nright step')

    return f'num {number} absent'


bt = bst(height=5, is_perfect=False)
print(bt)
# num = int(input('enter '))
num = 5
print(search(bt, num))