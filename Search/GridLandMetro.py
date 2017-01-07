n, m, k = map(int, raw_input().split(" "))
unique_rows = []
c1_list = []
c2_list = []

area = n * m

for i in range(k):
    r, c1, c2 = map(int, raw_input().split(" "))
    if r not in unique_rows:
        unique_rows.append(r)
        diff = c2 - c1 + 1
        c1_list.append([c1])
        c2_list.append([c2])
        area -= diff
    else:
        index = unique_rows.index(r)
        diff = c2 - c1 + 1

        if c2 < min(c1_list[index]):
            area -= diff
            c1_list[index].append(c1)
            c2_list[index].append(c2)
        elif c1 > max(c2_list[index]):
            area -= diff
            c1_list[index].append(c1)
            c2_list[index].append(c2)
        else:
            l = len(c1_list[index])
            for i in range(l):
                if c1 < c1_list[index][i] and c2 <= c2_list[index][i]:
                    area -= (c1_list[index][i] - c1) # may be + 1
                    c1_list[index][i] = c1
                    break
                elif c2 > c2_list[index][i] and c1 >= c1_list[index][i]:
                    area -= (c2 - c2_list[index][i])
                    c2_list[index][i] = c2
                    break
                elif c1 < c1_list[index][i] and c2 > c2_list[index][i]:
                    area -= (c1_list[index][i] - c1)
                    area -= (c2 - c2_list[index][i])
                    c1_list[index][i] = c1
                    c2_list[index][i] = c2
                    break
print area
