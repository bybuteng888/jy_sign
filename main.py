
from iqiyi import aiqiyi

'''脚本入口'''
def main():
    #创建任务对象
    _iqiyi=aiqiyi()
    contents=_iqiyi.start()
    
if __name__ == '__main__':
    main()
