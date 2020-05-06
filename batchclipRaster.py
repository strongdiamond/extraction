# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace=arcpy.GetParameterAsText(0)
inRaster=arcpy.GetParameterAsText(1)
inMaskData =arcpy.GetParameterAsText(2)
savepath=arcpy.GetParameterAsText(3)
# Set environment settings
#env.workspace = ws
#path="E:\\tttt\\tt"
# Set local variables
#inRaster = "090160.tif"
#inMaskData = "mask.shp"
 
# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")
 
cursor = arcpy.SearchCursor(inMaskData)
 
for row in cursor:
    mask = row.getValue("Shape")
    code = row.getValue("CountyName")  # name the output layer by COUNTRY_NA field
    outExtractByMask = ExtractByMask(inRaster,mask)
    outExtractByMask.save(savepath + "\\" +code + ".tif")