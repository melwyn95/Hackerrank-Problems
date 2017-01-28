for i in range(int(raw_input())):
    s = raw_input()
    substrings = []
    count = []
    length = []
    same = [[] for i in range(len(s))]
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substrings.append(s[i:j])
            length.append(len(s[i:j]))
            same[len(s[i:j])-1].append([s[i:j].count(chr(97+k)) for k in range(26)])
            count.append([s[i:j].count(chr(97+k)) for k in range(26)])
    answer = 0
    for bucket in same:
        for i in range(len(bucket)):
            for j in range(i+1, len(bucket)):
                if bucket[i] == bucket[j]:
                    answer += 1
    print answer        
