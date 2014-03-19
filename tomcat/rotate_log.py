#!/usr/local/bin/python3
import lzma
import os
import datetime
from stat import *
import tarfile

now = datetime.date.today()
age = 6
tomcat_log_dir = "/usr/local/tomcat/logs/"
file_list = os.listdir(tomcat_log_dir)
target_archives = []
old_files = []
for file in file_list:
    if file.endswith(".log"):
        ts = os.stat(tomcat_log_dir + file).st_mtime
        mtime = datetime.date.fromtimestamp(ts)
        if (now - mtime).days >= 0:
            target_archives.append(file)
        if (now - mtime).days >= 0:
            old_files.append(file)

tar_file = tarfile.open('test.tar.lzma', 'w:xz')
for archive in target_archives:
    tar_file.addfile(archive)

            #os.remove(file)



        #LOG_DIR=/usr/local/tomcat/logs/
        #
        #lzmafiles=`find ${LOG_DIR} -mmin +1440 -regex ".*\.\(log\|txt\)$" -printf "%p "`
        #if [ "$lzmafiles" != "" ] ; then
        #    lzma ${lzmafiles}
        #fi
        #
        #delfiles=`find ${LOG_DIR} -mmin +43200 -printf "%p "`
        #if [ "$delfiles" != "" ] ; then
        #    rm ${delfiles}
        #fi
        #
        #LOG_DIR=/var/log/jenkins/
        #delfiles=`find ${LOG_DIR} -mmin +43200 -printf "%p "`
        #if [ "$delfiles" != "" ] ; then
        #    rm ${delfiles}
        #fi