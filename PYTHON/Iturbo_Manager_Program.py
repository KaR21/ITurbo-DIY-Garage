from Manager import Manager
from Enployees import Enployees


m1 = Manager(1, "gaizka", "zabarte")
m2 = Manager(2, "leire", "sosola")

e1 = Enployees(1, "andoni", "goiko", "eibar", 632654357, "goiko.andoni@iturbo.eus","worker")
e2 = Enployees(2, "elena", "martin", "eibar", 632654357, "martin.elena@iturbo.eus","worker")
e3 = Enployees(3, "iraia", "ilarra", "eibar", 632654357, "ilarra.iraia@iturbo.eus","worker")

emplist=[]
emplist.append(m1)
emplist.append(m2)

emplist.append(e1)
emplist.append(e2)
emplist.append(e3)

for worker in emplist:
    worker.print()

def save_object(obj,filename):
   with open(filename, 'ab') as outp:  # Overwrites any existing file.
       pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

   ans=1
   while ans==1:
    e1 = Manager.Manager()
    save_object(e1 , 'manager_data.pkl')
    ans=int(input("Do you want to add a new manager? (1/0)"))
    del s1

