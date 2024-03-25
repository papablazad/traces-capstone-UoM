#%%
from utils_functions import *
############## PROCESS SOLAR TRACES ##############

# PROCESS FILES FOR NON REZ GENERATORS
if not os.path.exists("processed_traces/solar_traces/gen_solar_no_REZ"): # check if the folder solar_traces/gen_solar_no_REZ exists in the processed_traces folder. If not, create the folder
    os.makedirs("processed_traces/solar_traces/gen_solar_no_REZ")
for year in ref_years:
    path = f"{solar_path}/solar_{year}"
    solar_files = os.listdir(path)
    solar_files_no_REZ = [file for file in solar_files if 'REZ' not in file]    # get all the files that do not contain REZ in their name
    if not os.path.exists(f"processed_traces/solar_traces/gen_solar_no_REZ/REF_YEAR_{year}"):
        os.makedirs(f"processed_traces/solar_traces/gen_solar_no_REZ/REF_YEAR_{year}")
    for gen_no_rez in solar_files_no_REZ:
        file_path = f"{solar_path}/solar_{year}/{gen_no_rez}"
        if not os.path.exists(file_path):  # check if file exist in file_path. If not, print a warning
            warnings.warn(f"{file_path} does not exist!")
        else:
            # process the file
            process_csv(file_path, save_csv=True, filename=f"processed_traces/solar_traces/gen_solar_no_REZ/REF_YEAR_{year}/{gen_no_rez}")

# PROCESS FILES FOR REZ GENERATORS
if not os.path.exists("processed_traces/solar_traces/gen_solar_REZ"): # check if the folder solar_traces/gen_solar_no_REZ exists in the processed_traces folder. If not, create the folder
    os.makedirs("processed_traces/solar_traces/gen_solar_REZ")
for year in ref_years:
    path = f"{solar_path}/solar_{year}"
    solar_files = os.listdir(path)
    solar_files_REZ = [file for file in solar_files if 'REZ' in file]           # get all the files that contain REZ in their name
    REZs = list(set([file.split('_')[1] for file in solar_files_REZ]))          # split the names of solar_files_REZ by every "_", pick only the second string for each (REZ code), and drop duplicates
    for rez in REZs:
        files_rez = [file for file in solar_files_REZ if rez in file] # get only the files to the corresponding REZ
        if not os.path.exists(f"processed_traces/solar_traces/gen_solar_REZ/REF_YEAR_{year}/{rez}") and len(files_rez) > 0:
            os.makedirs(f"processed_traces/solar_traces/gen_solar_REZ/REF_YEAR_{year}/{rez}")
        for file_rez in files_rez:
            file_path = f"{solar_path}/solar_{year}/{file_rez}"
            if not os.path.exists(file_path): # check if file exist in file_path. If not, print a warning
                warnings.warn(f"{file_path} does not exist!")
            else:
                # process the file
                process_csv(file_path, save_csv=True, filename=f"processed_traces/solar_traces/gen_solar_REZ/REF_YEAR_{year}/{rez}/{file_rez}")