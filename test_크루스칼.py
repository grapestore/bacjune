class DisjointSet:
## 처음에 노드의 개수 만큼 U라는 전역변수 리스트를 만든다
## self에는 dset의 주소값이 저장되어있음, 전역 변수는 각자의 객체에게만 공유된다
## 멤버 변수는 다른 객체에도 값이 공유 된다
## self.변수명을 이용하지 않으면 지역변수로 선언되어 다른 메소드가 호출하지 못한다.
    def __init__(self,n):
        self.U = []        
        for i in range(n):
            self.U.append(i)

## p와 q가 다르면 이것은 연결되어 있지 않은 그래프를 의미한다
    def equal(self,p,q):
        if p == q:
            return True
        else:
            return False

## 본인 index리스트에 저장된 값이 자기 자신이면 이것은 사이클 Graph가 아니다
## 본인 index리스트에 저장된 값에 다른값이 들어 있으면 부모 노드로 이동하며 루트노드 까지 이어진다
    def find(self, i):
        j = i
        while self.U[j] != j:
            j = self.U[j]
        return j

## p,q가 다르면 p or q에 값을 방향을 넣어주어 두개의 그래프를 하나의 그래프로 만들어준다.
    def union(self,p,q):
        if p<q:
            self.U[q] = p
        else:
            self.U[p] = q

## E는 오름차순으로 정렬된 리스트여야 하며[노드번호, 노드번호, 가중치]로 만들어진다.
## 가중치를 기준으로 오름차순이어야 한다.
## n은 노드의 개수이다
def kruskal(n,E):
    F = []
    dset = DisjointSet(n)
    while len(F) < n-1:
        edge = E.pop(0)
        i,j = edge[0], edge[1]
        p = dset.find(i)
        q = dset.find(j)
        if not dset.equal(p,q):
            dset.union(p,q)
            F.append(edge)
    return F

matrix=[
        [0,1,1],
        [2,4,2],
        [0,2,3],
        [1,2,3],
        [2,3,4],
        [3,4,5],
        [1,3,6]
    ]
    
print(kruskal(5,matrix))
