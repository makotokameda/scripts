#!/usr/local/bin/python3
import os
import sys
import subprocess
import re
import codecs

msg_file = sys.argv[1]

branches = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], universal_newlines=True)
brs = re.search("-(.*?)$", branches.strip("\n"))
if brs == None:
    print('fertig')
pivStory_ids = brs.group(1).split(",")

pivURL = "https://www.pivotaltracker.com/story/show"

final_pids = []
pid_f = re.compile("[0-9]*")
for piv_id in pivStory_ids:
    m = pid_f.match(piv_id)
    if m != None:
        final_pids.append('#' + piv_id)


f = codecs.open(msg_file, "r+", "utf-8")
all = f.read()
f.seek(0)
begin_tag = '[' + ', '.join(final_pids) + ']'
print(begin_tag, file=f)
print(all, file=f)
f.close()