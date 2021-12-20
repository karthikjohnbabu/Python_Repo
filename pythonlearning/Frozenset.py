s={10,20,30,40}
fs=frozenset(s)
print(type(fs))#<class 'frozenset'>
print(fs)#frozenset({40, 10, 20, 30})
fs.add(50)#AttributeError: 'frozenset' object has no attribute 'add'