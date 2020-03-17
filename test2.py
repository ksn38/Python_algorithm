from collections import Counter


def assign_code(nodes, label, result, prefix=''):
    childs = nodes[label]
    tree = {}
    if len(childs) == 2:
        print('childs', childs)
        tree['0'] = assign_code(nodes, childs[0], result, prefix + '0')
        tree['1'] = assign_code(nodes, childs[1], result, prefix + '1')
        print('tree', tree)
        return tree
    else:
        result[label] = prefix
        return label


def search(binstree, number, path=''):
    if binstree.value == number:
        return f'число {number} обнаружено по следующему пути:\nroot {path}'

    if number < binstree.value and binstree.left != None:
        return search(binstree.left, number, path=f'{path}\n0')

    if number > binstree.value and binstree.right != None:
        return search(binstree.right, number, path=f'{path}\n1')

    return f'num {number} absent'


def Huffman_code(_vals):
    vals = _vals.copy()
    nodes = {}
    for n in vals.keys():  # leafs initialization
        nodes[n] = []

    while len(vals) > 1:  # binary tree creation
        s_vals = sorted(vals.items(), key=lambda x: x[1])
        a1 = s_vals[0][0]
        print('a1', a1)
        a2 = s_vals[1][0]
        print('a2', a2)
        vals[a1 + a2] = vals.pop(a1) + vals.pop(a2)
        nodes[a1 + a2] = [a1, a2]
        print('nodes', nodes)
        print('\n')
    code = {}
    root = a1 + a2
    # print('nodes', nodes)
    tree = {}
    tree = assign_code(nodes, root, code)  # assignment of the code for the given binary tree
    print('code', code)
    return code, tree


text = 'aaabbcddef'  # text to encode

vals = Counter(text)
code, tree = Huffman_code(vals)
print(vals)

encoded = ''.join([code[t] for t in text])
print('Text:', text)
print('Encoded text:', encoded)
