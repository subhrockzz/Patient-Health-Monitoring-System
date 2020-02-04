import hashlib
#h=hashlib.new('ripemd160')
#h.update(b"subhrajeetjpg@gmail.com")
name="subhrajeetjpg@gmail.com"
x = hashlib.sha1(str.encode(name))

y=(x.hexdigest())
print(y)
