from enum import Enum

class CalendarRequest(Enum):
    DAYOFWEEK = 1
    SPECIFICDATE = 2
    ERROR = 3

    @staticmethod
    def get_type(class_string):
        print(class_string)
        if class_string == "day of week":
            return Calendar_Request.DAYOFWEEK
        elif class_string == "specific date":
            return Calendar_Request.SPECIFICDATE
        else:
            print("getType() Error")
            return Calendar_Request.ERROR
