import time
import matplotlib.pyplot as plt
def minmax(low,high):
    if high-low<=1:
        return (max(arr[low],arr[high]),min(arr[low],arr[high]))
    else:
        max1, min1= minmax(low,int((low+high)/2))
        max2, min2= minmax((int((low+high)/2))+1,high)
    return max(max1,max2), min(min1,min2)

print("Minimum and Maximum")
sizes=[]
times=[]
n=int(input("enter the number of times you want to run: "))
for i in range(0,n):
    m=int(input("enter the number of array elements: "))
    sizes.append(m)
    arr=[]
    for j in range(0,m):
        temp=int(input())
        arr.append(temp)
    starttime=time.perf_counter()
    res=minmax(0 , len(arr)-1)
    endtime=time.perf_counter()
    finaltime=endtime-starttime
    times.append(finaltime)
    print(res)

plt.plot(sizes, times)
plt.ylabel("time taken")
plt.xlabel("size of arrays")
plt.show()
plt.savefig('minmax.png')