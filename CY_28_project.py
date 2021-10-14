#Session 28
#Sept 26, 2021
def TowerOfHanoi(n,source,destination,auxillary):
    if(n==1):
        print("Move disk 1 from source",source,"to destination",destination)
        return 
    TowerOfHanoi(n-1,source,auxillary,destination)
    print("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1,auxillary,destination,source,)

n=3
TowerOfHanoi(n,"A","B","C")

