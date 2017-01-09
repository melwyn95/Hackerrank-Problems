lb = [1]
ub = [3]
start = [3]
for i in range(50):
    start.append(start[i] * 2)
    lb.append(ub[i] + 1)
    ub.append(start[i+1]+lb[i+1]-1)
#print ub[49]
t = int(raw_input().strip())
for i in range(50):
    if t <= ub[i]:
        add = t - lb[i]
        print (start[i] - add)
        break
