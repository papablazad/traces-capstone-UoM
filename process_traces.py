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
solar_path = 'data/Solar/solar'
wind_path = 'data/Wind/wind'

############## FUNCTIONS ##############
def process_csv(data_path, save_csv=False, filename=''):
    try: 
        data = pd.read_csv(data_path)
        data['date'] = pd.to_datetime(data.iloc[:, 0:3])
        data = data.set_index('date').drop(columns=['Year', 'Month', 'Day']).dropna()
        data.columns = data.columns.astype(int)
        if save_csv: data.to_csv(filename)
        print(filename.split('/')[-1], 'SAVED!')
    except Exception as e:
        warnings.warn(f"An error occurred: {e}")

#%% 
############## PROCESS DEMAND TRACES ##############
# create a folder called "demand_traces" in processed_traces folder if the demand_traces folder does not exists
if not os.path.exists("processed_traces/demand_traces"):
    os.makedirs("processed_traces/demand_traces")   

for state in states:
    for scenario in scenarios:
        if not os.path.exists(f"processed_traces/demand_traces/{scenario}"): # create a folder for each scenario in "processed traves" folder if it does not exists
            os.makedirs(f"processed_traces/demand_traces/{scenario}")
        for poe in poes:
            if not os.path.exists(f"processed_traces/demand_traces/{scenario}/POE{poe}"): # create a folder in the scenario folder for each POE value if it does not exists
                os.makedirs(f"processed_traces/demand_traces/{scenario}/POE{poe}")
            for ref_year in ref_years: # create a folder in the scenario folder for each reference year if it does not exists
                if not os.path.exists(f"processed_traces/demand_traces/{scenario}/POE{poe}/REF_YEAR_{ref_year}"):
                    os.makedirs(f"processed_traces/demand_traces/{scenario}/POE{poe}/REF_YEAR_{ref_year}")
                for file_type in file_types:
                    data_path = f"{demand_path}/ISP Demand Traces {state} {scenario}/demand_{state}_{scenario}/{state}_RefYear_{ref_year}_{map_scenarios[scenario]}_POE{poe}_{file_type}.csv"
                    filename = f"processed_traces/demand_traces/{scenario}/POE{poe}/REF_YEAR_{ref_year}/{state}_{map_scenarios[scenario]}_REF_YEAR_{ref_year}_POE{poe}_{file_type}.csv"
                    process_csv(data_path, save_csv=True, filename=filename)


#%% 
############## PROCESS SOLAR TRACES ##############
# get all the filenames from solar_path
solar_files = os.listdir(solar_path)
solar_files_no_REZ = [file for file in solar_files if 'REZ' not in file] # get all the files that do not contain REZ in their name
solar_files_REZ = [file for file in solar_files if 'REZ' in file]         # get all the files that contain REZ in their name
    
# %% PROCESS WIND TRACES
wind_files = os.listdir(wind_path)
wind_files_no_REZ = [file for file in wind_files if 'REZ' not in file] # get all the files that do not contain REZ in their name
wind_files_REZ = [file for file in wind_files if 'REZ' in file]         # get all the files that contain REZ in their name

