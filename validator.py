'''
JsonValidator class is implemented in this module.
JsonValidator object loads all files in a provided schema folder as schemas
and all files in json folder as jsons, and validates all jsons against all schemas.
Uses jsonschema lib, or a custom json validation based on a specific task at hand.

dev start: 02/12
work in progress
working version: 10%
'''
from os import listdir              #
from os.path import isfile, join    #
from datetime import date           # temp for debuging
import random                       # temp for debuging

import jsonschema                   # for validating json
# JSON_obj for .json files and JSON_schema for .schema files
import validator_filesTypes


class JsonValidator:
    '''
    Main validator class.
    Loads schemas and jsons data and implements specific operations
    for json objects meant for testing them based on provided schemas.

    Attributes:
        collection_jsons     : list of validator_filesTypes.JSON_obj
        collection_schemas   : list of validator_filesTypes.JSON_schema
        debug_lvl            : enables extra print statements TMP

    Methods:

    '''

    def __init__(self, json_folder, schema_folder):
        '''
        JsonValidator constructor.
        Inits schema_folder and json_folder. Calls loadJSONS and loadSCHEMAS.

        Args:
            schema_folder : folder to look for schemas in.
            json_folder   : folder to look for jsons in.
        '''
        self.debug_lvl = True  # TMP to_remove debug
        self.deb_print(("#debug. JsonValidator obj. __init__(json_folder = %s, "
                        + "schema_folder = %s) >>> ") % (json_folder, schema_folder))

        self.collection_jsons = []
        self.collection_schemas = []

        self.load_JSONS(json_folder)
        self.load_SCHEMAS(schema_folder)

    def validate_schema(self, json_data, schema_data):
        '''
        Validates json_data on schema_data using "jsonschema" library.

        Args:
            json_data   (JSON_obj)       : json to validate
            schema_data (JSON_schema)    : schema
        '''
        self.deb_print("#debug. JsonValidator obj. validate_schema( __ )")
        self.deb_print("_json_data = %s" % json_data.get_name())
        self.deb_print("_schema_data = %s" % schema_data.get_name())

        try:
            jsonschema.validate(instance=json_data.get_data(),
                                schema=schema_data.get_data())
        except jsonschema.ValidationError as e:
            print(e.message)

    def load_JSONS(self, json_folder):
        '''
        Loads & adds to collection_jsons any file found in json_folder as JSON_obj.

        Args:
            json_folder   : folder to look for jsons in.
        '''
        self.deb_print("#debug. JsonValidator obj. loadJSONS() >>> ")

        for file_json in listdir(json_folder):
            if isfile(join(json_folder, file_json)):
                self.collection_jsons.append(
                    validator_filesTypes.JSON_obj(json_folder, file_json))

        self.deb_print("Jsons loaded. jsons count = %i" %
                       len(self.collection_jsons))

    def load_SCHEMAS(self, schema_folder):
        '''
        Loads & adds to collection_schemas any file found in schema_folder as JSON_schema.

        Args:
            schema_folder   : folder to look for schemas in.
        '''
        self.deb_print("#debug. JsonValidator obj. loadSCHEMAS() >>> ")

        for file_schema in listdir(schema_folder):
            if isfile(join(schema_folder, file_schema)):
                self.collection_schemas.append(
                    validator_filesTypes.JSON_schema(schema_folder, file_schema))

        self.deb_print("Shemas loaded. shemas count = %i" %
                       len(self.collection_schemas))

    # Debug ~
    def deb_print(self, text_to_print):
        '''
        Prints %text_to_print only if debug is enabled

        Args:
            text_to_print   : text to print out.
        '''
        if self.debug_lvl:
            print(text_to_print)

    def deb_getRandomJson(self):
        '''
        Debug fuction. to_remove
        Prints random JSON_obj index in collection_jsons and its filename.
        '''
        self.deb_print("#debug. JsonValidator obj. deb_getRandomJson() >>> ")

        rand_index = random.randint(0, len(self.collection_jsons) - 1)
        return([rand_index, self.collection_jsons[rand_index].get_name(),
                self.collection_jsons[rand_index]])

    def deb_printStats(self):
        '''
        Debug fuction. Prints out the number of loaded jsons/schemas.
        '''
        self.deb_print("#debug. JsonValidator obj. self.deb_printStats() >>> ")

        self.deb_print("collection_jsons len: %i" % len(self.collection_jsons))
        self.deb_print("collection_schemas len: %i" %
                       len(self.collection_schemas))
        deb_randJson = self.deb_getRandomJson()
        self.deb_print("Random Json index : %i. filename = %s." %
                       (deb_randJson[0], deb_randJson[1]))
        self.deb_print(deb_randJson)
        for iSchema in self.collection_schemas:
            self.validate_schema(deb_randJson[2], iSchema)

    def deb_updateReadme(self):
        '''
        Debug fuction. Prints a placeholder readme file.
        '''
        self.deb_print("#debug. JsonValidator obj. deb_updateReadme() >>> ")

        readme_file = open("README.md", "w")
        readme_file.write("results will be here. work in progress.")
        readme_file.write("\n")
        readme_file.write("\ncollection_jsons len: %i." %
                          len(self.collection_jsons))
        readme_file.write("\ncollection_schemas len: %i." %
                          len(self.collection_schemas))
        readme_file.write("\nREADME.md created at %s." % date.today())
        readme_file.close()
        print("README.md updated")
##----------- JsonValidator


if __name__ == "__main__":
    # Debuging >>
    validator_deb = JsonValidator(
        json_folder="task_folder/event/", schema_folder="task_folder/schema/")
    validator_deb.deb_printStats()
    validator_deb.deb_updateReadme()

    # test_a = validator_filesTypes.JSON_schema("task_folder/schema/", "cmarker_created.schema")
    # test_b = validator_filesTypes.JSON_schema("task_folder/schema/", "label_selected.schema")
    # test_c = validator_filesTypes.JSON_schema("task_folder/schema/", "sleep_created.schema")
    # test_d = validator_filesTypes.JSON_schema("task_folder/schema/", "workout_created.schema")

    # test_d.self.deb_printData()
