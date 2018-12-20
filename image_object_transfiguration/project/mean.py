import numpy as np
with open('./list_landmarks_celeba.txt','r')as f:
    line0 =f.readline()
    locations = f.readline().strip().split()   #eye,nose,mouth

    summ = np.zeros(10)
    for line in f:
         line = line.strip().split()
         for i in range(1,11):
             summ[i-1] = summ[i-1]+int(line[i])
    
    for i in range(10):
         summ[i] /=202599
         summ[i] -=256
         summ[i] /=256
         print(locations[i],": ",summ[i])
