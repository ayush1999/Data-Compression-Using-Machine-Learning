# Run length algorithm for lossless data compression.
def run_length_encode(s):
'''
Converting a string into its run
length code.
'''

    r = ""
    l = len(s)
    if l == 0:
        return ""
    if l == 1:
        return s + "1"
    last = s[0]
    cnt = 1
    i = 1
    while i < l:
        if s[i] == s[i - 1]:  
            cnt += 1
        else:
            r = r + s[i - 1] + str(cnt) 
            cnt = 1
        i += 1
    r = r + s[i - 1] + str(cnt)
    return r

def run_length_decode(s):
'''
Converting a run length code into its
equivalent string.
'''

    r= ""
    for i in range(0,len(s),2):
        temp=""
        for j in range(int(s[i+1])):
            temp = temp + s[i]
        r = r + temp
    return r
