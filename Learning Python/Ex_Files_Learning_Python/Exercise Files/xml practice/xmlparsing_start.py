# 
# Example file for parsing and processing XML
#
import xml.dom.minidom

def checkID_Name(mode, ID, Name):
    if mode.getAttribute("Name") == Name:
        if mode.getAttribute("ModeID") != ID:
            mode.setAttribute("ModeID", ID)
            mode.attributes["ModeID"].value = ID

def main():
  # use the parse() function to load and parse an XML file
  doc = xml.dom.minidom.parse("qdcm_calib_data_TD4302_cmd_mode_dsc_dsi_panel.xml")
  
  # print out the document node and the name of the first child tag
  #print(doc.nodeName)
#  print(doc.firstChild.tagName)
  
  # get a list of XML tags from the document and print each one
  modes = doc.getElementsByTagName("Mode")
  print("%d modes: " % modes.length)
  for mode in modes:
      print("ModeID: %s. Name: %s" % (mode.getAttribute("ModeID"), mode.getAttribute("Name")))

      #Make sure ModeID matches with Name
      checkID_Name(mode, 0, "0_None")
      checkID_Name(mode, 1, "1_2D_D75")
      checkID_Name(mode, 2, "2_2D_D75V")
      checkID_Name(mode, 3, "3_2D_D75S")
      checkID_Name(mode, 4, "4_2D_EVT1")
      checkID_Name(mode, 5, "5_3D_Boost")


#    
#  # create a new XML tag and add it into the document
#  newSkill = doc.createElement("skill")
#  newSkill.setAttribute("name", "jQuery")
#  doc.firstChild.appendChild(newSkill)
  print("\n")
  for mode in modes:    
      print("ModeID: %s. Name: %s" % (mode.getAttribute("ModeID"), mode.getAttribute("Name")))

  print("\n")
  print(doc)
if __name__ == "__main__":
  main();

