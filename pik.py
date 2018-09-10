import pickle
from pickle import *
L=[10,20,30,40,50]
f=open("F:\pythonpro\Binnarry.dat",'wb')
pickle.dump(L, f)
f.close()


f=open("F:\pythonpro\Binnarry.dat",'rb')
p=pickle.load(f)
print(p)
