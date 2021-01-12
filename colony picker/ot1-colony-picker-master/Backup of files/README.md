# ot1-colony-picker
Code for using opentrons 1 with OpenCFU to pick 24 well plate colonies
​
#Requirements:
​
- Opentrons OT-1 v2.5.2 software: https://opentrons.com/ot-app
- OpenCFU software: http://opencfu.sourceforge.net/
​
# Protocol:
​
1. Download the ot1-colony-picker repository: https://github.com/LabGenius/ot1-colony-picker
​
2. Get a photo of a 24-well plate containing colonies on it.
​
3. Crop the image so that the sides of the photo correspond to the sides of the plate. (photoeditor = https://www.freephototool.com/).
	Save the photo in jpeg format (example: PathToDownloadedRepository/joel1.jpeg)
​
4. Open OpenCFU Software 
​
5. Upload your croped image by clicking on "Add files"
​
6. Adjust the settings on the left hand side in order to highlight the colonie you want to. Help yourself with the video here: http://opencfu.sourceforge.net/ 
​
7. Select the colonies you want to pick by ticking the boxes corresponding to these colonies, in the lower-right handside of the window ("valid" column)
​
8. Then save the csv file containing the locations of the colonies selected by clicking on "Save all" > "Detailled" > Select the location (pathToDownloadedRepository/csvs)  and name your csv 
​
9. Open the "utils.py" file in an editing software (Sublime for instance: https://www.sublimetext.com/3 or Visual Studio Code) 
​
10. Line 29: change the name of the file to the name of the csv you just downloaded: for instance: "csvs/my_results.csv" will become "csvs/Joel_1.csv" and SAVE. 
    Line 44: change the name of the file to the name of the photo file of the plate you saved in step 3: for instance: "PathToDownloadedRepository/joel1.jpeg"
​
11. Open the "move_to.py" file and remove all the lines below line 11 ("#!--- Robot commands will be inserted here after DO NOT change this line!") and leave a blank line in line 12 and SAVE. 
​
12. Open your terminal, and run "python3 utils.py" from pathToDownloadedRepository.
​
13. Open Opentrons OT-1 v2.5.2 software and upload the "move_to.py" that has just been updated by runing step 12. 
