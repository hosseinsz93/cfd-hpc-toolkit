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

    # print(os.getcwd())

    sysCmd = subprocess.Popen('ls *[0-9][0-9][0-9][0-9][0-9][0-9]*', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdoutdata, stderrdata) = sysCmd.communicate()
    code = sysCmd.wait()

    if code < 0 or stderrdata:
        print('999999')
        if stderrdata:
            print(stderrdata)
        ret = -1
        if code < 0:
            ret = code
        sys.exit(ret)

    vfsFiles = re.compile(r'^cfield[0-9]{6}.*|^cs_[0-9]{6}.*|^nvfield[0-9]{6}.*|'
                           '^pfield[0-9]{6}.*|^sp_[0-9]{6}.*|^sp2_[0-9]{6}.*|^su0_[0-9]{6}.*|'
                           '^su1_[0-9]{6}.*|^su2_[0-9]{6}.*|^ufield[0-9]{6}.*|^vfield[0-9]{6}.*')
    retimestep = re.compile(r'^.+[^0-9]([0-9]{6})[^0-9].+$')
    recs = re.compile(r'^cs_')
    renv = re.compile(r'^nvfield')
    rep = re.compile(r'^pfield')
    reu = re.compile(r'^ufield')
    rev = re.compile(r'^vfield')

    files = stdoutdata.decode("utf-8").split('\n')
    if files[len(files)-1] == '':
        files.pop()

    for i in range(len(files)):
        if not vfsFiles.search(files[i]):
            files[i] = ''
            continue

        if not retimestep.match(files[i]):
            files[i] = ''
            continue

        timestep = retimestep.search(files[i])
        files[i] = '{} {}'.format(timestep.group(1), timestep.group(0))
    files.sort()


    i = 0
    # [0]: filename
    # [1]: number of files with this index
    # [2]: True is any file was too small.
    # [3]: bit array of required files.
    #      bit 0  (1): cs_
    #      bit 1  (2): nvfield
    #      bit 2  (4): pfield
    #      bit 3  (8): ufield
    #      bit 4 (16): vfield
    #      sum:   31
    cnt = [ [ '', 0, False, 0 ], [ '', 0, False, 0 ] ]
    for j in reversed(range(len(files))):
        # Found files that were ignored.  Stop here.
        if files[j] == '':
            break

        fileSplit = files[j].split()

        if cnt[i][0] == '':
            cnt[i][0] = fileSplit[0]

        if fileSplit[0] != cnt[i][0]:
            i += 1
            if i >= 2:
                break
            cnt[i][0] = fileSplit[0]

        cnt[i][1] += 1

        # If any file is too small, this iteration is incomplete.
        if os.path.getsize(fileSplit[1]) < 1024:
            cnt[i][2] = True

        # Make sure all required files exist.
        if recs.search(fileSplit[1]):
            cnt[i][3] += 1
        if renv.search(fileSplit[1]):
            cnt[i][3] += 2
        if rep.search(fileSplit[1]):
            cnt[i][3] += 4
        if reu.search(fileSplit[1]):
            cnt[i][3] += 8
        if rev.search(fileSplit[1]):
            cnt[i][3] += 16

    if cnt[0][1] == 0:
        print('999999')
        sys.exit(1)

    if len(sys.argv) < 2 or int(sys.argv[1]) < 0:
        mod = -1
    else:
        mod = int(sys.argv[1])

    if cnt[0][1] < cnt[1][1] or cnt[0][2] or cnt[0][3] != 31:
        print(modTimeStep(cnt[1][0], mod))
    else:
        print(modTimeStep(cnt[0][0], mod))


    sys.exit(0)


if __name__ == '__main__':
    lastTimeStep()
