class UnionFind():
    
    def __init__(self,n):
        # classの初期化 大きさnのグループを作る
        self.n = n
        #0~n-1の要素がありすべての要素の親は-1
        self.parents = [-1] * n
        
    def find(self, x):
        #xがどこにいるかを探している
        #親だったら自分を子だったら親を返す
        if self.parents[x] == -1:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        #要素xとyを結合する
        #xとyの親を探す
        x = self.find(x)
        y = self.find(y)
        if x == y:
            #親が同じだったらそのまま
            return
        if self.parents[x] > self.parents[y]:
            x,y = y,x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        #xが含まれるunionのサイズ
        return -self.parents[self.find(x)]
    
    def same(self, x, y):
        #xとyが同じunionであるかの判定
        return self.find(x) == self.find(y)
    
    def members(self, x):
        #xが含まれるunionのメンバー
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    def roots(self):
        #親の集合
        return [i for i, x in enumerate(self.parents) if x < 0]
    
    def group_count(self):
        #unionの数
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
