from pymongo import MongoClient
from dateutil.parser import parse
from data_preparation import get_latest_work_experience

client = MongoClient("127.0.0.1", 8201)
db = client.indeedspotmentor
data = db.data.find()


my_list=[]
my_dict1 = {"id":[],"skills":[],"additionalinformation":[]}

def getting_skills_additional_info():
	for data in db.data.find():
		my_dict1["id"].append(data.get('_id'))
		my_dict1['skills'].append(data.get('skills'))
		my_dict1['additionalinformation'].append(data.get('additional_information'))
	return my_dict1

def get_latest_work_experience(document_id, work_experiences):
    output_dict = {}
    end_date_to_workex_mapping = {}
    end_dates = []

    for i in range(len(work_experiences)):
        date = work_experiences[i].get('work_date')
        if date:
            if "present" in date.lower():
                output_dict.update({
                        "output_work_title" : work_experiences[i].get('work_title'),
                        # "output_work_company" : work_experiences[i].get('work_company'),
                        # "output_work_date" : work_experiences[i].get('work_date'),
                        "output_work_description" : work_experiences[i].get('work_description'),
                        # "document_id" : str(document_id)
                        
                    })

    if not output_dict:
        for i in range(len(work_experiences)):
            date = work_experiences[i].get('work_date')
            if date:
                split_date = date.split(" to ")
                if len(split_date) == 2:
                    end_dates.append(parse(split_date[1]))
                    end_date_to_workex_mapping.update({
                            parse(split_date[1]) : work_experiences[i]
                        })
        if end_dates:
            max_end_date = max(end_dates)
            latest_workex = end_date_to_workex_mapping[max_end_date]
            output_dict = {
                "output_work_title" : latest_workex.get('work_title'),
                # "output_work_company" : latest_workex.get('work_company'),
                # "output_work_date" : latest_workex.get('work_date'),
                "output_work_description" : latest_workex.get('work_description'),
                # "document_id" : str(document_id)
            }

    return output_dict

def getting_title_description():
	for data in db.data.find():
		my_list.append(get_latest_work_experience(str(data.get('_id')), data.get('work_experience')))
	return my_list

