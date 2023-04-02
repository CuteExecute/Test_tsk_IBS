from datetime import datetime, timedelta


def get_utcnow():
    return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')


def difference_time(first_date_time_string, second_date_time_string):
    def date_time_formatter(incoming_string):
        def restruct_datetime_string(inc_str):
            res = inc_str.split(".")[0]
            res = res.replace('T', ' ')
            return res

        date_string = restruct_datetime_string(incoming_string)
        date_formatter = "%Y-%m-%d %H:%M:%S"
        return datetime.strptime(date_string, date_formatter)

    first_date_time = date_time_formatter(first_date_time_string)
    second_date_time = date_time_formatter(second_date_time_string)

    return abs(first_date_time - second_date_time)
