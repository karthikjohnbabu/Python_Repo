# TODO: Implement this method
def findElementQuery(n, arr, q, query):
    first = -1
    last = -1
    for i in range(0, n):
        if (q != arr[i]):
            continue
        if (first == -1):
            first = i
        else:
            return -1
    return


# NOTE: Please do not modify this function
def main():
    n = int(input('Length of the array:').strip())
    arr = list(map(int, input('Enter the array:").strip().split(' ')))
    q = int(input("enter the element to search:").strip())

    query = []

    for i in range(q):
        x = int(input().strip())
        query.append(x)

    result = findElementQuery(n, arr, q, query)

    print(*result, sep="\n")


if __name__ == "__main__":
    main()

# Crio Methodology

# Milestone 1: Understand the problem clearly
# 1. Ask questions & clarify the problem statement clearly.
# 2. Take an example or two to confirm your understanding of the input/output & extend it to test cases
# Milestone 2: Finalize approach & execution plan
# 1. Understand what type of problem you are solving.
#      a. Obvious logic, tests ability to convert logic to code
#      b. Figuring out logic
#      c. Knowledge of specific domain or concepts
#      d. Knowledge of specific algorithm
#      e. Mapping real world into abstract concepts/data structures
# 2. Brainstorm multiple ways to solve the problem and pick one
# 3. Get to a point where you can explain your approach to a 10 year old
# 4. Take a stab at the high-level logic & write it down.
# 5. Try to offload processing to functions & keeping your main code small.
# Milestone 3: Code by expanding your pseudocode
# 1. Make sure you name the variables, functions clearly.
# 2. Avoid constants in your code unless necessary; go for generic functions, you can use examples for your thinking though.
# 3. Use libraries as much as possible
# Milestone 4: Prove to the interviewer that your code works with unit tests
# 1. Make sure you check boundary conditions
# 2. Time & storage complexity
# 3. Suggest optimizations if applicable