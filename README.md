# Python File sorter
----
## Simple python file sorter 
Odran HUSSON
https://odran-husson.fr

Simple tool to recursivly and automaticly sort files in asked repertory

## Usage
Change the following lines to your wanted outputs folders : 
```python
"Configuration"
movies_folder="/var/www/html/file-manager/Films/"
series_folder="/var/www/html/file-manager/Series/"
music_folder="/var/www/html/file-manager/Musique/"
```

To sort a folder execute :
```
python sort_dir.py /home/user/folder_to_sort
```

## Sample output
python sort_dir.py movie/
```
Results for folder "/var/www/html/file-sorter/Arrow2" :
	0  audio file(s)
	5  video file(s)
	0  sub folder(s)
Multiple movies or series :
	Moving "Arrow.S03E05.avi" to Series folder
	Moving "Arrow.S03E01.avi" to Series folder
	Moving "Arrow.S03E03.avi" to Series folder
	Moving "Arrow.S03E02.avi" to Series folder
	Moving "Arrow.S03E04.avi" to Series folder
Results for folder "/var/www/html/file-sorter/FILM" :
	0  audio file(s)
	0  video file(s)
	0  sub folder(s)
No match !

```

