from sqlalchemy import types
from datetime import datetime


def mapper(sql_type):
    if isinstance(sql_type, types.Integer):
        return "int"
    elif isinstance(sql_type, types.String):
        return "str"
    elif isinstance(sql_type, types.DateTime):
        return datetime
    elif isinstance(sql_type, types.Float):
        return "float"
    elif isinstance(sql_type, types.Boolean):
        return "bool"
    elif isinstance(sql_type, types.Date):
        return "datetime.date"
    elif isinstance(sql_type, types.Time):
        return "datetime.time"
    else:
        return "str"
