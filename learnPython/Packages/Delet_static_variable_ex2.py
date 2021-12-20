class Test:
    a=10
t=Test()
print(t.a)
#del t.a#AttributeError: a
del Test.a

# By using object reference/self variable we can read static variables but we cannot delete or modify.
#If we are trying to modify then a new instance variale will be added to that particular object.
#if we try to delete  static using object reference /self we get attribute error.


