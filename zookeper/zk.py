from kazoo.client import KazooClient
from kazoo.client import KazooState
from kazoo.handlers.gevent import SequentialGeventHandler
from time import sleep
import sys
import os
def watch_fun(event):
    print("A process got killed")
    children = zk.get_children("/trial")
    l = []
    for i in children:
        node = "/trial/"+i
        l1=int((zk.get(node)[0]).decode("utf-8"))
        l.append(l1)
    minn=min(l)
    if(minn==os.getpid()):
        minn1=min(children)
        minn1="/trial/"+minn1
        async_obj = zk.exists_async(minn1)
        sleep(5)
        async_obj.rawlink(my)
def my(async_obj):
    print("In callback")
    #zk.create_async("/trial/process",sequence=True,ephemeral=True)
    print("Current running processes are",zk.get_children("/trial"))
    print("Starting a new process by ",os.getpid())
    os.system("python /home/shashank/Desktop/zk.py 1 0")
zk = KazooClient(hosts='127.0.0.1:2181')
no_process = int(sys.argv[1])
zk.start()
pid=os.getpid()
pid_byte=bytes(str(pid),'utf-8')
l=zk.create("/trial/process",sequence=True,ephemeral=True)
zk.set(l,pid_byte)
while(len(zk.get_children("/trial"))!=no_process):
    count = 0
sleep(5)
l1=zk.get_children("/trial",watch=watch_fun)
print("process "+str(pid)+" created "+l)
sleep(25)
zk.stop()
