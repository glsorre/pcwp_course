#!/usr/bin/python
import subprocess
import optparse
import os
import shutil
import platform
import signal

import psutil

# print(os.environ['HOME'])

# if platform.system() == 'Darwin':
#     print('macos')
# elif platform.system() == 'Linux':
#     print('linux')
# else:
#     print('windows')

# os.chdir('lesson6')
# print(os.getcwd())

# for item in os.listdir('.'):
#     print(item)

# os.makedirs('prova')

# for item in os.listdir('.'):
#     print(item)

# shutil.rmtree('prova')

# for item in os.listdir('.'):
#     print(item)

# shutil.chown(file, "600")
# os.symlink(linkPosition, link)

# os.path.join(dir, file)
# os.path.islink(position)
# os.path.isfile(position)
# os.path.exists(dir)
#os.kill(pid, signal.SIGKILL)



# for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
#     print(proc.info)

# os.kill(97866, signal.SIGKILL)

# subprocess.run("ls -l")

# import subprocess, signal
# p = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
# out, err = p.communicate()

# print(out)

# for word in out.split():
#     print(word)

if __name__ == "__main__":
    parser = optparse.OptionParser()

    parser.add_option("-u", "--update",
                    dest="update", default=True,
                    action="store_true",
                    help="update")

    parser.add_option("-s", "--setup",
                    dest="setup",
                    action="store_false",
                    help="setup")

    (opts, args) = parser.parse_args()

    if opts.update == True and opts.setup == False:
        print("update and setup")
    elif opts.setup == False:
        print("setup")
    elif opts.update:
        print("update")
