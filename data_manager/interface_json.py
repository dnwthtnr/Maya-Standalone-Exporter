import json



class InterfaceJSON( ):

    def __init__(   self, json, overwrite = False, 
                    object_instance = True, rootdir = 'Desktop' ):

        #super( InterfaceJSON, self ).__init__( )
        
        self.schema = json                  # original json
        
        self.cache = dict                   # floating dictionary for quick access
        self.instance = object_instance     # if class instance is being used to manage 1 json or just as general commands
        
        if overwrite == False:              # location to save cache and if you want to overwrite self.schema
            #self.file = 'data_write.json'
            self.file = '{}\cache\data_write.json'.format( rootdir )

        else:
            self.file = self.schema


    # read and return given json
    def json_reader( self, directory = None ):

        if self.instance == True:
            directory = self.schema
        

        with open( directory ) as json_file:
            dict = json.load( json_file )


        if self.instance == True:
            self.cache = dict
            print( 'json successfully opened as cache' )

        return dict

    # write given json to disk - either overwrite loaded json or save as new
    def json_write( self, data, directory ):

        # if being used to manage one data set
        if self.instance == True:
            directory = self.file
            data = self.cache

        # write self.json to disk
        with open( directory, 'w' ) as json_file:
            json_file.write( data )

        

    # add data to floating dict
    def dict_add( self, dict_location, key, value, iterate = False ):

        if value is list():
            print('list')

        if iterate == True:
            new_dict = self.dict_pack(  key = key, 
                                        value = value )

        else:
            new_dict = { str(key) : value }
        
        dict_location.update( new_dict )

        pass

    # iteratively add values to keys -- creating new dictionary
    def dict_pack( self, key, value ):

        dictionary = dict()

        if key == int:          # int if you want them numbered instead of string keys

            iterations = value

        # if keys and values are same len then iterate together
        #if value>key then put multiple values under key
        #if key>value put same value under keys

        for i, item in enumerate(iterations):

            dictionary[ str( i ) ] = str(item)

        return dictionary



    # TODO: parse through given dict and return values and eval type ( var(), exec() )
    def json_unpack( self, dict ):
        pass