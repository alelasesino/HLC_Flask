
import datetime

def format_date(date):
    d = datetime.datetime.strptime(str(date), '%Y-%m-%d')
    return d.strptime(d.strftime('%d-%m-%Y'), '%d-%m-%Y')