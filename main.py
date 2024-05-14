from iqiyi import aiqiyi

'''脚本入口'''
def main():
    #创建任务对象
    _aiqiyi=aiqiyi()
    a = _aiqiyi.user_information()
    
if __name__ == '__main__':
    main()
