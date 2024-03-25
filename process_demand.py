#%% 
from utils_functions import *

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
                for file_type in file_types: # process all the original data from AEMO
                    data_path = f"{demand_path}/ISP Demand Traces {state} {scenario}/demand_{state}_{scenario}/{state}_RefYear_{ref_year}_{map_scenarios[scenario]}_POE{poe}_{file_type}.csv"
                    filename = f"processed_traces/demand_traces/{scenario}/POE{poe}/REF_YEAR_{ref_year}/{state}_{map_scenarios[scenario]}_REF_YEAR_{ref_year}_POE{poe}_{file_type}.csv"
                    process_csv(data_path, save_csv=True, filename=filename)

