
import os

def quartiles(arr,n):
    arr.sort()
    q1=n//4 
    q2=n//2
    q3=int(n*0.75)
    if n%4==0:
        fq=(arr[q1]+arr[q1-1])//2
        sq=(arr[q2]+arr[q2-1])//2
        tq=(arr[q3]+arr[q3-1])//2
    elif n%2==0:
        fq=(arr[q1])
        sq=(arr[q2]+arr[q2-1])//2
        tq=(arr[q3])
    else:
        fq=(arr[q1]+arr[q1-1])//2
        sq=(arr[q2])
        tq=(arr[q3]+arr[q3+1])//2
    return [fq,sq,tq]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data,n)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
