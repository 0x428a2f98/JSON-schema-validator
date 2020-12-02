#dev start: 02/12
#work in progress
#working version: 5%

import validator_filesTypes         # JSON_obj for .json files and JSON_schema doe .schema files
from os import listdir              #
from os.path import isfile, join    #
from datetime import date           # temp for debuging
import random                       # temp for debuging

class JsonValidator:
    '''
    Main validator class.
    Loads schemas and jsons data and implements specific operations
    for json objects meant for testing them based on provided schemas.
    
    Attributes:
        collectionJsons     : list of validator_filesTypes.JSON_obj
        collectionSchemas   : list of validator_filesTypes.JSON_schema
        debugLvl            : enables extra print statements TMP
    '''

    def __init__(self, jsonFolder, schemaFolder):
        '''
        JsonValidator constructor.
        Inits schemaFolder and jsonFolder. Calls loadJSONS and loadSCHEMAS.
        
        Parameters:
            schemaFolder : folder to look for schemas in.
            jsonFolder   : folder to look for jsons in.
        '''
        self.debugLvl = True        #TMP to_remove debug

        self.collectionJsons = []
        self.collectionSchemas = []
        self.loadJSONS(jsonFolder)
        self.loadSCHEMAS(schemaFolder)


    def loadJSONS(self, jsonFolder):
        '''
        Loads & adds to collectionJsons any file found in jsonFolder as JSON_obj.

        Parameters:
            jsonFolder   : folder to look for jsons in.
        '''
        #TMP to_remove debug
        if(self.debugLvl): print("#debug. loadJSONS() >>> ")
        for f in listdir(jsonFolder):
            if isfile(join(jsonFolder, f)):
                self.collectionJsons.append(validator_filesTypes.JSON_obj(jsonFolder, f))
        #TMP to_remove debug
        if(self.debugLvl): print("Jsons loaded. jsons count = ", len(self.collectionJsons))

    def loadSCHEMAS(self, schemaFolder):
        '''
        Loads & adds to collectionSchemas any file found in schemaFolder as JSON_schema.

        Parameters:
            schemaFolder   : folder to look for schemas in.
        '''
        #TMP to_remove debug
        if(self.debugLvl): print("#debug. loadSCHEMAS() >>> ")
        for f in listdir(schemaFolder):
            if isfile(join(schemaFolder, f)):
                self.collectionSchemas.append(validator_filesTypes.JSON_schema(schemaFolder, f))
        #TMP to_remove debug
        if(self.debugLvl): print("Shemas loaded. shemas count = ", len(self.collectionSchemas))

    '''
    Debug fuction. to_remove
    Prints random JSON_obj index in collectionJsons and its filename.
    '''
    def deb_getRandomJson(self):
        randIndex = random.randint(0, len(self.collectionJsons))
        return([randIndex, self.collectionJsons[randIndex].getName()])

    def deb_printStats(self):
            '''
            Debug fuction. Prints out the number of loaded jsons/schemas.
            '''
            print("#debug. JsonValidator obj. deb_printStats() >>> ")
            print("collectionJsons len: ", len(self.collectionJsons)) 
            print("collectionSchemas len: ", len(self.collectionSchemas))
            deb_randJson = self.deb_getRandomJson()
            print("Random Json index : %i. filename = %s ." % (deb_randJson[0], deb_randJson[1]))
            print(deb_randJson)

    def deb_updateReadme(self):
            '''
            Debug fuction. Prints a placeholder readme file.
            '''
            print("#debug. JsonValidator obj. deb_updateReadme() >>> ")
            f = open("README.md", "w")
            f.write("results will be here. work in progress.")
            f.write("\n")
            f.write("\ncollectionJsons len: %i" % len(self.collectionJsons)) 
            f.write("\ncollectionSchemas len: %i" % len(self.collectionSchemas))
            f.write("\nREADME.md created at %s" % date.today())
            f.close()
            print("README.md updated")

if __name__=="__main__": 
    #Debuging >>
    validator_deb = JsonValidator(jsonFolder="task_folder/event/", schemaFolder="task_folder/schema/")
    validator_deb.deb_printStats()
    validator_deb.deb_updateReadme()

    # test_a = validator_filesTypes.JSON_schema("task_folder/schema/", "cmarker_created.schema")
    # test_b = validator_filesTypes.JSON_schema("task_folder/schema/", "label_selected.schema")
    # test_c = validator_filesTypes.JSON_schema("task_folder/schema/", "sleep_created.schema")
    # test_d = validator_filesTypes.JSON_schema("task_folder/schema/", "workout_created.schema")

    # test_d.deb_printData()