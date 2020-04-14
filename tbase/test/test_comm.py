import os
import sys
import time
from multiprocessing import Process
import tbase.common as common
import tbase.communicator as communicator
import random



def testtask():
    while True:
        getdata =  communicator.Communicator().get_data()
        if getdata:
            with open(getdata.get("wpath"), "ab") as wfile:
                wfile.write(getdata.get("msg"))
            # time.sleep(4)
            print getdata.get("wpath")+ "write over !"

def test():
    for pid in range(0,10):
        sender = Process(target=testtask, name='send', args=([]))
        sender.start()

    for x in range(1000):
        msg = common.random_str(30)
        index = random.randint(0,9)
        content = {
            "msg": msg+'\n',
            "wpath": "file"+str(index)+".txt"
        }
        communicator.Communicator().send_data(content)
        print "oriqueue %d put over !"%index


if __name__ =="__main__":
    #note must init first this is import
    communicator.Communicator()
    test()