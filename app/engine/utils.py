import json
from datetime import datetime

required_keys = {"dt_from", "dt_upto", "group_type"}

required_group_types = ("month", "day", "hour")

# inputed datetime required fommat
datetime_format_from = "%Y-%m-%dT%H:%M:%S"


def validate_request(text: str) -> bool | dict:
    """validate user input"""

    try:
        input_json = json.loads(text)

        if set(input_json.keys()) == required_keys:

            dt_from = input_json["dt_from"]
            dt_upto = input_json["dt_upto"]
            group_type = input_json["group_type"]

            if group_type not in required_group_types:
                return False

            try:
                dt_from_ = datetime.strptime(dt_from, datetime_format_from)
                dt_upto_ = datetime.strptime(dt_upto, datetime_format_from)

                input_json["dt_upto"] = dt_upto_
                input_json["dt_from"] = dt_from_

            except ValueError:
                return False

            if dt_from_ >= dt_upto_:
                return False

        return input_json
    except (json.JSONDecodeError, KeyError):
        return False

