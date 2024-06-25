#clean_sick.py

"""this script can be run to clean the sick file of interest"""

#import neccesary modules and packages
from sick_tools import SickTools
from file_managers import FileManagers

#instantiate classes
fm = FileManagers()
st = SickTools()

#select file to process
raw_sick = fm.load_fn("Select a sick file to process")

#select projection
ESPG = 32615 #This is UTM zone 15N

#select a place to store the file
out = fm.load_dn("Select a place to store the output geotiff")

#load the sick file
sick = st.load_sick_file(raw_sick)

#interpolate the raw data
interpolated_topo = st.fill_nulls(sick[0])

#save the sick file as a geotiff
st.export_topo_as_geotiff(raw_sick, ESPG, out, interpolated_topo, sick)
