l1=[1,3,4,2,5]
d1={x:x**2 for x in l1}
print(d1)

d2={ x: f"id{x}"for x in range(5)}
print(d2)

l2=[101,103, 102]
l3=['gfg','ide','courses']
d3={l2[i]:l3[i] for i in range(len(l3))}
print(d3)