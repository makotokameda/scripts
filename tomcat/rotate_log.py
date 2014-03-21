#!/usr/local/bin/python3
import lzma
import os
import datetime
from stat import *
import tarfile

now = datetime.date.today()
archive_age = 7
delete_age = 30
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

tar_file = tarfile.open(file + '.tar.lzma', 'w:xz')
for archive in target_archives:
    tar_file.add(tomcat_log_dir + archive, arcname=archive)
    tar_file.close()
for old_f in old_files:
    os.remove(tomcat_log_dir + old_f)



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