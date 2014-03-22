#!/usr/local/bin/python3
import lzma
import os
import datetime
from stat import *
import tarfile


class Archiver(object):
    pass

    def __init__(self, files_dir, archive_age, delete_age):
        self.files_dir = files_dir
        self.file_list = os.listdir(self.files_dir)
        self.archive_age = archive_age
        self.delete_age = delete_age
        self.target_archives = []
        self.old_files = []

    def archive(self):
        self.set_target_files()
        self.archive_files()

    def set_target_files(self):
        for file in self.file_list:
            if file.endswith(".log"):
                ts = os.stat(self.files_dir + file).st_mtime
                now = datetime.date.today()
                mtime = datetime.date.fromtimestamp(ts)
                dif_test = now - mtime
                if (dif_test).days >= self.archive_age:
                    self.target_archives.append(file)
                if (now - mtime).days >= self.delete_age:
                    self.old_files.append(file)

    def archive_files(self):
        for archive in self.target_archives:
            f = tarfile.open(self.files_dir + archive + ".tar.lzma", "w:xz")
            f.add(self.files_dir + archive, arcname=archive)
            f.close()

        for old_f in self.old_files:
            os.remove(self.files_dir + old_f)


archive_age = 7
delete_age = 30
files_dir_list = ["/usr/local/tomcat/logs/", "/usr/local/tomcat/logs/"]
for files_dir in files_dir_list:
    archiver = Archiver(files_dir, archive_age, delete_age)
    archiver.archive()
