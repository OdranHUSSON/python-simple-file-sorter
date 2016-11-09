#!/bin/bash
echo "Cleaning .part files"
find /var/www/download/Telechargements -name "*.part" -type f
find /var/www/download/Telechargements -name "*.part" -type f -delete
echo "Cleaning nfo files"
find /var/www/download/Telechargements -name "*.nfo" -type f
find /var/www/download/Telechargements -name "*.nfo" -type f -delete
echo "Removing empty folders"
find /var/www/download/Telechargements -empty -type d 
find /var/www/download/Telechargements -empty -type d -delete
