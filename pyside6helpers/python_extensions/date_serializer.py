from datetime import date
import dateparser


class DateSerializer:

    @staticmethod
    def serialize(date_):
        return date_.strftime('%x')  # Use locale

    @staticmethod
    def deserialize(text: str, month: int = None, year: int = None):
        try:
            day = int(text)
            return date(year, month, day)
        except ValueError:
            pass

        return dateparser.parse(text)  # FIXME: check locale
