# 跳脫字元
print("第一行\n第二行")
print("第一行\t第二行")
print("第一行\\第二行")
print("第一\"行\"第二行")
print(r"第一行\t第二行")

# 字串取索引
s = "Python"
print(s[0])
print(s[5])
print(s[-1])

# 字串切片
print(s[0:3]) # 大於等於起始值, 小於結束值
print(s[3:]) # 沒有結束值, 取到最後一個字
print(s[:3]) # 沒有起始值, 從索引值 0 開始取
print(s[::2]) # 隔兩個字元取
print(s[::-1]) # 字串 reverse

# s[0] = "J" # 字串是不可變的, 所以不能指定索引更動內容