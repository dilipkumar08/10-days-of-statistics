import statistics
n=int(input())
l=list(map(int,input().split()))[0:n]
l.sort()
print(round(statistics.mean(l),1))
#manual method for mean
'''
mean=round(sum(l)/n,1)
print(mean)'''
print(round(statistics.median(l),1))
#manual method for median
'''if n%2==0:
    median=round((l[(n//2)]+l[(n//2)-1])/2,1)
else:
    median=l[n//2]
print(median)'''
print(round(statistics.mode(sorted(l)),1))
