import sys
import argparse
import os
from datetime import datetime, timedelta


def get_myfilesname(obj_path):
	all_file = os.listdir(obj_path)
	all_dirdate = []
	for name in all_file:
		if name.find('.') >= 0:
			continue
		all_dirdate.append(int(name[0:8]))  # xxxx year xx month xx day
	last_dirdate = max(all_dirdate)
	last_dirdate = datetime.strptime(
		str(last_dirdate)[0:4] + '-' + str(last_dirdate)[4:6] + '-' + str(last_dirdate)[6:8], "%Y-%m-%d")
	now_dirdate = last_dirdate + timedelta(days=7)  # next week
	now_dirdate = datetime.strftime(now_dirdate, "%Y-%m-%d")
	now_dirdate = now_dirdate.replace('-', '')

	final_obj_path = obj_path + '\\' + now_dirdate
	return final_obj_path, now_dirdate


def mkfiles(obj_path, now_dirdate):
	if os.path.exists(obj_path) is False:
		os.makedirs(obj_path)

	mdinfo = "## 本周工作"
	with open(obj_path + '\\罗程'+now_dirdate+'周报.md', 'a', encoding='utf-8') as f:
		for ll in mdinfo:
			f.write(ll)

	usrpfilepath = obj_path+'\\'+now_dirdate+"USRP"
	if os.path.exists(usrpfilepath) is False:
		os.makedirs(usrpfilepath)
	with open(usrpfilepath + '\\罗程'+now_dirdate+'USRP.md', 'a', encoding='utf-8') as f:
		for ll in mdinfo:
			f.write(ll)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--dirpath", type=str, default='./', help="Path of myReports workspace")
	args = parser.parse_args()
	# dirpath = 'E:/学习/周报/2024上半年'
	obj_path, now_dirdate = get_myfilesname(args.dirpath)
	mkfiles(obj_path, now_dirdate)

