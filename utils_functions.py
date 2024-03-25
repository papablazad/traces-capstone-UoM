#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import warnings

# ⋙⋙ DATA
states = ['NQ','CQ','GG','SQ','NNSW','CNSW','SNW','SNSW','VIC','CSA', 'SESA','TAS'] # state names
sce = ['HYDROGEN_EXPORT', 'PROGRESSIVE_CHANGE', 'STEP_CHANGE']                      # scenario names from the files
scenarios = ['Green Energy Exports', 'Progressive Change', 'Step Change']           # scenario names from the folders
map_scenarios = dict(zip(scenarios, sce))                                           # map scenario names
poes = [10, 50]                                                                     # probability of exceedance (POE) values
ref_years = np.arange(2011, 2024, 1)                                                # reference years

# OPSO_MODELLING: demand after the impact of PV (operational demand)
# OPSO_MODELLING_PVLITE: demand before the impact of PV (total demand)
# PV_TOT: total PV generation
file_types = ['OPSO_MODELLING', 'OPSO_MODELLING_PVLITE', 'PV_TOT']                  # file types

# ⋙⋙ PATHS
demand_path = 'data/Demand'
solar_path = 'data/Solar'
wind_path = 'data/Wind'

############## FUNCTIONS ##############
def process_csv(data_path, save_csv=False, filename=''):
    try: 
        data = pd.read_csv(data_path)
        data['date'] = pd.to_datetime(data.iloc[:, 0:3])
        data = data.set_index('date').drop(columns=['Year', 'Month', 'Day']).dropna()
        data.columns = data.columns.astype(int)
        if save_csv: 
            data.to_csv(filename)
            print(filename.split('/')[-1], 'SAVED!')
    except Exception as e:
        warnings.warn(f"An error occurred: {e}")
    return data