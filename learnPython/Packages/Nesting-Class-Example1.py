class outer:
    def __init__(self):
        print('outer Class object Creation')
    class inner:
        def __init__(self):
            print('Inner class object creation')
        class innerinner:
            def __init__(self):
                print('InnerInner class')
            def m1(self):
                print('Nested Inner class')
o=outer()
i=o.inner()
ii=i.innerinner()
ii.m1()

outer().inner().innerinner().m1()

