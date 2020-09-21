import os
import csv
import time
import datetime

attendance = {}
timeAttendedKnown = {}
timeAttendedUnknown = {}
lecture_time = 50
lecture_percent = 85

with open('fname.txt') as fname:
  for rows in fname:
    list = rows.split(',')
    attendance[list[0]] = int(list[1])
    timeAttendedKnown[list[0]] = 0

if os.path.isfile('meetingAttendanceList ('+str(int(attendance["LECTURE"])+1)+').csv') or os.path.isfile('meetingAttendanceList.csv'):
  print("IN")
  end_time = datetime.datetime.strptime(time.ctime(os.path.getctime('meetingAttendanceList ('+str(int(attendance["LECTURE"])+1)+').csv')), "%c")
  with open('meetingAttendanceList ('+str(int(attendance["LECTURE"])+1)+').csv') as file:
    csv_reader = csv.reader((x.replace('\0', '') for x in file),delimiter='\t')
    next(csv_reader)
    for row in csv_reader:
      if len(row)==3:
        curr = datetime.datetime.strptime(row[2], '%m/%d/%Y, %I:%M:%S %p')
        result = (end_time - curr).seconds * ((row[1] == 'Joined') * 2 - 1)
        if row[0] in attendance:
            timeAttendedKnown[row[0]] += result
        else:
          if row[0] in timeAttendedUnknown:
            timeAttendedUnknown[row[0]] += result
          else:
            timeAttendedUnknown[row[0]] = result

  attendance['LECTURE']+=1
  with open('fname.txt','w') as f:
    for name in attendance.keys():
      if (timeAttendedKnown[name] > (lecture_time * lecture_percent * 0.6)):
        attendance[name] += 1
      f.write(('{},{},\n').format(name,attendance[name]))

  with open('fnameUnknown.txt','w') as f:
    for name in timeAttendedUnknown.keys():
      if (timeAttendedUnknown[name] > 2400):
        timeAttendedUnknown[name] = 1
      else:
        timeAttendedUnknown[name] = 0
      f.write(('{},{},\n').format(name,timeAttendedUnknown[name]))