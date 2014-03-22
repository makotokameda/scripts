#!/usr/local/bin/python3
import os
import sys
import subprocess
import re
import codecs


class PivCommitMessageAppender(object):
    def __init__(self, msg_file):
        self.__msg_file = msg_file
        self.__msg_file = ""
        self.__piv_url = "https://www.pivotaltracker.com/story/show/"
        self.__final_pids = []
        self.__final_urls = []

    def find_piv_story_ids(self):
        branches = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], universal_newlines=True)
        brs = re.search("-(.*?)$", branches.strip("\n"))
        if brs == None:
            exit()
        self.set_piv_story(brs)

    def set_piv_story(self, brs):
        piv_story_ids = brs.group(1).split(",")
        pid_f = re.compile("[0-9]*")
        for piv_id in piv_story_ids:
            m = pid_f.match(piv_id)
            if m != None:
                self.__final_pids.append('#' + piv_id)
                self.__final_urls.append(self.__piv_url + piv_id)

    def append(self):
        self.find_piv_story_ids()
        f = codecs.open(self.__msg_file, "r+", "utf-8")
        contents = f.read()
        begin_tag = '[' + ', '.join(self.__final_pids) + ']'
        urls = '\n'.join(self.__final_urls)
        f.seek(0)
        print(begin_tag + contents + urls, file=f)
        f.close()


msg_file = sys.argv[1]
appender = PivCommitMessageAppender(msg_file)
appender.append()

