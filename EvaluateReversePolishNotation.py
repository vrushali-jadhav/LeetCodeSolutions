import operator
class Solution():
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operandStack = []
        operatorDict = {"+":operator.add, "-":operator.sub, "*": operator.mul, "/":operator.truediv}

        for character in tokens:
            if character not in operatorDict:
                operandStack.append(int(character))
            else:
                operatorVal = operatorDict[character]
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()

                operandStack.append(int(operatorVal(operand1,operand2))) 

                print(operandStack)

        return operandStack[0]
        
s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(s.evalRPN(["4","13","5","/","+"]))