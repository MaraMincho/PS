import collections
# def solution(nodeinfo):
#     td = {}
#     for key, (ind, depth) in enumerate(nodeinfo) :
#         td[depth] = td.get(depth, []) + [(key + 1, depth, ind)]
    
#     std = sorted(td.items(), key= lambda x: [x[0]]) [::-1]
#     td = {}
#     for ind in range(len(std)) :
#         depth, val = std[ind]
#         td[depth] = sorted(val, key = lambda x: x[2])
#     tree = {}
#     visited = collections.defaultdict(bool)
#     maxDepth = max(set(list(map(lambda x: x[1], nodeinfo))))
    
#     def dfs(minVal, maxVal, depth) :
#         if depth <= 0 :
#             return []
#         if not td.get(depth) :
#             return dfs(minVal, maxVal, depth - 1)
        
#         val = td[depth]
#         # print(depth, minVal, maxVal, val)
#         for (key, row, col) in val :
#             if visited[(row, col)] :
#                 continue
#             if minVal < col < maxVal :
#                 visited[(row, col)] = True
#                 # 왼쪽
#                 leftDfs = []
#                 rightDfs = []
#                 curDepth = depth - 1
#                 while curDepth > 0 and not leftDfs:
#                     leftDfs = dfs(minVal, col, curDepth)
#                     curDepth -= 1
#                 # 오른쪽
#                 curDepth = depth - 1
#                 while curDepth > 0 and not rightDfs :
#                     rightDfs = dfs(col, maxVal, curDepth)
#                     curDepth -= 1
#                 tree[key] = (leftDfs, rightDfs)
#                 return key
#         return []
        
#     dfs(-1, 100_000_000, maxDepth)
#     print(tree)
    
#     fr = []
#     def fn(curV) :
#         fr.append(curV)
#         (leftV, rightV) = tree[curV]
#         if leftV != []:
#             fn(leftV)
#         if rightV != []:
#             fn(rightV)
    
#     br = []
#     def bn(curV):
#         (leftV, rightV) = tree[curV]
#         if leftV != []:
#             bn(leftV)
#         if rightV != []:
#             bn(rightV)
#         br.append(curV)
#     root = td[maxDepth][0][0]
#     fn(root)
#     bn(root)

    
#     return [fr, br]
# solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	)

def solution(nodeinfo):
    board = []
    for key, (x, y) in enumerate(nodeinfo) :
        board.append((x, y, key))
        
    # (x, y, key)
    board.sort()
    mdv = max(board, key=lambda x: x[1])
    
    tree = {}
    def sp(node: list) :
        print("myNode", node)
        if len(node) == 1 :
            return node[0]
        elif len(node) == 0 :
            return None
        ind = node.index(max(node, key=lambda x: x[1]))
        print(node[:ind], node[ind + 1 :])
        tree[node] = (sp(node[:ind]), sp(node[ind + 1 :]))
        return node[ind][2]
    sp(board)
    print(tree)
        
solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	)