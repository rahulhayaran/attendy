import time
import serial
import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename

# TO = 'attendy196@gmail.com'
# FROM = 'attendy196@gmail.com'
# USERNAME = 'attendy196'
# PASSWORD = 'attendyrocks'

# ser = serial.Serial('COM3', 9600)
port = "/dev/tty.HC-06-DevB"
ser = serial.Serial(port, 9600)
ser.flushInput()

'''def send_email(TEXT):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(USERNAME, PASSWORD)
    server.sendmail(FROM, TO, TEXT)
    server.quit()'''

def send_mail(send_from: str, subject: str, text: str, send_to: list, files=None):
    send_to = default_address if not send_to else send_to

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = ', '.join(send_to)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            ext = f.split('.')[-1:]
            attachedfile = MIMEApplication(fil.read(), _subtype = ext)
            attachedfile.add_header(
                'content-disposition', 'attachment', filename=basename(f) )
        msg.attach(attachedfile)

    smtp = smtplib.SMTP(host="smtp.gmail.com", port= 587)
    smtp.starttls()
    smtp.login(username,password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

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
    52: 'Isabelle Zhou'
}

absent_header = 'The following students were absent:\n'
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

def read_id(b):
    id = []
    while b != 'e':
        id.append(b)
        b = ser.read()
    return id

while datetime.datetime.now().hour < 15:
    id_num = read_id(ser.read())
    if id_num == 100:
        break
    time_here = datetime.datetime.now()
    hour_here = time_here.hour
    minute_here = time_here.minute
    print(id_num)
    if type(id_num) == int:
        if hour_here < 14 or (hour == 4 and minute_here <= 11):
            present_list.append(met_2022[int(id_num)])
        else:
            late_list.append(met_2022[int(id_num)])
    here_list = present_list + late_list
    for num, name in met_2022.items():
        if name not in here_list:
            absent_list.append(name)
    TEXT = absent_header + print_list(absent_list) + late_header + print_list(late_list) + present_header + print_list(present_list)
    username = 'attendy196'
    password = 'attendyrocks'
    default_address = ['attendy196@gmail.com']

    send_mail(send_from = username,
    subject = "test",
    text = TEXT,
    send_to = None,
#    files = ['C:\\Users\\rahul\\Desktop\\MET\\fall18\\ugba10\\module1']
    )
    time.sleep(0.5)
