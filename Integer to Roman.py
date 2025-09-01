
class roman_converter:
    def __init__(self):
        self.value = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        self.roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    def int_to_roman(self,num):
        res = " "
        i = len(self.value)-1
        while num > 0:
            if num >= self.value[i]:
                res = res + self.roman[i]
                num = num - self.value[i]
            else:
                i = i - 1
        return res
obj = roman_converter()
num = int(input("Enter a number: "))
roman_num = obj.int_to_roman(num)
print(f"Roman Numeral of {num} is: {roman_num}")