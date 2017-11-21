import random as r
result = r.randrange(1, 101)
time = 4
shift_time = 4
while time > 0:
    answer = int(input('请输入你的答案：'))
    time -= 1
    if answer == result:
        print('你真聪明用了%d次就猜对了' % shift_time - time)
        exit()
    elif time != 0:
        print('你猜错了，还剩%d次机会' % time)
    else:
        print('次数用完了没有猜对，正确答案是%d' % result)
