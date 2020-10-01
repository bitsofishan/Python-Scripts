import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maxn,minn=scores[0],scores[0]
    count1,count2=0,0
    for i in range(len(scores)):
       if scores[i]<minn:
        minn=scores[i]
        count1+=1
       elif scores[i]>maxn:
        maxn=scores[i]
        count2+=1
    
    return(count2,count1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
