import os 
import csv
import datetime as datetime

def wrtie_to_file(data):

    if not os.path.exists('sim_results'):   
        os.makedirs('sim_results')
        
    extension =    ".csv"
    file_name = os.getcwd() + "/sim_results/" + f"{datetime.datetime.now():%Y-%m-%d %H-%M-%S}" + extension
    print(file_name)

    with open(file_name, 'w') as myfile:
        wr = csv.writer(myfile)
        for key in data:
            wr.writerow(['{} : {}'.format(key, data[key])])