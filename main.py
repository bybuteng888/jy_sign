from iqiyi import aiqiyi


'''脚本入口'''
def main():
    #创建任务对象
    _aiqiyi=aiqiyi()
    contents=_aiqiyi.start()
    
if __name__ == '__main__':
    main()
