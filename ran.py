

if __name__ == '__main__':

    import numpy as np
    start = 0  # 最小值
    end = 650000  # 最大值（不包含）
    num = 650000  # 生成的随机数数量
    random_numberslist = np.random.choice(np.arange(start, end), size=num, replace=False)
    np.savez('random_numbers.npz', random_numberslist=random_numberslist)