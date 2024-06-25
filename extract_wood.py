#extract_wood.py

#import neccesary modules and packages
from sick_tools import SickTools
from file_managers import FileManagers

#instantiate classes
fm = FileManagers()
st = SickTools()

class ExtractWood:
    def __init__(self):
        print("initialized")

    def extract_wood(self, before, after, ESPG, out):

        ##DO THE BEFORE TOPO
        #load the sick file
        sick_before = st.load_sick_file(before)

        #interpolate the raw data
        interpolated_topo_before = st.fill_nulls(sick_before[0])
        ##NOW DO THE AFTER TOPO
        #load the sick file
        sick_after = st.load_sick_file(after)

        #interpolate the raw data
        interpolated_topo_after = st.fill_nulls(sick_after[0])

        ##Now create the wood map
        woodmap = st.extract_wood(interpolated_topo_before, interpolated_topo_after, 5, 2650, 4)

        st.export_topo_as_geotiff(before, ESPG, out, interpolated_topo_before, sick_before)
        st.export_topo_as_geotiff(after, ESPG, out, interpolated_topo_after, sick_after)
        st.export_topo_as_geotiff(after, ESPG, out, woodmap, sick_after, wood = True)
