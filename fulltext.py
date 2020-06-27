
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
                    "title_suggest": {
                        "type": "completion"
                       
                    },
                    "recallNumber": {
                        "type": "text"
                        
                    
                    },
                    "consumerContact":{
                        "type": "text"
                    },
                    "products":{
                        "type":"nested"

                    },
                    "manufacturers":{
                        "type":"nested"

                    },
                    "distributors":{
                        "type":"nested"

                    },
                    "retailers":{
                        "type":"nested"

                    },
                    "importers":{
                        "type":"nested"
                    },
                    "manufacturerCountries":{
                        "type":"nested"
                    },
                    "remedyOptions":{
                        "type":"nested"
                    }
                }
            }
        }
    }
    
    return mappings


