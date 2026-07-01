user = {
    "id": 9,
    "account": "benchen",
    "password": "a12345",
    "email": "ben@gmail.com"
} # 是資料庫中的一筆資料
user2 = {
    "id": 10,
    "account": "may",
    "password": "a12345",
    "email": "may@gmail.com"
}

db = []
db.append(user)
db.append(user2)

print(type(user))
print(user)
print(user["email"])

print(f"\n{db}") # 為了換行
# 所以很多筆資料存進一個 list 當中, 就類似一個資料庫


# 取出 account may
# 取出指定索引指定欄位的資料
print(db[1]["account"])