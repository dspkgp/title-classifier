from data_indeed_reading import getting_title_description, getting_skills_additional_info
import pandas as pd

my_dict = {'id':[],'additionalinformation':[],'skills':[],'workdescription':[],'worktitle':[],'addinfo_workdesc':[],'addinfo_workdesc_skills':[]}
my_list = getting_title_description()
my_dict2 = getting_skills_additional_info()

def converting_list_to_dictionary(my_dictionary):
	for i in range(10000):
		my_dictionary['workdescription'].append(my_list[i].get('output_work_description'))
		my_dictionary['worktitle'].append(my_list[i].get('output_work_title'))
		my_dictionary['id'].append(my_dict2['id'][i])
		my_dictionary['skills'].append(my_dict2['skills'][i])
		my_dictionary['additionalinformation'].append(my_dict2['additionalinformation'][i])	
	return my_dictionary



def convert_my_dictionary_to_dataframe(my_dictionary):
	return pd.DataFrame(dict([ (key,pd.Series(value)) for key,value in my_dictionary.iteritems() ]))

def clean_redundand_values(my_dataframe):
    redundand = ["u'",",","{","}","[","]","_","'","%nbsp",";","\n",","]
    for element in redundand:
        my_dataframe['addinfo_workdesc_skills'] = my_dataframe['addinfo_workdesc_skills'].str.replace(element,'')

    return my_dataframe    


if  __name__ == "__main__":
    
    my_dict = converting_list_to_dictionary(my_dict)    
    df2 = convert_my_dictionary_to_dataframe(my_dict)    
    df2['addinfo_workdesc'] = df2[['additionalinformation','workdescription']].apply(lambda x: ','.join([elements for elements in x if isinstance(elements,basestring)]),axis=1) 
    df2['addinfo_workdesc_skills'] = df2[['addinfo_workdesc','skills']].apply(lambda x: ','.join([elements for elements in x if isinstance(elements,basestring)]),axis=1) 
    df2 = clean_redundand_values(df2)

    print df2.head()
    print "\n"
   	
