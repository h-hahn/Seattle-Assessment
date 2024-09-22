# to run this script successfully:
# create a data folder in your working directory that contains '2024_03_21.csv' and '2024_03_21_14-12-23.mp4' 
# create an outputs folder in your working directory for images to save to

# import necessary libraries to begin ----
import pandas as pd
import cv2 
import numpy as np

#######################################################################################
# --OBJECTIVE 1: Calculate cumulative distance traveled by ROV using telemetry data-- #
#######################################################################################

# read in telemetry data csv file 
telemetry = pd.read_csv('data/2024_03_21.csv')

# the time of the video begins at 14:12:23 and ends at 14:13:23 (1 minute long)
# I checked to see which rows these values were between (uncomment next 2 lines to view rows)
#print(telemetry[telemetry['time']=='14:12:23'])
#print(telemetry[telemetry['time']=='14:13:23'])

# subset the telemetry dataset to data in video based on previous row values
telemetry_subset = telemetry.iloc[100:161]

# change first distance point to 0 because this is the start point for the beginning of the video
telemetry_subset.at[100,'distance'] = 0

# make sure that the dataframe is correct (uncomment next line to check)
# print(telemetry_subset)

# determine total distance ROV moved in video by taking the sum of values of 'distance' column
print(telemetry_subset['distance'].sum())

### the total distance moved by the ROV in the video is ~6.23 ###
### this means that there will be 6 total images resulting from objective 2 ###

# now determine what time points the ROV moved a meter based on cumulative distance 
# this calculates the cumulative distance that the ROV has moved (round down to see when each meter is hit since values will not be exact)
telemetry_subset['cumulative_distance'] = telemetry_subset['distance'].cumsum().apply(np.floor)

# the distance column now has duplicate values, select for only the first of each value (which time point first hits that distance)
telemetry_subset = telemetry_subset.drop_duplicates(subset=['cumulative_distance'])

# yay now we can see what time points move 1 meter (uncomment next line to view)
#print(telemetry_subset[['time', 'cumulative_distance']]) 

##########################################################################
# --OBJECTIVE 2: Extract a .jpeg image for every 1 meter the ROV moves-- #
##########################################################################

# load in video using opencv (cv2)
rov_vid = cv2.VideoCapture('data/2024_03_21_14-12-23.mp4')

# Get the frame rate of the video
fps = rov_vid.get(cv2.CAP_PROP_FPS)

# each meter occurs at 9, 21, 30, 40, 49, 59 seconds into the video (look at subsetted telemetry dataframe above)
# calculate the frames at each meter point 
frame1 = int(9 * fps) # first meter
frame2 = int(21 * fps) # second meter
frame3 = int(30 * fps) # third meter
frame4 = int(40 * fps) # fourth meter
frame5 = int(49 * fps) # fifth meter
frame6 = int(59 * fps) # sixth meter

# I could not find a way to extract the images in one command because the intervals are not consistent 
# I will do it individually

# -------- 1 meter - 14:12:32 (9 seconds after beginning of video) --------
# Set the video capture to the first frame value (9 seconds into the video)
rov_vid.set(cv2.CAP_PROP_POS_FRAMES, frame1)

# Read the first frame 
success, image1 = rov_vid.read()

# if the frame is read successfully, save to outputs folder with correct timestamp
if success:
    print(f"Frame1 read successfully.")
    cv2.imwrite(f"outputs/14-12-32.jpg", image1)
# if unsuccessful print fail message to see which image failed
else:
    print(f"Failed to read frame1.")

# -------- 2 meters - 14:12:44 (21 seconds after beginning of video) --------
# Set the video capture to the second frame value (21 seconds into the video)
rov_vid.set(cv2.CAP_PROP_POS_FRAMES, frame2)

# Read the specified frame
success, image2 = rov_vid.read()

# if the frame is read successfully, save to outputs folder
if success:
    print(f"Frame2 read successfully.")
    cv2.imwrite(f"outputs/14-12-44.jpg", image2)
# if unsuccessful print fail message to see which image failed
else:
    print(f"Failed to read frame2.")

# -------- 3 meters - 14:12:53 (30 seconds after beginning of video) --------
# Set the video capture to the third frame value (30 seconds into the video)
rov_vid.set(cv2.CAP_PROP_POS_FRAMES, frame3)

# Read the specified frame
success, image3 = rov_vid.read()

# if the frame is read successfully, save to outputs folder
if success:
    print(f"Frame3 read successfully.")
    cv2.imwrite(f"outputs/14-12-53.jpg", image3)
# if unsuccessful print fail message to see which image failed
else:
    print(f"Failed to read frame3.")

# -------- 4 meters - 14:13:03 (40 seconds after beginning of video) --------
# Set the video capture to the fourth frame value (40 seconds into the video)
rov_vid.set(cv2.CAP_PROP_POS_FRAMES, frame4)

# Read the specified frame
success, image4 = rov_vid.read()

# if the frame is read successfully, save to outputs folder
if success:
    print(f"Frame4 read successfully.")
    cv2.imwrite(f"outputs/14-13-03.jpg", image4)
# if unsuccessful print fail message to see which image failed
else:
    print(f"Failed to read frame4.")

# -------- 5 meters - 14:13:12 (49 seconds after beginning of video) --------
# Set the video capture to the fifth frame value (49 seconds into the video)
rov_vid.set(cv2.CAP_PROP_POS_FRAMES, frame5)

# Read the specified frame
success, image5 = rov_vid.read()

# if the frame is read successfully, save to outputs folder
if success:
    print(f"Frame5 read successfully.")
    cv2.imwrite(f"outputs/14-13-12.jpg", image5)
# if unsuccessful print fail message to see which image failed
else:
    print(f"Failed to read frame5.")

# -------- 6 meters - 14:13:22 (59 seconds after beginning of video) --------
# Set the video capture to the sixth frame value (59 seconds into the video)
rov_vid.set(cv2.CAP_PROP_POS_FRAMES, frame6)

# Read the specified frame
success, image6 = rov_vid.read()

# if the frame is read successfully, save to outputs folder
if success:
    print(f"Frame6 read successfully.")
    cv2.imwrite(f"outputs/14-13-22.jpg", image6)
# if unsuccessful print fail message to see which image failed
else:
    print(f"Failed to read frame6.")

### ---All images were downloaded successfully to the outputs folder--- ###