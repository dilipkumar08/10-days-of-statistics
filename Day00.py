def weightedMean(X, W,n):
    s=0
    for i in range(n):
        s+=X[i]*W[i]
    
    print(round(s/sum(W),1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights,n)
