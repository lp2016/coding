def func(root):
    que = [root]
    res = []
    while que:
        next_que, layer = [], []
        for node in que:
            if node:
                layer.append(node.val)
                next_que += [node.left, node.right]
        que = next_que[:]
        if layer:
            res.append(layer[-1])
    return res