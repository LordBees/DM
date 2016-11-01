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
