s1=str(input())
s2=str(input())
s1,s2=list(s1),list(s2)
total_len=len(s1)+len(s2)
count=0
for i in s1:
    if i in s2:
        s2.remove(i)
        count+=1
total_len-=count*2
total_len=5
lst1=["f","l","a","m","e","s"]
while len(lst1)!=1:
    lst_emp=[]
    total_len=total_len%len(lst1)
    for i in range(total_len,len(lst1)+total_len-1):
        lst_emp.append(lst1[i%len(lst1)])
    lst1=lst_emp
print(*lst1)   

