import datetime



strptime_formats = {
    'The Moscow Times': '%A, %B %d, %Y',
    'The Guardian': '%A, %d.%m.%y',
    'Daily News': '%A, %d %B %Y',
}

while True:
    try:
        inp = input("Enter date: ")
    except (EOFError, KeyboardInterrupt):
        print("Stop program")
        exit(1)
    if not inp:
        print("Stop program")
        exit(1)

    date_source, raw_date = inp.split('—')
    date_format = strptime_formats.get(date_source.strip())
    if not date_format:
        print(f"Not valid date format: {date_source}")
        continue
    print(datetime.datetime.strptime(raw_date.strip(), date_format))