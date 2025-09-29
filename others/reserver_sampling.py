import random

def reservoir(stream, k=3):
    R=[]; it=0
    for x in stream:
        it+=1
        if len(R)<k: R.append(x)
        else:
            j=random.randint(1,it)
            if j<=k: R[j-1]=x
    return R

print(reservoir(range(1,101), k=5))