import os
import sys
import re
import shutil

def main():

    print("Starting Loop...")

    monthly_folders = "Pics/Monthly Folders"
    photos_from_discs = "Pics/Photos from disks"

    i=0
    k=0
    for subdir, dirs, files in os.walk(photos_from_discs):
        for file in files:
            if i % 1 == 0:
                print(file)
                regexResult = re.search(r"(20)?([0-9][0-9])-([0-1][0-9])-([0-3][0-9])", file)
                if regexResult:
                    year = regexResult.group(2)
                    month = regexResult.group(3)
                    day = regexResult.group(4)

                    if int(year) <= 23:
                        fullYear = "20"+year
                    else:
                        fullYear = "19"+year

                    filename = os.path.join(subdir, file)
                    
                    dirName = _dateToDirName(fullYear, month)
                    dirPath = os.path.join(monthly_folders, dirName)
                    _create_directory(dirPath) #Create the directory if it doesn't exist

                    dest = os.path.join(dirPath, file)

                    num = 0
                    while os.path.exists(dest):
                        num += 1
                        period = file.rfind('.')
                        if period == -1:
                            period = len(file)

                        new_file = f'{file[:period]}({num}){file[period:]}'
                        dest = os.path.join(dirPath, new_file)

                    shutil.move(filename, dest)

                    # print("    "+filename)
                    # print("    "+dest)
                    k = k+1
            i = i+1


            # if k==1: #limit to 100 files
            #     sys.exit(0)




def _create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def _dateToDirName(fullYear: str, month: str) -> str:
    if month == "01":
        monthName = "Jan"
    elif month == "02":
        monthName = "Feb"
    elif month == "03":
        monthName = "Mar"
    elif month == "04":
        monthName = "Apr"
    elif month == "05":
        monthName = "May"
    elif month == "06":
        monthName = "Jun"
    elif month == "07":
        monthName = "Jul"
    elif month == "08":
        monthName = "Aug"
    elif month == "09":
        monthName = "Sep"
    elif month == "10":
        monthName = "Oct"
    elif month == "11":
        monthName = "Nov"
    elif month == "12":
        monthName = "Dec"

    return (monthName + " " + fullYear)

if __name__ == "__main__":
    main()