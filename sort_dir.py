#!/bin/python
import glob, os, sys, shutil, re

# Odran HUSSON
# odran-husson.fr

"Configuration"
movies_folder="/var/www/download/Films/"
series_folder="/var/www/download/Series/"
music_folder="/var/www/download/Musique/"

"Gettings directory in arguments"
if len(sys.argv) != 2:
	sys.exit("Usage : "+sys.argv[0]+" directory")
else :
	directory_to_scan = sys.argv[1]
	if(directory_to_scan[-1:] == "/"):
		directory_to_scan = directory_to_scan[:-1]
		print directory_to_scan

"App vars"
cwd=os.getcwd()
total_audio_files = 0
total_video_files = 0
total_sub_folders = 0
audio_extensions = ("*.mp3","*.flac")
video_extensions = ("*.avi","*.mkv","*.mov","*.mp4")

"Functions"
def search_extensions( directory,extensions ):
	if(os.path.isdir( directory )) :
		"Moving to directory"
		os.chdir( directory )
		"Searching for files"
		matchs=[]
		for extension in extensions:
			matchs.extend(glob.glob(extension))
		os.chdir( cwd )
		return len(matchs)
	else :
		return 0;

def search_audio_files( directory ):
	if(os.path.isdir( directory )) :
		return search_extensions( directory, audio_extensions );
	else :
		return 0;

def search_video_files( directory ):
	if(os.path.isdir( directory )) :
		return search_extensions( directory, video_extensions );
	else :
		return 0;

def scan( directory ):
	if(os.path.isdir( directory )) :
		"Searching for files"
		global total_audio_files
		global total_video_files
		global total_sub_folders

		total_audio_files += search_audio_files( directory );
		total_video_files += search_video_files( directory );

		"Searching for folders"
		for file in os.listdir( directory ):
			if os.path.isdir( directory+"/"+file ):
				scan( directory+"/"+file )
				total_sub_folders+=1
		return;
	else :
		return 0;

def move_movies(directory):
	global series_folder
	global movies_folder

	series_regex = "(.*)S([0-9]{2})E([0-9]{2}).*(\..{3})"
	os.chdir( directory )
	matchs=[]
	for extension in video_extensions:
		matchs.extend(glob.glob(extension))
	for movie in matchs:
		m = re.match(series_regex, movie)
		if m:
			#Series file
			name = m.group(1)+"S"+m.group(2)+"E"+m.group(3)+m.group(4)
			if not os.path.isdir( series_folder+m.group(1)[:-1] ):
				os.mkdir( series_folder+m.group(1)[:-1])
			if not os.path.isdir( series_folder+m.group(1)[:-1] + "/" + "S"+m.group(2)):
				os.mkdir( series_folder+m.group(1)[:-1]+ "/" + "S"+m.group(2))
			print "\tMoving \""+name+"\" to Series folder"
			os.rename(movie,series_folder+m.group(1)[:-1]+ "/" + "S"+m.group(2)+"/"+name)
		else :
			print "\tMoving \""+movie+"\" to Movie folder"
			os.rename(movie,movies_folder+movie)
	os.chdir( directory_to_scan )


def show_result(directory):
	global total_audio_files
	global total_video_files
	global total_sub_folders
	
	print "Results for folder \""+directory+"\" :"
	print "\t",total_audio_files," audio file(s)"
	print "\t",total_video_files," video file(s)"
	print "\t",total_sub_folders," sub folder(s)"

	if ( total_sub_folders == 0 and total_video_files > 0 and total_audio_files < total_video_files):
		#Multiple video files can be multiple movies or series
		print "Multiple movies or series :"
		file = directory.split('/')[-1]
		move_movies(directory)
		os.chdir(cwd)
	elif (total_sub_folders >= 0 and total_audio_files > 0):
		#Band / album
		print "Seems like a band / album"
		file = directory.split('/')[-1]
		print "Moving \""+directory+"/"+file+"\" to Music folder / "+file
		shutil.move(directory+"/",music_folder+"/"+file)
	else :
		#No match
		print "No match !"
	total_audio_files = 0
	total_video_files = 0
	total_sub_folders = 0
	video_files = []


for file in os.listdir( directory_to_scan ):
	move_movies(directory_to_scan)
	if os.path.isdir( directory_to_scan+"/"+file ):
		scan( directory_to_scan+"/"+file )
		show_result( directory_to_scan+"/"+file )
