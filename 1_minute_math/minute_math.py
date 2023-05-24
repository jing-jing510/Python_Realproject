# auth ： xiaokou
# date ： 2023/5/24 10:30
import random
import time

# 直接在控制台使用命令行运行
# 程序运行之后倒计时1分钟之后结束
# 随机出100以内的2个整数加减乘除运算题目（除法确保能够除尽，但除数不能为0）
# 每出一道题目，由玩家给出答案，然后程序判断对错，接着出下一题，并且显示剩余时间
# 1分钟时间结束，显示总题数和正确率（正确率精确到小数点后2位），并将之前的题目和答案显示出来


#     找到能被a 整除的数
def get_divisor(a):
    l = []
    for i in range(1,a+1):
        if a%i ==0:
            l.append(i)
    return random.choice(l)



if __name__=="__main__":
    ops = ["+","-","*","/"]
    # 计时
    start_time =time.time()
    total = 0
    correct = 0
    question = []
    while time.time()-start_time <=60:
        a = random.randint(1,99)
        op = random.choice(ops)
        if op == '/':
            # 除法确保能够除尽，但除数不能为0
            b = get_divisor(a)
        else:
            b =random.randint(1,99)
        # 获取正确答案
        a_op_b = "{}{}{}".format(a,op,b)
        c = int(eval(a_op_b))

        try:
            ans = int(input("{} = ".format(a_op_b)))
        except:
            ans = ' '

        # 判断是否正确
        if time.time() -start_time <=60:
            if c == ans:
                print("回答正确!剩余时间{}秒".format(int(60-(time.time()-start_time))))
                correct +=1
            else:
                print("回答错误!剩余时间{}秒".format(int(60 - (time.time() - start_time))))
            total +=1
            question.append("{}={}".format(a_op_b,c))
print("{}道题目,正确率{:.2f}%".format(total,correct/total * 100))
for q in question:
    print(q)
