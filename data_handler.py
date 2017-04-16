import pandas as pd
import numpy as np
import math
from sklearn.preprocessing import MinMaxScaler

class time_series_data_handler(object):

    def __init__(self, datapath, input_columns, target_columns,\
                training_test_ratio = [0.8,0.2], input_time_step = 5, target_time_step = 2,\
                time_lag = 2, overlap = 4, test_only = False, scaling_bound = [-1,1], skiprows = None):

        """
            args:
                datapath (string): path to data csv file
                input columns (list) : input sequence index list. ex) [0,1,2]
                target columns (list) : taget sequences index list
                training_validation_test_ratio = default is [80,10,10]
                input_time_step (integer): input data truncation length
                target_time_step (integer): target data truncation length
                time_lag (integer, possibly negative integer): default is 1.

                    In that case, data will be paired as follows:
                        train_x, train_y = (x1_t, x2_t, xN_t), (y1_t+1, y2_t+1, yM_t+1)

                input_overlap (positive integer + 0) : defualt is 0; no overlap would apply. If the value of
                input_overlap is positive integer, cossecutive x data pairs will overlap the value of 'input_overlap' time_step each others.
                target_overlap (positive integer + 0) : Similar to input_overlap
                test_only (boolean) : dafault is False. If true, an instantiated handler only has test_x, test_y.

            properties:
                train_x : dimension = [ number of data x time_step x num_seqeunce ]
                train_y : same as train_x
                validation_x  : same as train_x
                validation_y  : same as train_x
                test_x  : same as train_x
                test_y  : same as train_x
        """

        if test_only == False:
            self.train_x = []
            self.train_y = []
            self.validation_x = []
            self.validation_y = []

        self.test_x = []
        self.test_y = []
        self.datapath = datapath
        self.input_columns = input_columns
        self.target_columns = target_columns
        self.training_test_ratio = training_test_ratio
        self.input_time_step = input_time_step
        self.target_time_step = target_time_step
        self.time_lag = time_lag
        self.overlap = overlap
        
        self.scaling_bound = scaling_bound
        self.input_data_scaler = None
        self.target_data_scaler = None

        def load_data():
            df_x = pd.read_csv(str(datapath), usecols = input_columns, skiprows = skiprows)
            df_y = pd.read_csv(str(datapath), usecols = target_columns, skiprows = skiprows)
            dmat_x = df_x.as_matrix()
            dmat_y = df_y.as_matrix()
            return dmat_x , dmat_y

        def set_scalers():
            # Adapt code for various scaler and its parameters.
            self.input_data_scaler = MinMaxScaler(feature_range=(self.scaling_bound[0],self.scaling_bound[1]))
            self.target_data_scaler = MinMaxScaler(feature_range=(self.scaling_bound[0],self.scaling_bound[1]))

        def prepare_scaled_data():
            x_, y_ = load_data()
            set_scalers()
            
            #return x_, y_
            
            return self.input_data_scaler.fit_transform(x_),\
                self.target_data_scaler.fit_transform(y_)
            
        def csv_to_data():
            # Read data from CSV file -> Scaling data -> split into [training / test] set
            scaled_x, scaled_y = prepare_scaled_data()
            # Convert 2d (or possibly 1d) data structure into 3d

            _3d_x_data = np.empty((input_time_step,len(input_columns))) # Declare an empty array
            for i in xrange(0,np.shape(scaled_x)[0], input_time_step-overlap):
                try:
                    _3d_x_data = np.dstack((_3d_x_data,scaled_x[i:i+input_time_step]))
                except:
                    pass

            _3d_y_data = np.empty((target_time_step,len(target_columns)))
            for i in xrange(input_time_step,np.shape(scaled_x)[0], input_time_step-overlap):
                try:
                    _3d_y_data = np.dstack((_3d_y_data,scaled_y[i+(time_lag-1):i+(time_lag-1)+target_time_step]))
                except:
                    pass

            print _3d_x_data.shape
            print _3d_y_data.shape

            # Dimension of train_x, train_y = [Num of data, time_step, num_input]
            packed_x = np.transpose(_3d_x_data, (2,0,1))
            packed_y = np.transpose(_3d_y_data, (2,0,1))

            # Delete the first element along the first axix ( =0 ) -> Need to improve.
            # Trouble shoting is required : Withouth following scripts, the first element will be an 'erronous entry'

            packed_x = np.delete(packed_x,0,0)
            packed_y = np.delete(packed_y,0,0)

            # Fit the 1st dimension of train_y into the one of train_x
            while np.shape(packed_x)[0] > np.shape(packed_y)[0]:
                packed_x = np.delete(packed_x, packed_x.shape[0]-1, 0)

            # Split packed_x, packed_y into train / test set
            test_index = int(math.floor(packed_x.shape[0]*training_test_ratio[0]))

            if test_only == False:
                self.train_x = packed_x[0:test_index]
                self.train_y = packed_y[0:test_index]
                self.test_x = packed_x[test_index:]
                self.test_y = packed_y[test_index:]
            else:
                self.test_x = packed_x
                self.test_y = packed_y

        csv_to_data()