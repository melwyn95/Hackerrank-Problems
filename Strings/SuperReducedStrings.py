s = raw_input()
flag = True
while flag:
    i = 0
    while i < len(s):
        if i+1 == len(s):
            flag = False
            break
        #print s[i], s[i+1], s
        if s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
            flag = True
            break
        i += 1
    if i == len(s):
        flag = False
if len(s) > 0:
    print s
else:
    print "Empty String"
