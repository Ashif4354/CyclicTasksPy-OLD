from datetime import datetime, timedelta

def get_ist_time():
    utc_now = datetime.utcnow()
    ist_now = utc_now + timedelta(hours=5, minutes=30)
    return ist_now.strftime('%d-%m-%Y %H:%M:%S')
