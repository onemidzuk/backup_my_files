import os
import time

source = ['/home/midzuk/PycharmProjects/', '/home/midzuk/Документы']

target_dir = '/media/midzuk/625CF2BD5CF28AD5/PyProj'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))


if os.system(zip_command) == 0:
    print('Backup is succesfully competed. Your copy is in', target)
else:
    print('Backup failed!')