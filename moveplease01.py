#!/usr/bin/env python3
import shutil
import os
os.chdir("/home/student3/mycode/")

xname = input("What is the new name for kerrigan.obj?")

shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" +xname)



#shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
#shutil.copytree("5g_research/", "5g_research__backup/")
