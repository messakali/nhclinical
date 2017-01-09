# -*- coding: utf-8 -*-
"""Contains various useful methods for managing datetimes."""
from datetime import datetime

from openerp import models
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT as DTF


class DatetimeUtils(models.AbstractModel):

    _name = 'datetime_utils'

    @classmethod
    def zero_microseconds(cls, date_time):
        """
        Return the passed date_time with any microseconds set to 0.

        :param date_time:
        :type date_time: datetime or str
        :return:
        """
        if isinstance(date_time, str):
            date_time = datetime.strptime(date_time, DTF)
        date_time = date_time.replace(microsecond=0)
        return date_time.strftime(DTF)

    @classmethod
    def zero_seconds(cls, date_time):
        """
        Return the passed date_time with any seconds and microseconds set to 0.

        :param date_time:
        :type date_time: datetime
        :return:
        """
        if not isinstance(date_time, datetime):
            raise TypeError("Datetime object required but {} was passed."
                            .format(type(date_time)))
        return date_time.replace(second=0, microsecond=0)

    @classmethod
    def reformat_server_datetime_for_frontend(cls, date_time,
                                              date_first=False):
        """
        Reformat a datetime in Odoo's 'default server datetime format'
        (see imports) to one more appropriate for the front end.

        Can choose whether the date or time comes first.

        :param date_time:
        :type date_time: str
        :param date_first:
        :type date_first: bool
        :return:
        :rtype: str
        """
        date_time = cls.zero_microseconds(date_time)
        date_time = datetime.strptime(date_time, DTF)
        date = '%d/%m/%Y'
        time = '%H:%M'
        format_string = '{} {}'
        if date_first:
            datetime_format = format_string.format(date, time)
        else:
            datetime_format = format_string.format(time, date)
        date_time = date_time.strftime(datetime_format)
        return date_time
