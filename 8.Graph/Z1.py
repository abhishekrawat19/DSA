class Queue:
    def __init__(self):
        self.front=-1
        self.q=[]

    def push(self,k):
        if self.front==-1:
            self.front=0
        self.q.append(k)
    def pop(self):
        if len(self.q) == 0:
            return -1
        x=self.q[self.front]
        self.front+=1
    
        if len(self.q)==self.front:
            self.q=[]
            self.front=-1

        return x
    
    def getfront(self):
        return self.q[self.front]
    
    def size(self):
        return len(self.q)-self.front
    


class Soultion:
    q=Queue()

    ans=[]
    indegree=[0]*n
    adjlist=[]

    for i in range(n):
        adjlist.append([])

    for a,b in prerequisites:
        # b--> a
        indegree[a]+=1
        adjlist[b].append(a)

    for i in range(n):
        if indegree(i)==0:
            ans.append(i)
            q.push(i)

    while q.size()>0:
        front=q.pop()

        for x in adjlist[front]:
            indegree[x]-=1
            if indegree(x)==0:
                ans.append(i)
                q.push(i)



