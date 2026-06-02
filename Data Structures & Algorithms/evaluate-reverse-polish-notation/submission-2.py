class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        k = []
        for op in tokens:
            if op == '+':
                b = k.pop()
                a = k.pop()
                k.append(a + b)
            elif op == '-':
                b = k.pop()
                a = k.pop()
                k.append(a - b)
            elif op == '*':
                b = k.pop()
                a = k.pop()
                k.append(a * b)
            elif op == '/':
                b = k.pop()
                a = k.pop()
                k.append(int(a / b))
            else:
                k.append(int(op))
        return k[-1]
        