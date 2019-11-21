##import arcpy
##fc = r"H:\PythonGIS\Ploderer\data\data\geoportal.gdb\Fire"
##targetPrj = r"H:\...TNoutline_projected.shp"
##arcpy.Project_management(fc, r"H:\ ... geoportal.gdb\Fire_reprojected", targetPrj)



import arcpy
##arcpy.env.workspace = r"H:\... geoportal.gdb"
##fcList = arcpy.ListFeatureClasses("H*")
##print fcList

targetFc = r"H:\ ... USA.gdb\TNoutline" #navigate to folder
targetSR = arcpy.Describe(targetFc).Spatialreference.Name
##print targetSR
##outFolder = r"H:\... \USA.gdb\\"
##
##for fc in fcList:
##    fcSR = arcpy.Describe(fc).SpatialReference.Name
##    if fcSR != targetSR:
##        arcpy.Project_management(fc, outFolder+fc+"_projected", targetPrj)
##    else:
##        print "SR is same as target SR."

import arcpy
inFolder = r"H:\PythonGIS\Ploderer\ArcpyLesson1\data1\data1\Lesson1" #navigate to correct folder
arcpy.env.workspace = inFolder
fcList = arcpy.ListFeatureClasses("T*")
print fcList

for fc in fcList:
    fcSR = arcpy.Describe(fc).SpatialReference.Name
    in fcSR != targetSR:
        arcpy.Project_management(fc, outFolder + fc[:-4] + "_projected.shp", targetSR)
    else:
        print "SR is same"
        

for fc in fcList:
    print fc