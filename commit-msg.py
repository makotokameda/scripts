#!/usr/local/bin/python3
import subprocess
import re

branches = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], universal_newlines=True)
a = re.search("-(.*?)$",  branches.strip("\n"))
pivStoryIDs = a.group(1).split(".")
pivURL="https://www.pivotaltracker.com/story/show"

p = re.compile("[0-9]*")
for pivID in pivStoryIDs:
    m = p.match(pivID)

# if [ "$ManualMessagePivotalID" == "" ] ; then
#
#         if [ $Branch == "master" ] ; then
#         echo ""
#         else
#                 StoryNo="$(echo $Branch | sed -e "s/^.*-\([0-9]*\)$/\1/g")"
#         mv $1 $1.tmp-msg
#         echo "[#$StoryNo]" > $1
#         cat $1.tmp-msg >> $1
#                 echo "$PivotalTrackerURL/$StoryNo" >> $1
#         fi
# fi