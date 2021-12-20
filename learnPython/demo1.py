#My requirement is to have both methods or both functions. What do i do?

#solution 1
import module1
import module2
module1.add(10,20)
module2.add(10,20)

#Solution 2:
from module1 import add as a1
from module2 import add as a2
a1(10,20)
a2(10,20) 