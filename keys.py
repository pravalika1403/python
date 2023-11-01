l=[]
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
beta=['x','k','q','s','u','p','m','j','f','g','d','b','e','h','c','a','y','r','v','o','i','n','z','t','l','w']
for i in range(3):
    s=list(map(str,input().split()))
    l.append(s)
for i in l:
    for j in i:
        en=[]
        for k in j:
            en.append(k)
        for item in range(len(en)):
            for s in range(26):
                if  en[item]==beta[s]:
                    en[item]=alpha[s]
                    break
        for item in en:
            print(item,end=' ')
                
                

    
for i in l:
    for j in i:
        print(j,end=' ')
    print()
    
