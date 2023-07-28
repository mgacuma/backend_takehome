import pandas as pd
import sys

class Transformer():
    def __init__(self):
        pass

    def total_experiments(self, usersData: pd.DataFrame, experimentsData: pd.DataFrame):
        user_map = {}

        for index, row in usersData.iterrows():
            user_map[row['user_id']] = 0


        for index, row in experimentsData.iterrows():
            user_map[row['user_id']] += 1
            
        return user_map
    
    def users_compounds(self, usersData: pd.DataFrame, experimentsData: pd.DataFrame, compoundsData: pd.DataFrame):
        compounds_map = {}
        user_map = {}
        # Fill compounds map with all known compounds
        for index, row in compoundsData.iterrows():
            compounds_map[row['compound_id']] = row['compound_name']

        # Fill users map with another map of compounds with value of num of experiments
        for index, row in usersData.iterrows():
            user_map[row['user_id']] = { key: 0 for key in compounds_map }

        # Fill with experiments used
        for index, row in experimentsData.iterrows():
            experiment = row
            user = experiment.user_id
            compound_ids = experiment.experiment_compound_ids.split(';')



            for compound_id in compound_ids:
                user_map[user][int(compound_id)] += 1

        for user_id, compounds in user_map.items():
            max_compound_used = max(compounds.values())
            keys_with_max_value = [key for key, value in compounds.items() if value == max_compound_used]
            user_map[user_id] = keys_with_max_value

        return user_map
    
    