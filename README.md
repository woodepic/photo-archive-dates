This project consists of two tools which make dating old photo backups (in my case, fom optical disks), much much easier. 

One tool moves a set of images from their raw data folder (direct from disk) to a folder based on date created (eg, a may 2005 folder).

The other tool (refine.py) determines the most accurate date for each file, and updates the date created for each file. This program uses various sources of dates to determine the correct creation date, including the date handwritten on the old, optical backup disks, the date in the filename, and the date created/modified flags.

main.py moves the files to dated folders
refine.py uses various search criteria to determine the most accurate date, and list that as the date created for each file.

The code is pretty simple, so just take a look to see more specifics.

To run:
1. python3 -m venv .venv
2. source .venv/bin/activate
3. python3 main.py OR python3 refine.py




