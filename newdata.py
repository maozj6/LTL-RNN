import numpy as np

if __name__ == '__main__':
    data = np.load('train.npz',allow_pickle=True)

    x1 = np.array(data['y'],dtype=np.float64)[1:]
    y1 = np.array(data['z'],dtype=np.float64)[1:]

    start = 0  # 最小值
    end = 6600  # 最大值（不包含）
    num = 6600  # 生成的随机数数量
    newxtrain=[
    ]
    newytrain=[]
    xval=[]
    yval=[]
    xtest=[]
    ytest=[]
    random_numberslist = np.random.choice(np.arange(start, end), size=num, replace=False)*100
    # 不重复随机数
    for i in range(num):
        random_numbers = random_numberslist[i]
        # print(random_numbers)
        # print("---")

        if i <400:
            print(i)

            xtmp = []
            ytmp = []
            for j in range(100):
                xtmp.append(x1[random_numbers + j * 100])
                ytmp.append(y1[random_numbers + j * 100])
            newxtrain.append(xtmp)
            newytrain.append(ytmp)

        if 400<i<500:
            print(i)

            xtmp=[]
            ytmp=[]
            for j in range(100):
                xtmp.append(x1[random_numbers+j*100])
                ytmp.append(y1[random_numbers+j*100])
            xval.append(xtmp)
            yval.append(ytmp)

        if 500<i<600:
            print(i)

            xtmp=[]
            ytmp=[]
            for j in range(100):
                xtmp.append(x1[random_numbers+j*100])
                ytmp.append(y1[random_numbers+j*100])
            xtest.append(xtmp)
            ytest.append(ytmp)

    np.savez("newtrain.npz",x=newxtrain,y=newytrain)
    np.savez("newval.npz",x=xval,y=yval)
    np.savez("newtest.npz",x=xtest,y=ytest)

