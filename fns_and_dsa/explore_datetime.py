from datetime import datetime, timedelta
import datetime

def display_current_datetime():
    now = datetime.datetime.now()
    current_date = now.date()
    print(f"Current date and time: {now.strftime("%Y-%m-%d %H:%M:%S")}")



def  calculate_future_date ():
    days_ahead = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.datetime.now() + datetime.timedelta(days=days_ahead)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()