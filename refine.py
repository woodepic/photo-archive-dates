import os
import sys
import re
import shutil
import datetime
import filedate
from pathlib import Path

def main():

    print("Starting Loop...")

    monthly_folders = "Pics/Monthly Folders"

    i=0
    k=0
    for subdir, dirs, files in os.walk(monthly_folders):
        for file in files:
            if i % 1 == 0:
                dirRegexResult = re.search(r"\/([A-Z][a-z][a-z]) (\d\d\d\d)", subdir)

                if dirRegexResult:
                    filename = os.path.join(subdir, file)
                    dirMonthStr = dirRegexResult.group(1)
                    dirYear = dirRegexResult.group(2)

                    print("folder date: "+dirMonthStr+" "+dirYear)

                    currentFile = fileDetails(filename)
                    #print(currentFile)

                    if currentFile.realDateknown:
                        #set date to real date
                        _setFileDate(currentFile.filepath, 
                                    currentFile.rl_year_cr, 
                                    currentFile.rl_month_cr,
                                    currentFile.rl_day_cr,
                                    currentFile.os_hour_cr,
                                    currentFile.os_min_cr,
                                    currentFile.os_sec_cr)
                        pass
                    elif currentFile.os_month_cr == dirMonthStr and currentFile.os_year_cr == dirYear:
                        #this is the correct date so leave it
                        pass
                    else:
                        #the date is totally wrong, so just change it to a specific date within the folder month
                        dirMonthInt = _monthWordToInt(dirMonthStr)
                        _setFileDate(currentFile.filepath, 
                                    dirYear, 
                                    dirMonthInt,
                                    "01",
                                    currentFile.os_hour_cr,
                                    currentFile.os_min_cr,
                                    currentFile.os_sec_cr)
                        pass



                    k = k+1
            i = i+1
            # if k==10: #limit to 100 files
            #     sys.exit(0)

def _monthWordToInt(month: str) -> str:
    if month == "Jan":
        return "01"
    elif month == "Feb":
        return "02"
    elif month == "Mar":
        return "03"
    elif month == "Apr":
        return "04"
    elif month == "May":
        return "05"
    elif month == "Jun":
        return "06"
    elif month == "Jul":
        return "07"
    elif month == "Aug":
        return "08"
    elif month == "Sep":
        return "09"
    elif month == "Oct":
        return "10"
    elif month == "Nov":
        return "11"
    elif month == "Dec":
        return "12"
    else:
        return None

def _setFileDate(filepath: str, year: str, month: str, day: str, hour: str, min: str, sec: str):
    os.system('SetFile -m "{}" "{}"'.format((month+"/"+day+"/"+year+" "+hour+":"+min+":"+sec), filepath))
    #     #setFile -d <mm/dd/yyyy> <FILE>
    #     #mm/dd/[yy]yy [hh:mm:[:ss]



class fileDetails:
    def __init__(self, filepath):
        self.filepath = filepath
        self.realDateknown = False
        self.os_year_cr = None
        self.os_month_cr = None
        self.os_day_cr = None
        self.os_hour_cr = None
        self.os_min_cr = None
        self.os_sec_cr = None
        self.rl_year_cr = None
        self.rl_month_cr = None
        self.rl_day_cr = None

        #assume the file exists
        rawDateTimeStr = str(datetime.datetime.fromtimestamp(os.stat(filepath).st_birthtime))
        osDateRegexResult = re.search(r"(\d\d\d\d)-(\d\d)-(\d\d) (\d\d):(\d\d):(\d\d)", rawDateTimeStr)
        if osDateRegexResult:
            self.os_year_cr = osDateRegexResult.group(1)
            self.os_month_cr = osDateRegexResult.group(2)
            self.os_day_cr = osDateRegexResult.group(3)
            self.os_hour_cr = osDateRegexResult.group(4)
            self.os_min_cr = osDateRegexResult.group(5)
            self.os_sec_cr = osDateRegexResult.group(6)
        
        filenameDetailsRegex = re.search(r"(20)?([0-9][0-9])-([0-1][0-9])-([0-3][0-9])", filepath)
        if filenameDetailsRegex:
            self.realDateknown = True

            tempYr = filenameDetailsRegex.group(2)
            self.rl_month_cr = filenameDetailsRegex.group(3)
            self.rl_day_cr = filenameDetailsRegex.group(4)

            if int(tempYr) < 23:
                self.rl_year_cr = "20"+tempYr
            else:
                self.rl_year_cr = "19"+tempYr

    def __str__(self):
        if not self.realDateknown:
            return  f"File path: {self.filepath}\n\
    os_year_cr: {self.os_year_cr}\n\
    os_month_cr: {self.os_month_cr}\n\
    os_day_cr: {self.os_day_cr}\n\
    os_hour_cr: {self.os_hour_cr}\n\
    os_min_cr: {self.os_min_cr}\n\
    os_sec_cr: {self.os_sec_cr}\n"
        else:
            return  f"File path: {self.filepath}\n\
    os_year_cr: {self.os_year_cr}\n\
    os_month_cr: {self.os_month_cr}\n\
    os_day_cr: {self.os_day_cr}\n\
        rl_year_cr: {self.rl_year_cr}\n\
        rl_month_cr: {self.rl_month_cr}\n\
        rl_day_cr: {self.rl_day_cr}\n\
    os_hour_cr: {self.os_hour_cr}\n\
    os_min_cr: {self.os_min_cr}\n\
    os_sec_cr: {self.os_sec_cr}\n"
                    


        

        

if __name__ == "__main__":
    main()