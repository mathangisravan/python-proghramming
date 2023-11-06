str1 = 'amma'
l = 0
r = len(str1) -1
flag =0
while(l <len(str1)//2):
    if(str1[l]==str1[r]):
        l=-1
        r = +1
    else:
        flag = 1
if(flag ==0):
    print('The word is a palendrome')
elif(flag ==1):
    print('The word is not a palendrome')