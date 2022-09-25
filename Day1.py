
import math

def stdDev(n,arr):
    mean=sum(arr)/n
    s=0
    for i in range(n):
        s+=(arr[i]-mean)**2
    sd=math.sqrt(s/n)
    print(round(sd,1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(n,vals)
