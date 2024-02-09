def gcdOfStrings(str1, str2):
    res = ''
    if len(str1)<len(str2):
        for i in range(len(str1)):
            j=i
            while str1[j] == str2[j] and j<len(str1)-1:
                res += str1[j]
                j+=1
            break
    else:
        for i in range(len(str2)):
            j=i
            while str1[j] == str2[j] and j<len(str2)-1:
                res += str2[j]
                j+=1
            break
    print(res)

str1 = "ABABAB"
str2 = "ABAB"
gcdOfStrings(str1, str2)