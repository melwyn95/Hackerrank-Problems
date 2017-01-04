s = raw_input()
s_set = list(set(list(s)))
s_print = ""
for i in s_set:
    count = s.count(i) % 2
    s_print += (i * count)
if len(s_print) > 0:
    print s_print
else:
    print "Empty String"
