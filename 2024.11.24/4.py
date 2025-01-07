import random

def tree_generator():
    """Генерирует дерево в виде вложенных списков, где каждая ветка может быть либо 'leaf', либо новой ветвью, созданной рекурсивно."""
    tree = []
    branches = random.randrange(0,5)
    
    for i in range(branches):
        if random.choice([True, False]):
            tree.append('leaf')
        else:
            tree.append(tree_generator())
            
        
        if not tree:
            return [['leaf']]
            
    
    return tree
    
    
print(tree_generator()) #['leaf']
print(tree_generator()) #['leaf', [[['leaf', 'leaf', 'leaf', []], ['leaf', 'leaf'], ['leaf']], ['leaf'], 'leaf', 'leaf'], 'leaf', 'leaf']
