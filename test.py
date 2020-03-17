import hashlib

s = 'hello world'
b = []

for i in range(0, len(s)):
    for j in range(1, len(s) + 1):
        if len(s[i:j]) != 0 and len(s[i:j]) != len(s):
            b.append(''.join(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()))

print(len(set(b)))
print(set(b))