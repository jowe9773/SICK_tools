#extract_wood.py

#import neccesary modules and packages
from sick_tools import SickTools
from file_managers import FileManagers

#instantiate classes
fm = FileManagers()
st = SickTools()

#select files to process
raw_sick_before = fm.load_fn("Select a pre sick file to process")
raw_sick_after = fm.load_fn("Select a post sick file to process")

#select projection
ESPG = 32615 #This is UTM zone 15N

#select a place to store the file
out = fm.load_dn("Select a place to store the output geotiffs")

##DO THE BEFORE TOPO
#load the sick file
sick_before = st.load_sick_file(raw_sick_before)

#interpolate the raw data
interpolated_topo_before = st.fill_nulls(sick_before[0])

#save the sick file as a geotiff
st.export_topo_as_geotiff(raw_sick_before, ESPG, out, interpolated_topo_before, sick_before)

##NOW DO THE AFTER TOPO
#load the sick file
sick_after = st.load_sick_file(raw_sick_after)

#interpolate the raw data
interpolated_topo_after = st.fill_nulls(sick_after[0])

#save the sick file as a geotiff
st.export_topo_as_geotiff(raw_sick_after, ESPG, out, interpolated_topo_after, sick_after)

##Now create the wood map
woodmap = st.extract_wood(interpolated_topo_before, interpolated_topo_after, 5, 2650, 4)

st.export_topo_as_geotiff(raw_sick_after, ESPG, out, woodmap, sick_after, wood = True)
