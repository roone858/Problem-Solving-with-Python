x=int(input())
result=[]
total = 0
for i in range(x):
    m,w,k,p= [int(x) for x in input().split()[slice(4)]] 
    total=0
    if k>m:
        total=-1
    elif k==m:
        total=m+w
    else :
        rm=m-k
        w=w-rm
        total = m+w
            
    if total > p :
        result.append(f"NO 'we gonna die' we need {total} to servive")
    else:
        result.append(f"YES 'we need {total} p to servive'")
        
[print(x) for x in result]
    
