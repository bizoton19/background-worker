
mappings_index = "cpsc-recalls"
def mappings():
    """sets elasticsearch mappings for recall search 

  Returns:
   the mapping
  """
    mappings = {
        "mappings": {
            "recall": {
                "properties": {
                    "fulltext": {
                        "type": "text"
                    },
                    "TitleSuggest": {
                        "type": "completion"
                       
                    },
                    "RecallNumber": {
                        "type": "text"
                        
                    
                    },
                    "ConsumerContact":{
                        "type": "text"
                    },
                    "Products":{
                        "type":"nested"

                    },
                    "Manufacturers":{
                        "type":"nested"

                    },
                    "Distributors":{
                        "type":"nested"

                    },
                    "Retailers":{
                        "type":"nested"

                    },
                    "Importers":{
                        "type":"nested"
                    },
                    "ManufacturerCountries":{
                        "type":"nested"
                    },
                    "RemedyOptions":{
                        "type":"nested"
                    }
                }
            }
        }
    }
    
    return mappings


