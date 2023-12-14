#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygrib


# In[2]:


import pandas as pd


# In[3]:


from datetime import timedelta


# In[4]:


import os


# In[5]:


import datetime as dt


# In[6]:


import numpy as np


# In[7]:


import matplotlib.pyplot as plt


# In[8]:


from matplotlib.lines import Line2D


# In[9]:


from matplotlib.ticker import MaxNLocator 


# In[10]:


import pickle


# In[11]:


import matplotlib.dates as mdates


# In[12]:


forecast_hr = np.arange(15,85,3)


# In[13]:


latbounds = [ 18.5 - 0.25 , 19.5 ]
lonbounds = [ 72.5 , 73.5 + 0.25 ]


# In[14]:


time_from_ref = np.arange(15,85,3)


# In[15]:


columns_prec = []

for i in ['Prec']:
    for time_steps in forecast_hr:
        for j in np.arange(19.5,18.25,-0.25):
            for k in np.arange(72.5,73.75,0.25):
                columns_prec.append(f'{i}_{j}_{k}_{time_steps:03d}')


# In[16]:


x = dt.datetime.now().replace(second=0, microsecond=0)


# In[17]:


pd.to_datetime(x)


# In[18]:


day=x.day
month = x.month
year = x.year


# In[19]:


start_day = f'{year}-{month}-{day}'
end_day = pd.to_datetime(start_day) + timedelta(hours=24)


# In[20]:


start_day


# In[21]:


end_day


# In[22]:


data_prec = pd.DataFrame(index =[pd.to_datetime(start_day) + timedelta(hours=6)], columns = columns_prec)


# In[23]:


#data_prec = pd.DataFrame(index =[pd.to_datetime('2023-08-19') + timedelta(hours=6)], columns = columns_prec)


# In[23]:


data_prec


# In[24]:


root_directory = f"/home/subimal/Documents/HDFC_Web/Automation/{day:02d}-{month:02d}-{year}"


# In[ ]:


#root_directory = f"C:/Users/Admin/Desktop/GFS FORECASTS/24-{month:02d}-{year}"


# In[25]:


#root_directory = f"C:/Users/Admin/Desktop/Automation/19-08-{year}"


# In[25]:


root_directory


# In[27]:


counter =0


# In[28]:


for time_step in data_prec.index:
    
    year = time_step.year
    month = time_step.month
    day = time_step.day

    ref_time = time_step.hour
    
    date_temp = pd.date_range(start = time_step + timedelta(hours = 15), end = time_step + timedelta(hours = 84) , freq = '3H')
    col_temp = np.arange(0,25)
    
    data_temp = pd.DataFrame(index  = date_temp, columns=col_temp)
    
    for time_lag in time_from_ref:
        
        filename =f'gfs.t{ref_time:02d}z.pgrb2.0p25.f{time_lag:03d}'
        #directory = find_key(directory_names, filename)
        
        
        
        grib = f'{root_directory}/{filename}'
        grbs = pygrib.open(grib)
        variable_name_to_select = 'Precipitation rate'  # Replace with the variable name you want

        # Loop through the GRIB messages (variables) in the file
        for grb in grbs.select(name=variable_name_to_select):
            # Access the data and metadata of the selected variable
            data = grb.values  # Data values
            latitudes, longitudes = grb.latlons()  # Latitudes and longitudes
            parameter_name = grb.name  # Parameter name (e.g., 'Temperature', 'Wind speed', etc.)
            level_type = grb.typeOfLevel  # Level type (e.g., 'surface', 'isobaricInhPa', etc.)
            level_value = grb.level  # Level value (e.g., 850, 1000, etc.)
            valid_time = grb.validDate  # Valid time of the data


        # latitude lower and upper index
        latli = 2
        latui = 7 

        # longitude lower and upper index
        lonli = 2
        lonui = 7



        time = pd.to_datetime(f'{year}-{month}-{day}') + timedelta(hours = int(int(ref_time) + int(time_lag)))
        data = data[latli:latui,lonli:lonui][::-1]
        time_prev = time - timedelta(hours = 3)

        if ((int(time_lag)%6) == 0):
            if len(np.ravel(data)) == 25:
                data_temp.loc[time][0:25] =  (np.ravel(data)*21600) - np.ravel(data_temp.loc[time_prev][0:25])

        elif ((int(time_lag)%6) != 0) & ((int(time_lag)%3) == 0):
            if len(np.ravel(data)) == 25:
                data_temp.loc[time][0:25] =  (np.ravel(data)*10800)
        else:
            print(filename)
            
                
    data_prec.loc[time_step][0:600] = np.ravel(data_temp)
    
    counter += 1
    if (counter)%500 == 0:
        print(f'Loop {counter} Done!')
        


