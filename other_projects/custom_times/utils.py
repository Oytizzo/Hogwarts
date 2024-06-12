import re


def convert_to_seconds(time_str: str, format: str):
    if format in ("D days HH:MM:SS", "d days hh:mm:ss"):
        days, hours, minutes, seconds = re.findall(r'(\d+) days (\d+):(\d+):(\d+)', time_str)[0]
        total_seconds = int(days) * 24 * 60 * 60 + int(hours) * 60 * 60 + int(minutes) * 60 + int(seconds)

        return total_seconds


if __name__ == "__main__":
    total_sec = convert_to_seconds("2 days 01:10:05", "D days HH:MM:SS")
    print(total_sec)
    print(type(total_sec))
