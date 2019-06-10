def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
time = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
print("file1 : ",file_len('machine1.txt'))
r = open('machine1.txt', 'r').read()
for i in range(0,24):
    print(time[i]+" => ",end='')
    print(r.count(time[i]))
print("file2 : ",file_len('machine2.txt'))
print("file3 : ",file_len('machine3.txt'))
