# gdownloader
Python script to download google drive files from command line

## Usage:
	./gdownloader.py <URL>
Input can be the entire URL of google drive file, or driveID. Make sure that gdownloader.py is executable, otherwise run with:

	python gdownloader.py <URL>

## Options:
	--large               Use when downloading large files.
	--output <filename>   Specify output filename (default filename is driveID).

## Example:
	./gdownloader.py https://drive.google.com/open?id=1rk65W3AJn7LNgrnPjpqvK3iO3vT28 --large
