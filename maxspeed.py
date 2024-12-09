import numpy as np

# 加载数据
data = np.load('train.npz', allow_pickle=True)
x = np.array(data['y'], dtype=np.float64)[1:]
y = np.array(data['z'], dtype=np.float64)[1:]

# 计算第1和第100之间的变化量
dx_list = x[99:] - x[:-99]  # 对应的 x 变化量
dy_list = y[99:] - y[:-99]  # 对应的 y 变化量

# 找出最大值和最小值
dx_max, dx_min = dx_list.max(), dx_list.min()
dy_max, dy_min = dy_list.max(), dy_list.min()

print(f"dx 最大值: {dx_max}, 最小值: {dx_min}")
print(f"dy 最大值: {dy_max}, 最小值: {dy_min}")
# # 计算每一步的变化量
# dx = np.diff(x)
# dy = np.diff(y)
#
# # 分别计算 x 和 y 方向的速度
# speed_x = np.abs(dx)
# speed_y = np.abs(dy)
#
# # 找到 x 和 y 方向的最大速度
# max_speed_x = np.max(speed_x)
# max_speed_y = np.max(speed_y)
#
# print("x 方向最大速度:", max_speed_x)
# print("y 方向最大速度:", max_speed_y)
