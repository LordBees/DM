##iotest
def readfile(fname):
        try:
            f = open(fname,'r')
            data = f.readlines()
            f.close()
        except:
            try:
                f.close()
            except:
                print('error/file already closed!')
        return data


x =  readfile('Dwarf.txt')
for y in range(len(x)):
    x[y] = x[y].strip('\n')


data = x
x=None
test_in = ['Dwarf','HILL']
##readingdata = [False,'',0]
##for x in range(len(data)):
##    if '[' in data[x]:
##        if not readingdata[0]:##define cases for where data goes
##            if data[x] == '[BASE]':##base char attributes
##                pass
##            elif data[x]
##            readingdata[2] == data[x+1]##stores linelength
reading = False

ctag = ''
for x in range(len(data)):
    #detets start and end of file
    if '[' in data[x]:
        ctag  = data[x]
        reading = True
    elif data[x] == '[END]':
        reading = False
        
        
