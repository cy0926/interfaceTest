import time
'''时间问题，运行的时候，跟时间相关的，总是会报下面这个错误，目前暂时无法解决，但是运行tests.py这个，又不会报下面这个错误，在接口测试的代码里面，
   同样的时间相关的代码，就会报下面这行错。。。。
     ValueError: unconverted data remains: +00:00
'''
time1 = '2001-08-20 14:00:00'
timeArray = time.strptime(str(time1), "%Y-%m-%d %H:%M:%S")
# t1 = time.st
print(timeArray)
print(type(timeArray))
# # %m/%d/%Y%H:%M:%S
e_time = int(time.mktime(timeArray))
print(e_time)
print(type(e_time))

now_time = str(time.time())  # 当前时间
ntime = now_time.split(".")[0]
n_time = int(ntime)
print(n_time)
print(type(n_time))

if n_time > e_time:
    print(u'当前时间大')
    print('event has started')
else:
    print(u'e_time大')
