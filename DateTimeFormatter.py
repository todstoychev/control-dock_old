from datetime import datetime


class DateTimeFormatter:
    @staticmethod
    def format_string(input_str: str, format_str: str):
        return datetime.strptime(input_str, format_str)