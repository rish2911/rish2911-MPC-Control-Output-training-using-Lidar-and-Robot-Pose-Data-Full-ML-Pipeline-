import os
import glob
import pandas as pd
import numpy as np

class data_imp():
    def __init__(self, full_path_of_inputfiles:str, outfile_name="combined_csv.csv") -> np.array:
        self.path_ = full_path_of_inputfiles
        print("path supplied \n")
        # os.chdir(self.path_)
        self.data_ = None
        self.outfile_name_ = outfile_name
        self.combine_files()
        self.data_extraction()
        pass

    def combine_files(self, extension='csv'):
        if os.path.exists(self.path_ + "\\"+ self.outfile_name_):
            print("The file already exists")
            return None
        else:
            print("The file does not exist")
            print("combining input files \n")
            all_filenames = [i for i in glob.glob(self.path_+'\\*.{}'.format(extension))]
            #combine all files in the list
            combined_csv = pd.concat([pd.read_csv(f, header=None) for f in all_filenames], axis=0)
            # print(combined_csv)
            #export to csv
            # encoding ‘utf-8-sig’ is added to overcome the issue when exporting ‘Non-English’ languages.
            print("writing combined files \n")
            combined_csv.to_csv(self.path_ + "\\"+ self.outfile_name_, index=False, encoding='utf-8-sig')
            return None

    def data_extraction(self):
        print("extracting data as array \n")
        with open(self.path_ + "\\"+ self.outfile_name_, newline='') as csvfile:
            df = pd.read_csv(csvfile)
            self.data_ = df.to_numpy()
        print(self.data_.shape)

# if __name__=="__main__":
#     input_path = "Input_data\\training"
#     imported = data_imp(input_path)
#     print(imported.data_)

    
   