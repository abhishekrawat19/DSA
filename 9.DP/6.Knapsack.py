# 0/1 knapsack

def knapsack(i,W,n,Values,weights):
    if i==n:
        return 0
    #take case
    take=0
    if weights[i]<=W:
        take=values[i]+knapsack(i+1,W-weights[i],n,values,weights)
    not_take=knapsack(i+1,W,n,values,weights)

    return max(take,not_take)





n=5
values=[10,5,8,5,3]
weights=[3,2,4,6,4]
W=6


knapsack(0,W,n,values,weights)