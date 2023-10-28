import json

from pymongo.collection import Collection

from app.data import Config
from app.engine.db.db import get_db

from pymongo import MongoClient

from datetime import datetime
from dateutil.relativedelta import relativedelta


def aggregate_salary_data(dt_from: datetime, dt_upto: datetime, group_type: str) -> str:
    """user input request aggregation through mongodb requests"""
    # getting collection
    collection: Collection = get_db().get_collection("sample_collection")

    dataset, labels = [], []

    current_date = dt_from

    # while dates exists
    while current_date <= dt_upto:
        next_date = None

        if group_type == "hour":
            next_date = current_date + relativedelta(hours=1)
        elif group_type == "day":
            next_date = current_date + relativedelta(days=1)
        elif group_type == "month":
            next_date = current_date + relativedelta(months=1)

        if current_date == dt_upto:
            next_date = dt_upto

        if next_date:
            query = [
                {
                    "$match": {
                        "dt": {"$gte": current_date, "$lt": next_date}
                    }
                },
                {
                    "$group": {
                        "_id": None,
                        "total_value": {"$sum": "$value"}
                    }
                }
            ]

            result = list(collection.aggregate(query))

            try:
                dataset.append(result[0]['total_value'])
            except:
                dataset.append(0)
            labels.append(current_date.isoformat())

            current_date = next_date

            # fill missings of end datetime
            if current_date == dt_upto:
                if dt_upto not in labels:
                    labels.append(dt_upto.isoformat())
                    dataset.append(0)
                break
        else:
            break

    return json.dumps({"dataset": dataset, "labels": labels})
