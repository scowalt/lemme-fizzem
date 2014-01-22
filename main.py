import os
import re
import shutil
import sys
import win32api

# http://stackoverflow.com/a/9269316/1222411
DIRECTORY_REGEX = r"RADS\\projects\\lol_air_client\\releases\\(?P<version>[0-9\.]+?)\\deploy\\assets\\sounds\\(?P<language>[a-z]{2}\_[A-Z]{2}?)\\[Cc]hampions"
BAD_REGEX = r"\\\$RECYCLE\.BIN\\" # avoids trying to modify a deleted League of Legends installation

def replace_sounds_with_champ(root_folder, champion):
	rex = re.compile(r"^.*%s\.mp3\.bak"%sys.argv[1])
	
	# Find sound file for champion
	champion_file = None
	for root,dirs,files in os.walk(root_folder):
		for f in files:
			result = rex.search(f)
			if result:
				champion_file = os.path.join(root, f)
				break

	if not champion_file:
		print "Couldn't find champion " + champion
		restore_files(root_folder)
		return
	
	for root,dirs,files in os.walk(root_folder):
		for f in files:
			new_f = f[:len(f) - 4] #remove .bak extention from file name
			shutil.copyfile(os.path.join(root, champion_file), os.path.join(root, new_f))


def restore_files(root_folder):
	print "Restoring files in " + root_folder
	rex = re.compile(r"^.*\.(bak)")
	for root,dirs,files in os.walk(root_folder):
		for f in files:
			result = rex.search(f)
			if result:
				new_f = f[:(len(f) - 4)] # chop off .bak extension
				try:
					os.remove(os.path.join(root, new_f))
				except WindowsError as e:
					print str(e)
					pass
				try:
					os.rename(os.path.join(root, f), os.path.join(root, new_f)) #restore file
				except WindowsError as e:
					print str(e)
					pass

def backup_files(root_folder):
	rex = re.compile(r"^.+\.(bak)")
	for root,dirs,files in os.walk(root_folder):
		for f in files:
			backed_up = rex.match(f)
			if not backed_up:
				new_f = f + ".bak"
				os.rename(os.path.join(root,f), os.path.join(root, new_f))

# http://stackoverflow.com/a/13068033/1222411
def find_dir(root_folder, rex):
	bad = re.compile(BAD_REGEX)
	for root,dirs,files in os.walk(root_folder):
		for d in dirs:
			full_dir = os.path.join(root,d)
			champion_directory = rex.search(full_dir)
			bad_directory = bad.search(full_dir)
			if champion_directory and not bad_directory:
				if sys.argv[1] == 'restore':
					restore_files(full_dir)
				else:
					backup_files(full_dir)
					replace_sounds_with_champ(full_dir, sys.argv[1])


# http://stackoverflow.com/a/13068033/1222411
def find_dir_in_all_drives(dir_name):
	#create a regular expression for the file
	rex = re.compile(dir_name)
	drives = win32api.GetLogicalDriveStrings().split('\000')[:-1]
	for drive in drives:
		print "Scanning drive " + str(drive) + " for League of Legends installation"
	 	find_dir( drive, rex )

if len(sys.argv) is not 2:
	print "Wrong arguments"
else:
	find_dir_in_all_drives(DIRECTORY_REGEX)