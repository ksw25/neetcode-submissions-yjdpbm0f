class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        operations= {
            "+": lambda a,b: a+b,
            "-": lambda a,b: a-b,
            "*": lambda a,b: a*b,
            "/": lambda a,b: int(a/b),
        }

        for val in tokens:
            if val not in operations:
                stack.append(int(val))
            else:
                post, pre = stack.pop(), stack.pop() 
                res = operations[val](pre, post)
                stack.append(res)
        return stack[-1]