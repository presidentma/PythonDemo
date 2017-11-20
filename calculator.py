class calculator:
    def calculator(self, firstInput, symbol, secondInput):
        operator = {
            '+': firstInput + secondInput,
            '-': firstInput - secondInput,
            '*': firstInput * secondInput,
            '/': firstInput / secondInput
        }
        res = operator.get(symbol)
        if res:
            return res
        else:
            return '不支持的计算符号'

    def getResult(self, firstInput, symbol, secondInput):
        print(self.calculator(firstInput, symbol, secondInput))

bool = True
while(bool):
    firstInput = float(input('请输入第一个数字：'))
    symbol = str(input('请输入计算符号+ - * /：'))
    secondInput = float(input('请输入第二个数字：'))
    calculatorClass = calculator()
    calculatorClass.getResult(firstInput, symbol, secondInput)
