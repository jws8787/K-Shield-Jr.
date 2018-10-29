import platform
import os
import re

def get_process_list() :
	my_os = platform.system()

	if(my_os == 'Linux') :
		all_ps = os.popen('ps -a').read()
		process_list = re.findall(":\d\d\s([\w_\-\.]+)", all_ps)

		return process_list

	elif(my_os == 'Windows'):
		process_list = ['System Idle Process', 'System', 'Registry', 'Memory Compression']

		regex = re.compile(".*[.]exe\s", re.I)
		all_ps = os.popen('tasklist').read()
	
		for process in regex.findall(all_ps) :
			process_list.append(process)

		return process_list

	return False

if __name__ == '__main__' :
	process_list = get_process_list()
	for x in process_list :
		print(x)