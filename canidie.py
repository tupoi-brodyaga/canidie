array = ['t', 'r', 'a', 'c', 'e', 'c', 'a', 'r', 's']
print (array)
s = array[::-1]
print (s)
if array[0] != s[0]:
    del s[0]
if array[1] != s[1]:
    del s[1]
if array[2] != s[2]:
    del s[2]
if array[3] != s[3]:
    del s[3]
if array[4] != s[4]:
    del s[4]
if array[5] != s[5]:
    del s[5]
if array[6] != s[6]:
    del s[6]
if array[7] != s[7]:
    del s[7]
if array[8] != s[8]:
    del s[8]
print ('input:', ''.join(array))
print ('output:', ''.join(s))
print ('perfect, i create pelindrome')
