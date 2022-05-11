name1s="Pavithra"
name2s="Nitheesh kumar"
name1=[]

name1s.lower()
name2s.lower()
for i in name1s:
    name1.append(i)
name2=[]
for i in name2s:
    name2.append(i)
for i in range(0,len(name1)):
    if name1[i] != '*':
        for j in range(0,len(name2)):
            if name2[j] != '*':
                if name1[i] == name2[j]:
                    name1[i]='*'
                    name2[j]='*'
                    break
count=0
for i in name1:
    # print(i)
    if i != '*':
        count+=1
for i in name2:
    # print(i)
    if i != '*':
        count+=1
# print(count)
# count=12
checker=['F','L','A','M','E','S']
ind=0
# cw1=0
# cw2=0
# cf=0
for i in range(6,1,-1):
    # cf+=1
    if ind==len(checker):
        ind-=1
    num=count%i
    if num==0:
        j=1
        # ind+=1
        while(j<i):
            # cw1+=1
            if ind==len(checker)-1:
                ind=0
                j+=1
            else:
                ind+=1
                j+=1
        # print(checker[ind])
        checker.remove(checker[ind])
        if ind==len(checker):
            ind=0
    else:
        l=0
        while(l<num):
            # cw2+=1
            if l==0:
                ind=ind
            else:
                if ind==len(checker)-1:
                    ind=0
                else:
                    ind+=1
            l+=1
        # print(checker[ind])
        checker.remove(checker[ind])
        if ind==len(checker):
            ind=0

print(checker)
