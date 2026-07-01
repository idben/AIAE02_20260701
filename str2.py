# 跳脫字元
print("第一行\n第二行")
print("第一行\t第二行")
print("第一行\\第二行")
print("第一\"行\"第二行")
print(r"第一行\t第二行")
print("-" * 20)
# 字串取索引
s = "Python"
print(s[0])
print(s[5])
print(s[-1])
print("-" * 20)
# 字串切片
print(s[0:3]) # 大於等於起始值, 小於結束值
print(s[3:]) # 沒有結束值, 取到最後一個字
print(s[:3]) # 沒有起始值, 從索引值 0 開始取
print(s[::2]) # 隔兩個字元取
print(s[::-1]) # 字串 reverse
print("-" * 20)
# s[0] = "J" # 字串是不可變的, 所以不能指定索引更動內容

s2 = "豬腳麵線"
print(len(s2))
print("-" * 20)

s3 = "Python PYTHON"
print(f"轉大寫: {s3.upper()}")
print(f"轉小寫: {s3.lower()}")
print(f"第一個字元轉大寫: {s3.capitalize()}")
print(f"每一個單字的第一個字母轉成大寫: {s3.title()}")
print("-" * 20)

s4 = "     hello     "
print(s4)
print(s4.strip())