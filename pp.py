




encrypter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',"@","#","$","%","*","1","2","3","4","5"]

word=input("enter word").lower()
shift=int(input("enter value"))
shifted_index=0
decrypter=[]

newlist=[]

for letter in word:
    decrypter.append(letter)

for i in range(0,len(decrypter)):
    if(decrypter[i]in encrypter):
        for j in range(0,len(encrypter)):
            if(decrypter[i]==encrypter[j]):
                shifted_index=j-1-shift
                newlist.append(shifted_index)

for j in range(0,len(newlist)):
    print(encrypter[newlist[j]])