# In[29]:


data_prec


# In[30]:


data_prec = data_prec.shift(freq=pd.Timedelta(hours=17, minutes=30))
data_prec.head()


# In[31]:


n_features = 25
n_steps = 24
n_samples_test = data_prec.shape[0]


# In[32]:


X_test_prec_cnn_lstm = np.full((n_samples_test,24,5,5),np.nan)


# In[33]:


import copy


# In[34]:


for i in range(data_prec.shape[0]):
    temp_array = np.full((24,5,5),np.nan)
    counter = 0
    
    for j in np.arange(15,85,3):
        
        selected_cols = data_prec.filter(regex=f'_{j:03d}$')
        temp_array[counter] = selected_cols.iloc[i].values.reshape(5,-1)
        counter +=1
        
    X_test_prec_cnn_lstm[i] = copy.deepcopy(temp_array)


# In[35]:


X_test_prec_cnn_lstm_daily = np.full((n_samples_test,3,5,5),np.nan) #for daily interval


# In[36]:


for i in range(X_test_prec_cnn_lstm_daily.shape[0]):
    X_test_prec_cnn_lstm_daily[i,0,:,:] = np.sum(X_test_prec_cnn_lstm[i,0:8,:,:], axis = 0)
    X_test_prec_cnn_lstm_daily[i,1,:,:] = np.sum(X_test_prec_cnn_lstm[i,8:16,:,:], axis = 0)
    X_test_prec_cnn_lstm_daily[i,2,:,:] = np.sum(X_test_prec_cnn_lstm[i,16:24,:,:], axis = 0)


# In[37]:


X_test_prec_cnn_lstm_daily.shape


# In[38]:


X_test_prec_cnn_lstm_reshaped = np.expand_dims(X_test_prec_cnn_lstm_daily, axis=1)


# In[39]:


X_test_prec_cnn_lstm_reshaped = np.moveaxis(X_test_prec_cnn_lstm_reshaped, 1, -1)


# In[40]:


X_test_prec_cnn_lstm_reshaped.shape


# In[41]:


with open('/home/subimal/Documents/HDFC_Web/Automation/X_test_prec_cnn_lstm_reshaped.pickle', 'rb') as file:
    X_test_prec_cnn_lstm_hindcast2023_reshaped= pickle.load(file)


# In[42]:


X_test_prec_cnn_lstm_hindcast2023_reshaped.shape


# In[ ]:


X_test_prec_cnn_lstm_reshaped.shape


# In[ ]:


X_test_prec_cnn_lstm_hindcast2023_concatenate =np.concatenate((X_test_prec_cnn_lstm_hindcast2023_reshaped, X_test_prec_cnn_lstm_reshaped), axis=0)


# In[78]:


#X_test_prec_cnn_lstm_hindcast2023_concatenate = X_test_prec_cnn_lstm_hindcast2023_reshaped


# In[79]:


X_test_prec_cnn_lstm_hindcast2023_concatenate.shape


# In[80]:


# Function to generate uncertainty bands
def generate_uncertainty_bands(model, x_test, num_passes=1000):
    predictions = []
    for _ in range(num_passes):
        preds = np.array(model(x_test,  training = True))
        predictions.append(preds)
        #if _%100 == 0:
            #print(f'{_} predictions complete!')
    predictions = np.array(predictions)
    mean_predictions = np.mean(predictions, axis=0)
    std_predictions = np.std(predictions, axis=0)
    return predictions, mean_predictions, std_predictions


# In[81]:


stations_ok_merged = sorted(['Andheri', 'B ward', 'Bandra','C ward', 'Chembur', 'D Ward',
               'Dindoshi','F North', 'F South', 'G South','Gowanpada', 'H West ward', 'K East ward',
               'Kurla', 'L ward', 'M West ward','Malvani','MCGM 1','Mulund','N ward','Nair Hospital',
               'Nariman Fire','S ward','SWD Workshop dadar','Vikhroli','vileparle W', 'Byculla', 'Chincholi', 
                      'Colaba', 'Dahisar', 'K West ward', 'Kandivali','Marol','Memonwada','Rawali camp','Thakare natya','Worli'])


# In[82]:


from tensorflow.keras.models import Sequential, load_model


# In[83]:


