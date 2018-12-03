import time
import serial
import smtplib
import datetime

TO = 'attendy196@gmail.com'
FROM = 'attendy196@gmail.com'
USERNAME = 'attendy196'
PASSWORD = 'attendyrocks'

ser = serial.Serial('COM3', 9600)
'''def send_email(TEXT):
    print('Sending Email')
    smtpserver = smtplib.SMTP('smtp.gmail.com',587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject:' + SUBJECT + '\n'
    print(header)
    msg = header + '\n' + TEXT + ' \n\n'
    smtpserver.sendmail(GMAIL_USER, TO, msg)
    smtpserver.close()'''

def send_email(TEXT):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(USERNAME, PASSWORD)
    server.sendmail(FROM, TO, TEXT)
    server.quit()

met_2022 = {
    1: 'Rimika Banerjee',
    2: 'Sravya Basvapatri',
    3: 'Ryan Chen',
    4: 'Luofei Chen',
    5: 'Kai Chorazewicz',
    6: 'Ashvin Dhawan',
    7: 'Quin Etnyre',
    8: 'Jahnvi Doshi',
    9: 'Charlie Faramarzi',
    10: 'Diego Gonzalez',
    11: 'Chai Goyal',
    12: 'Alara Guler',
    13: 'Amy Guo',
    14: 'Shiyuan Guo',
    15: 'Matt Hallac',
    16: 'Kelly Han',
    17: 'Rahul Hayaran',
    18: 'Neha Hudait',
    19: 'Francis Indaheng',
    20: 'Ayush Jain',
    21: 'Daniel Jing',
    22: 'Nishi Kaza',
    23: 'Andrew Kirillov',
    24: 'Elliot Larson',
    25: 'Aadhrik Kuila',
    26: 'Sean Lin',
    27: 'Chelsea Lo',
    28: 'Richard Liu',
    29: 'Nikhil Mandava',
    30: 'Alexander Manes',
    31: 'Michael McNabb',
    32: 'Ethan Mehta',
    33: 'Erel Saul',
    34: 'Rishma Murugan',
    35: 'Neha Nagabothu',
    36: 'Deven Navani',
    37: 'Dev Ojha',
    38: 'Harish Palani',
    39: 'Anika Ramachandran',
    40: 'Manav Rathod',
    41: 'Alfonso Sanchez',
    42: 'Birkaran Sachdev',
    43: 'David Shau',
    44: 'Vikram Shirsat',
    45: 'Jaiveer Singh',
    46: 'Austin Sun',
    47: 'Prangan Tooteja',
    48: 'Michael Trehan',
    49: 'Julius Vering',
    50: 'Hannah Vinh',
    51: 'Vincent Wang',
    52: 'Isabelle Zhou',
}

absent_header = '\nThe following students were absent:\n'
late_header = '\nThe following students were late:\n'
present_header = '\nThe following students were present and on time:\n'

absent_list = []
late_list = []
present_list = []
here_list = []

def print_list(a_list):
    string_list = ''
    for element in a_list:
        string_list += str(element) + "\n"
    return string_list

#while datetime.datetime.now().hour < 15:
roster_dir = str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day) + 'attendance_log' + '.csv'
roster = open(roster_dir, "w")
roster.write('On Time, Tardy, Absent\n')
while datetime.datetime.now().minute < 53:
    id_num = ser.readline().decode("utf-8")
    id_num = [int(s) for s in id_num.split() if s.isdigit()][0]
    time_here = datetime.datetime.now()
    hour_here = time_here.hour
    minute_here = time_here.minute
    print(id_num)
    if type(id_num) == int:
        if hour_here < 14 or (hour_here == 14 and minute_here <= 10):
            roster.write(met_2022[int(id_num)] + '\n')
            if met_2022[int(id_num)] not in present_list:
                present_list.append(met_2022[int(id_num)])
        else:
            roster.write(' ' + ',' + met_2022[int(id_num)] + '\n')
            if met_2022[int(id_num)] not in late_list:
                late_list.append(met_2022[int(id_num)])
    time.sleep(0.5)
here_list = present_list + late_list
for num, name in met_2022.items():
    if name not in here_list:
        roster.write(' ' + ',' + ' ' + ',' + name + '\n')
        absent_list.append(name)
TEXT = absent_header + print_list(absent_list) + late_header + print_list(late_list) + present_header + print_list(present_list)
send_email(TEXT)
