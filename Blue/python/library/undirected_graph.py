for _ in range():
    #辺をgraghに追加
    a,b = map(int,input().split())
    #インデックスのため-1
    a = a - 1
    b = b - 1
    """
    頂点aからb,bからaへのパスを追加
    フォーマットは[[b],[a,c,d]]のようになる
    """
    gragh[a].append(b)
    gragh[b].append(a)