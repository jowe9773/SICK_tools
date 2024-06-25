#repeat_sick.py

#import neccesary modules and packages
import os
from pathlib import Path
from sick_tools import SickTools
from file_managers import FileManagers

#instantiate classes
fm = FileManagers()
st = SickTools()

#load directory containing data for each experiment organized into individual directories
directory = fm.load_dn("Choose folder containing data organized by experiment")

#select directory to store outputs in
out = fm.load_dn("select directory to store outputs in")

#choose a coordinate system to store data in
ESPG = 32615

# List all subdirectories in the root directory
subdirectories = [os.path.join(directory, d) for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
print(subdirectories)

# Iterate through each subdirectory
for subdir in subdirectories:
    print(f"Processing subdirectory: {subdir}") #print the working subdirectory

    #iterate through the files in the subdirectory and find the files for the "before" and "after"
    for subdir, _, files in os.walk(subdir):
        for file in files:
            filepath = os.path.join(subdir, file)
            if ("_nowood" in filepath or "_pre" in filepath) and ".DAT" in filepath:
                before = Path(filepath).as_posix()
                print("Before was created!")

            if ("_wood" in filepath or "_post" in filepath) and ".DAT" in filepath:
                after = Path(filepath).as_posix()
                print("After was created!")
        
        #Now that we have the before and after files, we can create pre, post, and wood map DEMs
        ##DO THE BEFORE TOPO
        #load the sick file
        sick_before = st.load_sick_file(before)

        #interpolate the raw data
        interpolated_topo_before = st.fill_nulls(sick_before[0])

        #save the sick file as a geotiff
        st.export_topo_as_geotiff(before, ESPG, out, interpolated_topo_before, sick_before)

        ##NOW DO THE AFTER TOPO
        #load the sick file
        sick_after = st.load_sick_file(after)

        #interpolate the raw data
        interpolated_topo_after = st.fill_nulls(sick_after[0])

        #save the sick file as a geotiff
        st.export_topo_as_geotiff(after, ESPG, out, interpolated_topo_after, sick_after)

        ##Now create the wood map
        woodmap = st.extract_wood(interpolated_topo_before, interpolated_topo_after, 5, 2650, 4)

        st.export_topo_as_geotiff(after, ESPG, out, woodmap, sick_after, wood = True)



