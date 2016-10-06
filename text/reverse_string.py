# Enter string and it will be reversed and printed

s = input('Enter a string to be reversed:')
s = list(s)
s.reverse()
s = ''.join(s)
print(s)