stations_coordinates = pd.read_excel('/home/subimal/Documents/HDFC_Web/Automation/Stations_Coordinates.xlsx',header = 0, index_col='Place')
stations_coordinates.head()
lat_lon = []

for i in np.arange(18.5,19.5+0.25,0.25):
    for j in np.arange(72.5, 73+0.25,0.25):

        lat_lon.append([i,j])

lat_lon = np.array(lat_lon)
lat_lon=lat_lon.astype(float)
def find_closest_pair(lat_lon_array, target_lat, target_lon):
    # Calculate differences in latitude and longitude
    delta_lat = lat_lon_array[:, 0] - target_lat
    delta_lon = lat_lon_array[:, 1] - target_lon

    # Calculate Euclidean distances
    distances = np.sqrt(delta_lat**2 + delta_lon**2)

    # Find the index of the pair with the minimum distance
    closest_index = np.argmin(distances)

    # Return the closest pair of latitude and longitude
    return lat_lon_array[closest_index]


# In[ ]:


#Root directory path

#root_directory = "C:/Users/Admin/Desktop/GFS FORECASTS/boxplottimeseries"

# List of main directory names
#main_directories = stations_ok_merged

# Create main directories
#for main_dir in main_directories:

    #main_dir_path = os.path.join(root_directory, main_dir)

    #os.makedirs(main_dir_path, exist_ok=True)


# In[88]:


#start_day = '2023-08-19'
#start_day


# In[159]:


