import kmNet
import time
import multiprocessing
import json


stop_time=2

Counter = multiprocessing.Value('i', 1)

# 这里可以直接配置
# data={
#     "ip": "192.168.2.188",
#     "port": "33794",
#     "uuid": "8697E04E"
# }

# 这里是打包后通过配置文件配置
with open('config.json', 'r') as f:
        data = json.load(f)


def slow_function(cou):
    kmNet.init(data['ip'],data['port'],data['uuid'])
    cou.value=0
    print("成功连接！")
    


# 创建并启动子进程
def create_and_run_process():

    while Counter.value:

        p = multiprocessing.Process(target=slow_function,args=(Counter,))
        p.start()
        time.sleep(stop_time)  # 等待两秒
        if Counter.value:
            print("连接失败！正在重新连接！")
        p.terminate()  # 终止子进程
        p.join()  # 确保子进程完全退出


if __name__=="__main__":
    multiprocessing.freeze_support()
    create_and_run_process()

