"""Закодируйте любую строку по алгоритму Хаффмана."""

from collections import Counter


def assign_code(nodes, label, result, prefix=''):
    childs = nodes[label]
    tree = {}
    if len(childs) == 2:
        tree['0'] = assign_code(nodes, childs[0], result, prefix + '0')
        tree['1'] = assign_code(nodes, childs[1], result, prefix + '1')
        return tree
    else:
        result[label] = prefix
        return label


def Huffman_code(_vals):
    vals = _vals.copy()
    nodes = {}
    for n in vals.keys():
        nodes[n] = []

    while len(vals) > 1:
        s_vals = sorted(vals.items(), key=lambda x: x[1])
        a1 = s_vals[0][0]
        a2 = s_vals[1][0]
        vals[a1 + a2] = vals.pop(a1) + vals.pop(a2)
        nodes[a1 + a2] = [a1, a2]
    code = {}
    root = a1 + a2
    # print('nodes', nodes)
    tree = {}
    tree = assign_code(nodes, root, code)
    return code, tree


text = 'aaabbcddef'
print('Text:', text)

vals = Counter(text)
code, tree = Huffman_code(vals)

encoded = ''.join([code[t] for t in text])
print('Encoded text:', encoded)