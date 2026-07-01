age = 18
name = 'Ben Chen'
height = 170.5
is_login = True # 下底線命名方式 蛇形命名方式
isAdmin = False
# 小駝峰命名方式



print(age)
print(name)
print(height)
print(is_login)


age = 28
print(age)

age = "老師騙人"
print("\r") # 換行字元: \n \r
print(age)


a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)


age = 38
print(name, age)
print("年紀是" + str(age))
print(f"{name} 年紀是 {age}")

your_name = input("請輸入你的名字：")
your_age = input("請輸入你的年紀：")
print(f"{your_name} 年紀是 {your_age}")
# print(your_age + 1) # input 收到的資料一定是字串

print(type(your_age))
print(type(your_age).__name__)