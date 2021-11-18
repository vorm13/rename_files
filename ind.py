import os

with open('dict.txt') as file_names:
    for line in file_names:
        info = dict() 
        info['num_file_name'] = line.split(";")[0]
        info['human_name'] = line.split(';')[1]
        
        less_n_human_name = str(info['human_name'])
        try:
            os.rename(info['num_file_name'], less_n_human_name[:-1]+'.pdf')
        except FileNotFoundError:
            print('No file found with name: '+info['num_file_name'])

print('Done!')
