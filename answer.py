class Game:
    def smallGame(self):
        time = 3
        answer = '大哥哥'
        while time > 1:
            name = str(input('请输入您的姓名：'))
            age = int(input('请输入您的年龄：'))
            question = str(input('(你叫我叫什么?)请输入你的答案：'))
            if age > 18:
                time -= 1
                if question == answer:
                    print('您老答对了，奖励你一个么么哒！~~~~~~')
                    exit()
                else:
                    print('您老是成年人了。。。。,可以玩这个游戏,你还剩%d次机会！' % time)
            else:
                print('您小还是一个骚年啊，我看你还是回家歇着吧')
                exit()

game = Game()
game.smallGame()
