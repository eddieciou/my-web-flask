from datetime import datetime
import pytz


class DateTimeUtil:
    """時間轉換相關操作:
    Str
    Dto (DateTimeObj)
    Int (UTCTimeStamp)
    """
    YmdHMS_FORMAT = "%Y-%m-%d %H:%M:%S"
    YmdH_FORMAT = "%Y-%m-%d %H"
    TZ = pytz.timezone('Asia/Taipei')
    EST = pytz.timezone('US/Eastern')

    @staticmethod
    def get_now_dtm_obj():
        """ex. 2018-08-24 13:07:06.276367 <class 'datetime.datetime'>"""
        return datetime.utcnow()
