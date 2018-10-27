import random
a = ['羊1', '羊2', '汽车']
times = 1000*1000  # 尝试次数
first, change = 0, 0
for i in range(times):
    x = random.choice(a)  # 正确答案
    y = random.choice(a)  # 参赛者选择答案
    if x == y:   # 坚持最初的选择
        first += 1
    else:         # 改变选择
        change += 1
print("坚持初心获得胜利的概率：{:.2f}%".format(first/times*100))
print("改变初心获得胜利的概率：{:.2f}%".format(change/times*100))
