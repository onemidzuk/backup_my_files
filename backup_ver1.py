import os
import time

source = ['/home/midzuk/PycharmProjects/', '/home/midzuk/Документы']

target_dir = '/media/midzuk/625CF2BD5CF28AD5/PyProj'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
print("Catalogue succesfully created!")

#target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

target = today + os.sep + now + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))


if os.system(zip_command) == 0:
    print('Backup is succesfully competed. Your copy is in', target)
else:
    print('Backup failed!')