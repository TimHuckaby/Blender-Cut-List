#(c) 2022 Tim Huckaby (@timhuckaby)
#
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####



# import the blender's python API and python's os module
import bpy, os

# select all the mesh objects in the scene
objects = bpy.context.scene.objects
for ob in objects:
    ob.select_set(ob.type == "MESH")

# get the current selection
selection = bpy.context.selected_objects

# initialize a blank result variable
result = ""

# iterate through the selected objects
for sel in selection:
    # get the current object's dimensions; convert from meters to inches and round to 2 decimal places
    dims = sel.dimensions
    x = float(round(sel.dimensions.x * 39.370, 2))
    y = float(round(sel.dimensions.y * 39.370, 2))
    z = float(round(sel.dimensions.z * 39.370, 2))
    # format and output to the screen
    scr = "%s - %.02fin x %.02fin x %.02fin\n" % (sel.name, x, y, z)
    print(scr)
    # write the selected object's name and dimensions to a string for the file output
    # if you want to output to a txt file to open in word, notepad, etc. then use this line:
    # result += "%s - %.02fin x %.02fin x %.02fin\n" % (sel.name, x, y, z)
    # if you want to output to a csv file to open in excel so you can sort, etc. then use this line:
    result += "%s , %.02f , %.02f , %.02f\n" % (sel.name, x, y, z)

# get path to render output (ie: C:\Users\TimHuckaby\)
tempFolder = os.path.expanduser('~')
# make a filename
# if you are creating a text file for word, notepad, etc uncomment this next line:
# filename = os.path.join (tempFolder, "Documents\CutList.txt")
# if you are creating a csv file for excel uncomment this next line:
filename = os.path.join (tempFolder, "Documents\CutList.csv")
# confirm path exists
os.makedirs(os.path.dirname(filename), exist_ok=True)
# open the file to write to
file = open(filename, "w")
# write the data to file
# write the header for excel.  if you are creating a txt file you can comment out this next line:
file.write("Name, Length, Width, Height\n")
file.write(result)
# close the file
file.close()

