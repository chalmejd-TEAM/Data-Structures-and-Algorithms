from datetime import datetime
nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']
large = nemo * 100000

def findNemo(array):
    count = 0
    t0 = datetime.now().microsecond
    for i in range(len(array)):
        if(array[i] == 'nemo'):
            # print('Found Nemo')
            count = count + 1
    t1 = datetime.now().microsecond
    print('Call took:', t1-t0, 'microseconds. Found ', count, 'Nemos')
    

findNemo(nemo)
findNemo(everyone)
findNemo(large)

