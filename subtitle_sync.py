import os
import sys


def sync_fuc(file, sync_num):
    f = open(file, 'r')
    fr = open(file.split('.')[0] + '_' + sync_num + '.smi', 'w')
    line = True

    while line:

        line = f.readline()
        print(line, end='')

        if 'SYNC Start' in line:
            cur_sync = line[line.index('=') + 1:line.index('>')]
            cur_sync = int(cur_sync) + int(float(sync_num)*1000)
            line = line[:line.index('=') + 1] + \
                str(cur_sync) + line[line.index('>'):]

            print(line, end='')
            fr.write(line)

        else:
            fr.write(line)

    fr.close()


if __name__ == "__main__":

    file_name = sys.argv[1]
    sync_num = sys.argv[2]

    sync_fuc(file_name, sync_num)
    # fuck
