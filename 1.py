rooms = []
Total = 0
Dimensions = []

Number = int(input("Input number of rooms (3-20): "))
while Number < 3 or Number > 20:
    Number = int(input("Re-enter number of rooms (3-20): "))

for NumbAvr in range(Number):
    room_name = input(f"Name of room {NumbAvr + 1}: ")
    length = int(input("Length: "))
    width = int(input("Width: "))
    Area = length * width

    # 确保 Dimensions 有足够的行
    while len(Dimensions) <= NumbAvr:
        Dimensions.append([])

    # 直接存储所有数据（房间名、长、宽、面积）
    Dimensions[NumbAvr] = [room_name, length, width, round(Area, 2)]
    rooms.append(room_name)  # 可选：如果仍需单独存储房间名

# 计算总面积和平均值
Total = sum(row[3] for row in Dimensions)  # 所有房间面积之和
Average = round(Total / Number, 2)
# 假设 Dimensions 是二维数组，结构为: [房间名, 长度, 宽度, 面积]
# 冒泡
# 冒泡排序：按面积降序（大的在前，小的在后）
n = len(Dimensions)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        # 比较当前元素和下个元素的面积（索引3）
        if Dimensions[j][3] < Dimensions[j + 1][3]:
            # 交换两个房间的所有数据（名称、长、宽、面积）
            Dimensions[j], Dimensions[j + 1] = Dimensions[j + 1], Dimensions[j]

# 打印排序结果
print("排序后（面积从大到小）：")
for room in Dimensions:
    print(f"房间: {room[0]}, 长度: {room[1]}, 宽度: {room[2]}, 面积: {room[3]}")