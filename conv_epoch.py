import datetime

# second_epoch = datetime.datetime.now().timestamp()*1000
# print(second_epoch)
# start = int(datetime.datetime(2018,1,1).timestamp())
# end = int(datetime.datetime.now().timestamp())
# print(start)
# print(end)
# dt = input('put some here')
# y,m,d = dt.split(',')



def strt(yr,mo,dy):
    start = datetime.datetime(int(yr),int(mo),int(dy)).timestamp()
    return ((int(start))*1000)


def end():  
    start = datetime.datetime.now().timestamp()
    return ((int(start))*1000)

# print(strt(2021,1,1))
# print(end()/1000)

