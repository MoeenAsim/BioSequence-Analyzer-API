from datetime import datetime
from copy import deepcopy
from database.connection import analysis_collection

def save_analysis(data):

    document = deepcopy(data)

    document["created_at"] = datetime.utcnow()

    result = analysis_collection.insert_one(document)

    return str(result.inserted_id)
from bson import ObjectId

def get_analysis(analysis_id):

    analysis = analysis_collection.find_one(
        {
            "_id": ObjectId(analysis_id)
        }
    )

    if analysis:
        analysis["_id"] = str(analysis["_id"])

    return analysis
def get_all_analysis():

    analyses = list(analysis_collection.find())

    for analysis in analyses:
        analysis["_id"] = str(analysis["_id"])

    return analyses
from bson import ObjectId

def delete_analysis(analysis_id):

    result = analysis_collection.delete_one(
        {
            "_id": ObjectId(analysis_id)
        }
    )

    return result.deleted_count