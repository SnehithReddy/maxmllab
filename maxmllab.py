def getDistinctCharactersCount(stringInput):
    stringDict = {}
    for i in stringInput:
        if stringDict.__len__() == 26:
            return "26"
        if i not in stringDict:
            stringDict[i] = "1"
    return str(stringDict.__len__())
 
 
 
def distinctCharacter (S,len):
    distinict_count = [1]*len
    dic ={}
    dic[S[0]]=1

    for each_index in range(1,len):
        if S[each_index] not in dic:
            distinict_count[each_index]=distinict_count[each_index-1]+1
            dic[S[each_index]] = distinict_count[each_index]
           
        else:
            distinict_count[each_index]=distinict_count[each_index-1]
            
    return distinict_count
            
 
len_ = int(input())
S = input()
Q = int(input())
arr = []
out_ = distinctCharacter(S, len_)
 
for _ in range(Q):
    l,r=list((map(int, input().split())))
    l= l-1
    print(getDistinctCharactersCount(S[l:r]))
    # set_count = set(S[l:r])
    # print(len(set_count))
    # if len==0:
    #     print (0)
    # else:
        
    #     res = out_[r-1]-out_[l-1]+1
    #     print(res)