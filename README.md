# SICK_tools
Tools to read and manipulate data from a SICK branded 3d line scanner.

For my purposes, I want to take the raw data files from the sick scanner and turn them into geotiff files. My end goal is a "before" scan, and "after" scan and a "change" scan in which I identifty changes of a certain magnitude and geographic size.

I have written files that can process one experiment, or a batch of experiments, as long as the file stucture is correct. For me, it made the most sense to have all data files for each experiment in one directory, then repeats of the same experimental setup within a directory. All of these directories are then in one directory, which is selected and the whole thing is processed. 
