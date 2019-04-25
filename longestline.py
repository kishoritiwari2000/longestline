'''
write the function largest() which accept the a filename as a parameter
and reports the longest line along with number of char
'''
def largest(f):
    a = open(f,'r')
    lines = a.readlines()
    a.close()
    lm = [len(i) for i in lines]
    mx = max(lm)
    return mx , lm.index(mx)+1
file = 'name.txt'
char, position = largest(file)
print('largest line at position ',position)
print('number of char ',char)


