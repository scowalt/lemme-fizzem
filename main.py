import os
import re
import win32api

def restore_files(root_folder):
	rex = re.compile(r"^.*\.(bak)")
	# delete all non-backup files
	for root,dirs,files in os.walk(root_folder):
		for f in files:
			result = rex.search(f)
			if not result:
				os.remove(root+f) # delete non-bacup files
	# restore backed-up files
	for root,dirs,files in os.walk(root_folder):
		for f in files:
			result = rex.search(f)
			if result:
				new_f = f[:(len(f) - 4)] # chop off .bak extension
				os.rename(root+f, root+new_f) #restore file

def backup_files(root_folder):
	for root,dirs,files in os.walk(root_folder):
		for f in files:
			os.rename(root+f, root+f+".bak")

# http://stackoverflow.com/a/13068033/1222411
def find_dir(root_folder, rex):
	for root,dirs,files in os.walk(root_folder):
		for d in dirs:
			full_dir = root + d
			result = rex.search(full_dir)
			if result:
				print os.path.join(root,d)

# http://stackoverflow.com/a/13068033/1222411
def find_dir_in_all_drives(dir_name):
	#create a regular expression for the file
	rex = re.compile(dir_name)
	for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
		print "Scanning drive " + str(drive)
		find_dir( drive, rex )

# http://stackoverflow.com/a/9269316/1222411
find_dir_in_all_drives(r"lol_air_client\\releases\\(?P<version>[0-9\.]+?)\\deploy\\assets\\sounds\\(?P<language>[a-zA-Z\_]+?)")