for station in stations_ok_merged:
    model = load_model(f'/home/subimal/Documents/HDFC_Web/Automation/my_best_cnn_model_only_prec_{station}_downscaling_2.h5')
    predictions = []
    mean_preds = []
    std_preds = []
    predictions, mean_preds, std_preds = generate_uncertainty_bands(model, X_test_prec_cnn_lstm_hindcast2023_concatenate)
    predictions_today = predictions[:,-1,:]
    predictions_1_day_lead = []

    for i in range(predictions.shape[0]):
        predicted_values = []

        for j in range(0,predictions.shape[1]):
            predicted_values.append(predictions[i,j,0])
        predictions_1_day_lead.append(predicted_values)

    predictions_1_day_lead = np.array(predictions_1_day_lead)
    
    predictions_2_day_lead = []

    for i in range(predictions.shape[0]):
    
        predicted_values = []

        for j in range(0,predictions.shape[1]):
            predicted_values.append(predictions[i,j,1])
        
        predictions_2_day_lead.append(predicted_values)
    
    predictions_2_day_lead = np.array(predictions_2_day_lead)
    
    predictions_3_day_lead = []

    for i in range(predictions.shape[0]):
    
        predicted_values = []

        for j in range(0,predictions.shape[1]):
            predicted_values.append(predictions[i,j,2])
        
        predictions_3_day_lead.append(predicted_values)
    
    predictions_3_day_lead = np.array(predictions_3_day_lead)
    plt.ioff()
    dates = pd.date_range(start =data_prec.index[0],end=pd.to_datetime(data_prec.index[0])+ timedelta(hours=71),freq='1D')
    data_GFS_prec_stationwise_testing = {}
    data_GFS_prec_stationwise = {}
    
    
    data_GFS_prec_stationwise[station] = pd.DataFrame()
    
    station_lat = stations_coordinates.loc[station,'Lat (N)']
    station_lon = stations_coordinates.loc[station, 'Long (E)']

    closest_lat_lon = find_closest_pair(lat_lon, station_lat, station_lon)
    closest_lat = str(closest_lat_lon[0])
    closest_lon = str(closest_lat_lon[1])

    selected_cols_testing = data_prec.filter(regex=f'{closest_lat}_{closest_lon}')
    
    data_GFS_prec_stationwise_testing[station] = copy.deepcopy(selected_cols_testing)
    
    data_GFS_prec_stationwise_daily = {}
    data_GFS_prec_stationwise_testing_daily = {}
    
    data_GFS_prec_stationwise_testing_daily[f'{station}'] = pd.DataFrame(index=data_GFS_prec_stationwise_testing[f'{station}'].index,columns=['1','2','3'])
    data_GFS_prec_stationwise_testing_daily[f'{station}'].iloc[:,0] = data_GFS_prec_stationwise_testing[f'{station}'].iloc[:,0:8].sum(axis = 1)
    data_GFS_prec_stationwise_testing_daily[f'{station}'].iloc[:,1] = data_GFS_prec_stationwise_testing[f'{station}'].iloc[:,8:16].sum(axis = 1)
    data_GFS_prec_stationwise_testing_daily[f'{station}'].iloc[:,2] = data_GFS_prec_stationwise_testing[f'{station}'].iloc[:,16:24].sum(axis = 1)
    
    y_pred_gfs = np.array(data_GFS_prec_stationwise_testing_daily[f'{station}']).astype(float)
    
    gfs1 = y_pred_gfs[:,0]
    gfs2 = y_pred_gfs[:,1]
    gfs3 = y_pred_gfs[:,2]
    
    dates_gfs_1daylead=pd.date_range(start='2023-05-25', end = start_day, freq='1D')
    dates_gfs_2daylead=pd.date_range(start='2023-05-26', end = pd.to_datetime(start_day)+ timedelta(hours=24), freq='1D')
    dates_gfs_3daylead=pd.date_range(start='2023-05-27', end = pd.to_datetime(start_day)+ timedelta(hours=48), freq='1D')
    
    j=0
    for start_date in data_prec.index:
        #dates = pd.date_range(start =start_date,end=pd.to_datetime(start_date)+ timedelta(hours=71),freq='1D')
        dates = pd.date_range(start =pd.to_datetime(start_date)+ timedelta(minutes =30),end=pd.to_datetime(start_date)+ timedelta(hours=71,minutes =30),freq='1D')

        #fig, ax = plt.subplots(figsize=(10, 6))
        #data = predictions[:,j]
        list1 = predictions_today[:,0]
        list2 = predictions_today[:,1]
        list3 = predictions_today[:,2]

        gfs1 = y_pred_gfs[j,0]
        gfs2 = y_pred_gfs[j,1]
        gfs3 = y_pred_gfs[j,2]

        # Combine the three lists into a single list
        data = [list1, list2, list3]

        # Create a figure and axis object
        fig, ax = plt.subplots(figsize=(8, 6))

        # Plot the box plots with fill color and set zorder
        boxplot = ax.boxplot(data, patch_artist=True, medianprops={'color': 'black'}, zorder=1)

        # Add scatter plot
        scatter_x = [1, 2, 3]  # X-coordinates for scatter points
        scatter_y = [gfs1, gfs2, gfs3]  # Y-coordinates for scatter points
        scatter = ax.scatter(scatter_x, scatter_y, color='red', marker='*', s=70, label='GFS Forecast', zorder=2)

        # Set colors for box plots
        colors = ['lightblue', 'lightblue', 'lightblue']
        for patch, color in zip(boxplot['boxes'], colors):
            patch.set_facecolor(color)

        # Add labels and title
        ax.set_xticklabels([dates[0], dates[1], dates[2]], fontsize=12)
        ax.set_ylabel('Daily Rainfall(mm)', fontsize=12)
        ax.set_xlabel('Dates', fontsize=12)
        ax.set_title(f'Predicted Daily Rainfall\nInitialisation: {start_date}', fontsize=14)

        # Set grid lines
        ax.grid(True, linestyle='--', alpha=0.5)

        # Adjust spacing
        plt.tight_layout()

       # Custom legend for box plot
        box_legend = ax.legend(handles=boxplot['boxes'], labels=['GEFS Forecasts downscaled\nby IITB with uncertainty band'], loc='upper left', bbox_to_anchor=(1, 1), fontsize=8)


        # Create a separate axis for the scatter plot legend
        ax_scatter_legend = fig.add_axes([0.83, 0.68 , 0.15, 0.15])  # Adjust the position and size as needed
        scatter_legend = ax_scatter_legend.legend(handles=[scatter], labels=['Original GEFS Forecast from NCEP'], loc='upper left', bbox_to_anchor=(1, 1), fontsize=8)
        ax_scatter_legend.axis('off')  # Turn off axis for scatter plot legend

        #ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

        # Add both legends to the plot
        ax.add_artist(box_legend)


        hour = str(f'{pd.to_datetime(start_date).hour:02}')
        minutes = str(f'{pd.to_datetime(start_date).minute:02}')
        seconds = str(f'{pd.to_datetime(start_date).second:02}')
        date = str(pd.to_datetime(start_date).date())

        # Save the plot as an image file (e.g., PNG or PDF) if needed
        #plt.savefig(f'C:/Users/Admin/Desktop/GFS FORECASTS/boxplottimeseries/{station}/{station}_{date}_{hour}_{minutes}_{seconds}_1.jpg', bbox_inches='tight', dpi=300)
        plt.savefig(f'/home/subimal/Documents/HDFC_Web/Automation/{station}/boxplot1.jpg', bbox_inches='tight', dpi=300)

        # Show the plot
        plt.close(fig)
        j+=1
        
    # Sample time series data
    #time_series_data = predictions_1_day_lead
    print((pd.date_range(start='2023-05-25', end = pd.to_datetime(start_day)).shape))
    print(predictions_1_day_lead.mean(axis=0).shape)
    time_series_data = pd.DataFrame({
        'Date':pd.date_range(start='2023-05-26', end = pd.to_datetime(start_day)+ timedelta(hours=24), freq='1D'),
        'Value':predictions_1_day_lead.mean(axis=0)
    })

    # Sample box plot data
    box_plot_data = predictions_today[:,0]

    # Create a figure and a single subplot
    fig, ax = plt.subplots(figsize=(6, 4))

    # Convert the date to numeric representation
    box_plot_date = pd.to_datetime(start_day) + timedelta(hours=24)
    box_plot_num = mdates.date2num(box_plot_date)

    # Plot the box plot
    ax.boxplot(box_plot_data, vert=True, positions=[box_plot_num], widths=2)

    # Plot the time series
    #ax.plot(time_series_data['Date'], time_series_data['Value'], color='red')
    for i in range(predictions_1_day_lead.shape[0]):
        ax.plot(time_series_data['Date'],predictions_1_day_lead[i], color='red', alpha=0.4, linewidth=0.01)
    ax.plot(time_series_data['Date'], time_series_data['Value'], color='red',linewidth=0.8)
    
    # Set x-axis limit to show only dates from 25th May to 27th July 2023
    ax.set_xlim(pd.to_datetime('2023-05-25'), pd.to_datetime(start_day)+ timedelta(hours=71))

    # Set x-axis ticks at the start of each week
    weekly_ticks = pd.date_range(start='2023-05-25', end=pd.to_datetime(start_day)+ timedelta(hours=71), freq='w')
    ax.set_xticks(weekly_ticks)

    # Format the x-axis date labels as 'YYYY-MM-DD'
    date_format = mdates.DateFormatter('%b-%d')
    ax.xaxis.set_major_formatter(date_format)
    plt.xticks(rotation=45)

    # Set y-axis limits to ensure both plots share the same scale
    y_min = min(min(time_series_data['Value']), min(box_plot_data))
    y_max = max(max(time_series_data['Value']), max(box_plot_data))
    ax.set_ylim(y_min - 5, y_max * 1.5)

    # Set labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Rainfall (mm)')
    ax.set_title('1 day lead')

    # Show the plot
    plt.tight_layout()

    
    # Save the plot as an image file (e.g., PNG or PDF) if needed
    #plt.savefig(f'C:/Users/Admin/Desktop/GFS FORECASTS/boxplottimeseries/{station}/{date}_{hour}_{minutes}_{seconds}1dayleadtime_2023_1.jpg', bbox_inches='tight', dpi=300)
    plt.savefig(f'/home/subimal/Documents/HDFC_Web/Automation/{station}/1dayleadtime_2023.jpg', bbox_inches='tight', dpi=300)

    # Show the plot
    plt.close(fig)
    
    time_series_data = pd.DataFrame({
        'Date':pd.date_range(start='2023-05-27', end = pd.to_datetime(start_day)+ timedelta(hours=48), freq='1D'),
        'Value':predictions_2_day_lead.mean(axis=0)
    })

    # Sample box plot data
    box_plot_data = predictions_today[:,1]

    # Create a figure and a single subplot
    fig, ax = plt.subplots(figsize=(6, 4))

    # Convert the date to numeric representation
    box_plot_date =  pd.to_datetime(start_day) +  pd.Timedelta(2, "d")
    box_plot_num = mdates.date2num(box_plot_date)

    # Plot the box plot
    ax.boxplot(box_plot_data, vert=True, positions=[box_plot_num], widths=2)

    # Plot the time series
    #ax.plot(time_series_data['Date'], time_series_data['Value'], color='red')
    for i in range(predictions_2_day_lead.shape[0]):
        ax.plot(time_series_data['Date'],predictions_2_day_lead[i], color='red', alpha=0.4, linewidth=0.01)
    ax.plot(time_series_data['Date'], time_series_data['Value'], color='red',linewidth=0.8)

    # Set x-axis limit to show only dates from 25th May to 27th July 2023
    ax.set_xlim(pd.to_datetime('2023-05-25'), pd.to_datetime(start_day)+ timedelta(hours=95))

    # Set x-axis ticks at the start of each week
    weekly_ticks = pd.date_range(start='2023-05-25', end=pd.to_datetime(start_day)+ timedelta(hours=95), freq='w')
    ax.set_xticks(weekly_ticks)

    # Format the x-axis date labels as 'YYYY-MM-DD'
    date_format = mdates.DateFormatter('%b-%d')
    ax.xaxis.set_major_formatter(date_format)
    plt.xticks(rotation=45)

    # Set y-axis limits to ensure both plots share the same scale
    y_min = min(min(time_series_data['Value']), min(box_plot_data))
    y_max = max(max(time_series_data['Value']), max(box_plot_data))
    ax.set_ylim(y_min - 5, y_max * 1.5)

    # Set labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Rainfall (mm)')
    ax.set_title('2 day lead')

    # Show the plot
    plt.tight_layout()
    
    # Save the plot as an image file (e.g., PNG or PDF) if needed
    #plt.savefig(f'C:/Users/Admin/Desktop/GFS FORECASTS/boxplottimeseries/{station}/{date}_{hour}_{minutes}_{seconds}2dayleadtime_2023_1.jpg', bbox_inches='tight', dpi=300)
    plt.savefig(f'/home/subimal/Documents/HDFC_Web/Automation/{station}/2dayleadtime_2023.jpg', bbox_inches='tight', dpi=300)

    # Show the plot
    plt.close(fig)
    
    time_series_data = pd.DataFrame({
        'Date':pd.date_range(start='2023-05-28', end = pd.to_datetime(start_day)+ timedelta(hours=72), freq='1D'),
        'Value':predictions_3_day_lead.mean(axis=0)
    })

    # Sample box plot data
    box_plot_data = predictions_today[:,2]

    # Create a figure and a single subplot
    fig, ax = plt.subplots(figsize=(6, 4))

    # Convert the date to numeric representation
    box_plot_date =  pd.to_datetime(start_day) +  pd.Timedelta(3, "d")
    box_plot_num = mdates.date2num(box_plot_date)

    # Plot the box plot
    ax.boxplot(box_plot_data, vert=True, positions=[box_plot_num], widths=2)

    # Plot the time series
    #ax.plot(time_series_data['Date'], time_series_data['Value'], color='red')
    for i in range(predictions_3_day_lead.shape[0]):
        ax.plot(time_series_data['Date'],predictions_3_day_lead[i], color='red', alpha=0.4, linewidth=0.01)
    ax.plot(time_series_data['Date'], time_series_data['Value'], color='red',linewidth=0.8)

    # Set x-axis limit to show only dates from 25th May to 27th July 2023
    ax.set_xlim(pd.to_datetime('2023-05-25'), pd.to_datetime(start_day)+ timedelta(hours=105))

    # Set x-axis ticks at the start of each week
    weekly_ticks = pd.date_range(start='2023-05-25', end=pd.to_datetime(start_day)+ timedelta(hours=105), freq='w')
    ax.set_xticks(weekly_ticks)

    # Format the x-axis date labels as 'YYYY-MM-DD'
    date_format = mdates.DateFormatter('%b-%d')
    ax.xaxis.set_major_formatter(date_format)
    plt.xticks(rotation=45)

    # Set y-axis limits to ensure both plots share the same scale
    y_min = min(min(time_series_data['Value']), min(box_plot_data))
    y_max = max(max(time_series_data['Value']), max(box_plot_data))
    ax.set_ylim(y_min - 5, y_max * 1.5)

    # Set labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Rainfall (mm)')
    ax.set_title('3 day lead')

    # Show the plot
    plt.tight_layout()
    
    #plt.savefig(f'C:/Users/Admin/Desktop/GFS FORECASTS/boxplottimeseries/{station}/{date}_{hour}_{minutes}_{seconds}3dayleadtime_2023_1.jpg', bbox_inches='tight', dpi=300)
    plt.savefig(f'/home/subimal/Documents/HDFC_Web/Automation/{station}/3dayleadtime_2023.jpg', bbox_inches='tight', dpi=300)

    # Show the plot
    plt.close(fig)

    # Show the plot
    plt.close(fig)
    print(f'{station} completed')


# In[ ]:


with open('/home/subimal/Documents/HDFC_Web/Automation/X_test_prec_cnn_lstm_reshaped.pickle', 'wb') as file:
    pickle.dump(X_test_prec_cnn_lstm_hindcast2023_concatenate, file)

