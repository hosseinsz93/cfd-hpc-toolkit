#!/usr/bin/python

# Find the last complete time step in current directory.

DEBUG = False
# DEBUG = True

import os
import pdb
import re
import string
import subprocess
import sys


def modTimeStep(timeStep, mod):
    if mod < 0:
        return int(timeStep);

    return (int(timeStep) // mod) * mod


def lastTimeStep():

    if DEBUG:
        import pdb
        pdb.set_trace()

    # print os.getcwd()

    sysCmd = subprocess.Popen('ls *[0-9][0-9][0-9][0-9][0-9][0-9]*', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdoutdata, stderrdata) = sysCmd.communicate()
    code = sysCmd.wait()

    if code < 0 or stderrdata:
        print '999999'
        if stderrdata:
            print (stderrdata)
        ret = -1
        if code < 0:
            ret = code
        sys.exit(ret)

    retimestep = re.compile(r'^.+[^0-9]([0-9]{6})[^0-9].+$')
    reexclstdo = re.compile(r'\.stdout\.')
    reexclResu = re.compile(r'^Result')
    reexclshea = re.compile(r'^shear')

    files = string.split(stdoutdata, '\n')
    if files[len(files)-1] == '':
        files.pop()

    for i in range(len(files)):
        if reexclstdo.match(files[i]) or reexclResu.match(files[i]) or reexclshea.match(files[i]):
            files[i] = ''
            continue

        if not retimestep.match(files[i]):
            files[i] = ''
            continue

        timestep = retimestep.search(files[i])
        files[i] = '{} {}'.format(timestep.group(1), timestep.group(0))
    files.sort()


    i = 0
    cnt = [ [ '', 0 ], [ '', 0 ] ]
    for j in reversed(range(len(files))):
        # Found files that were ignored.  Stop here.
        if files[j] == '':
            break

        if cnt[i][0] == '':
            cnt[i][0] = files[j][0:6]

        if files[j][0:6] != cnt[i][0]:
            i += 1
            if i >= 2:
                break
            cnt[i][0] = files[j][0:6]

        cnt[i][1] += 1

    if cnt[0][1] == 0:
        print '999999'
        sys.exit(1)

    if len(sys.argv) < 2 or int(sys.argv[1]) < 0:
        mod = -1
    else:
        mod = int(sys.argv[1])

    if cnt[0][1] < cnt[1][1]:
        print modTimeStep(cnt[1][0], mod)
    else:
        print modTimeStep(cnt[0][0], mod)


    sys.exit(0)


if __name__ == '__main__':
    lastTimeStep()
