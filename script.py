import os
import sys

def appendedname(prefix, filepath):
	lis = filepath.split('/')
	file_name = lis[-1]
	newfile_name = prefix + " " + file_name
	lis[-1] = newfile_name
	return "/".join(lis)

def recurse_dir(prefix, filename):
	init = filename
	val = os.listdir(init)
	for i in val:
		newfile = init+"/"+i
		# print newfile
		if os.path.isdir(newfile):
			recurse_dir(prefix, newfile)
		else:
			if newfile == "./script.py":
				continue
			prefixed_name = appendedname(prefix, newfile)
			os.rename(newfile, prefixed_name)

def main():
	number = len(sys.argv)
	if(number!=3):
		if(number<3):
			print "Too less arguments specified. Please follow the format given in README."
		else:
			print "More number of arguements are passed. Please follow the format given in README"
		sys.exit()
	print "This Change is PERMANENT. Are you sure you want to continue? [Y/N]"
	choice = raw_input()
	if choice=="Y":
		filepath = sys.argv[1]
		prefix = sys.argv[2]
		recurse_dir(prefix, filepath)

if __name__ == '__main__':
	main()