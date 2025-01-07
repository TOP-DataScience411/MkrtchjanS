def tree_leaves(branches):
    """Считает количество листьев в дереве, представленном вложенными списками"""
    count = 0
    for branch in branches:
        if branch == 'leaf':
            count += 1
        elif isinstance(branch, list):
            count += tree_leaves(branch)
            
    return count

    
tree = [[[['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']], [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf'], ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']]
print(tree_leaves(tree))  # 38
