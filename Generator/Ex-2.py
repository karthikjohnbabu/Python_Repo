#write a generator function to generate first n values?
def first_n_values_Generator(n):
    i=1
    while i<=n:
        yield i
        i=i+1
g= first_n_values_Generator(5)
for x in g:
    print(x)


