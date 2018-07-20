
def findProfession(level, pos):
    seen = {}
    depth = 1
    root = (Tree('Engineer'), depth)
    marked = set()
    q = [root] #queue
    while q:
        if depth > level+1:
            break
        current, depth = q.pop(0)
        if current not in marked and depth <= level:
            if depth in seen:
                seen[depth].append(current.value)
            else:
                seen[depth] = [current.value]
        if current.value == 'Engineer':
            current.left = Tree('Engineer')
            current.right = Tree('Doctor')
        else:
            current.left = Tree('Doctor')
            current.right = Tree('Engineer')
        marked.add(current)
        depth += 1
    
        q.append((current.left, depth))
        q.append((current.right, depth))
    return seen[level][pos-1]

pp.pprint(findProfession(1,1))
