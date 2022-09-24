import statistics
n=int(input())
l=list(map(int,input().split()))[0:n]
print(round(statistics.mean(l),1))
print(round(statistics.median(l),1))
print(round(statistics.mode(sorted(l)),1))
