#%%
from utils_functions import *
############## PROCESS WIND TRACES ##############
REZs = pd.read_excel('data/Draft 2024 ISP Inputs and Assumptions workbook.xlsx', 
                     sheet_name='Renewable Energy Zones',usecols='B:B',skiprows=6, nrows=44).dropna().values.flatten() # get all the REZs from the excel file
REZs = np.append(REZs, ['V0', 'N0']) # add V0 and N0 to the REZs list
#%% 
# PROCESS WIND TRACES FROM NON-REZ
if not os.path.exists("processed_traces/wind_traces/gen_wind_no_REZ"): # check if the folder wind_traces/gen_wind_no_REZ exists in the processed_traces folder. If not, create the folder
    os.makedirs("processed_traces/wind_traces/gen_wind_no_REZ")
for year in ref_years:
    path = f"{wind_path}/wind_{year}"
    wind_files = os.listdir(path)
    wind_files_no_REZ = [file for file in wind_files if file.split('_')[0] not in REZs]    # get all the files that do not contain REZ in their name (first string in the file name)
    if not os.path.exists(f"processed_traces/wind_traces/gen_wind_no_REZ/REF_YEAR_{year}"):
        os.makedirs(f"processed_traces/wind_traces/gen_wind_no_REZ/REF_YEAR_{year}")
    for gen_no_rez in wind_files_no_REZ:
        file_path = f"{wind_path}/wind_{year}/{gen_no_rez}"
        if not os.path.exists(file_path):  # check if file exist in file_path. If not, print a warning
            warnings.warn(f"{file_path} does not exist!")
        else:
            process_csv(file_path, save_csv=True, filename=f"processed_traces/wind_traces/gen_wind_no_REZ/REF_YEAR_{year}/{gen_no_rez}")
#%%
# PROCESS WIND TRACES FROM REZ 
if not os.path.exists("processed_traces/wind_traces/gen_wind_no_REZ"): # check if the folder wind_traces/gen_wind_no_REZ exists in the processed_traces folder. If not, create the folder
    os.makedirs("processed_traces/wind_traces/gen_wind_no_REZ")
for year in ref_years:
    path = f"{wind_path}/wind_{year}"
    wind_files = os.listdir(path)
    wind_files_REZ = [file for file in wind_files if file.split('_')[0] in REZs]
    for rez in REZs:
        files_rez = [file for file in wind_files_REZ if file.split('_')[0] == rez] # get only the files to the corresponding REZ
        if not os.path.exists(f"processed_traces/wind_traces/gen_wind_REZ/REF_YEAR_{year}/{rez}") and len(files_rez) > 0:
            os.makedirs(f"processed_traces/wind_traces/gen_wind_REZ/REF_YEAR_{year}/{rez}")
        for file_rez in files_rez:
            file_path = f"{wind_path}/wind_{year}/{file_rez}"
            if not os.path.exists(file_path): # check if file exist in file_path. If not, print a warning
                warnings.warn(f"{file_path} does not exist!")
            else:
                process_csv(file_path, save_csv=True, filename=f"processed_traces/wind_traces/gen_wind_REZ/REF_YEAR_{year}/{rez}/{file_rez}")
# %%
