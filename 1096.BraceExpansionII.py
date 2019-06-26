class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def cal():
            nonlocal op_stack, res_stack
            op = op_stack.pop()
            l2 = res_stack.pop()
            l1 = res_stack.pop()
            if op == ',':
                for item in l2:
                    if item not in l1:
                        l1.append(item)
                res_stack.append(l1)
            elif op == '*':
                res_stack.append([s1 + s2 for s1 in l1 for s2 in l2])
        
        res_stack, op_stack = list(), list()
        for i, c in enumerate(expression):
            if c == '{':
                if i > 0 and expression[i - 1] not in {',', '{'}:
                    op_stack.append('*')
                op_stack.append(c)
            elif c == ',':
                while op_stack[-1] == '*':
                    op = op_stack.pop()
                    l2 = res_stack.pop()
                    l1 = res_stack.pop()
                    res_stack.append([s1 + s2 for s1 in l1 for s2 in l2])
                op_stack.append(c)
            elif c == '}':
                while op_stack[-1] != '{':
                    cal()
                op_stack.pop()
            else:
                if not res_stack:
                    res_stack.append([c])
                    continue
                if i > 0 and expression[i - 1] == '}':
                    op_stack.append('*')
                if i > 0 and expression[i - 1] not in {',', '{', '}'}:
                    res_stack[-1][-1] += c
                else:
                    res_stack.append([c])

        while op_stack:
            cal()
        return sorted(res_stack[0])

