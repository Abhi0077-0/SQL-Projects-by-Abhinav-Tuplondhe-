from datetime import date
import pandas as pd
from deta import app
from send_email import send_email



SHEET_ID = "1ENRGKf4dcU2NrJAJetUKoSFoS9shtkENUv5y6f2ncRs"
SHEET_NAME = "Sheet1"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"


def load_df(url):
    parse_dates = ["scheduled_date"]
    df = pd.read_csv(url, parse_dates=parse_dates)
    return df


def query_data_and_send_emails(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if (present >= row["scheduled_date"].date()):
            send_email(
                subject=f'[Coding Is Fun]',
                receiver_email=row["email"],
                name=row["name"]
            )
            email_counter += 1
    return f"Total Emails Sent: {email_counter}"


@app.lib.cron()
def cron_job(event):
    df = load_df(URL)
    result = query_data_and_send_emails(df)
    return result