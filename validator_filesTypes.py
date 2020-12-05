#   small monitor hecks
#   work in progress
import json

class JSON_schema:
    '''
    This is a class for working with json schemas

    Attributes:
        schemaData     : json schema content
        filename    : filename of a .schema file

    Methods:

    '''

    def __init__(self, folder, filename):
        '''
        JSON_schema constructor.

        Args:
            filename : filename from which to load schema data & set as schema name
            folder   : path to schema folder
        '''
        with open(folder + filename) as json_file:
            data_TMP = json.load(json_file)
        self.schema_data = data_TMP
        self.filename = filename

    def get_name(self):
        '''
        getName()

        Returns:
            string  : schema filename
        '''
        return self.filename

    def get_data(self):
        '''
        getData()

        Returns:
            string  : schema data
        '''
        return self.schema_data

    def deb_printData(self):
        '''
        Debug fuction. Prints out JSON_schema content.
        '''

        print("#debug. output scheme w/ filename = " + self.filename + " >>> ")
        result_data = json.dumps(self.schema_data, indent=4)
        print(result_data)
##----------- JSON_schema


class JSON_obj:
    '''
    This is a class for working with json data

    Attributes:
        jsonData : json data
        filename : filename to load data from
        folder   : path to json folder
    '''

    def __init__(self, folder, filename):
        '''
        JSON_obj constructor.
        Loads json data and sets object attributes

        Args:
            filename : filename to load data from
            folder   : file folder path
        '''

        with open(folder + filename) as json_file:
            data_TMP = json.load(json_file)
        self.json_data = data_TMP
        self.filename = filename

    def get_name(self):
        '''
        getName()

        Returns:
            string  : json filename
        '''
        return self.filename

    def get_data(self):
        '''
        getData()

        Returns:
            string  : json data
        '''
        return self.json_data

    def deb_printData(self):
        '''
        Debug fuction. Prints out JSON_obj content.
        '''
        print("#debug. output json data w/ filename # " + self.filename + " >>> ")
        result_data = json.dumps(self.json_data, indent=4)
        print(result_data)
##----------- JSON_obj