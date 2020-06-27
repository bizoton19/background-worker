
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
                        "type":"nested",
                        "properties":{
                           "type": {
                               "type": "text",
                               "fields": {
                                   "Type":{
                                   "type":"keyword"
                                }
                              }
                           },
                           "name":{
                               "type": "text",
                               "fields": {
                                   "Name":{
                                   "type":"keyword"
                                }
                              }
                           }
                        }

                    },
                    "manufacturers":{
                        "type":"nested",
                        "properties":{
                           "name": {
                               "type": "text",
                               "fields": {
                                   "Name":{
                                   "type":"keyword"
                                }
                              }
                           }
                        }

                    },
                    "distributors":{
                        "type":"nested",
                        "properties":{
                           "name": {
                               "type": "text",
                               "fields": {
                                   "Name":{
                                   "type":"keyword"
                                }
                              }
                           }
                        }

                    },
                    "retailers":{
                        "type":"nested",
                        "properties":{
                           "name": {
                               "type": "text",
                               "fields": {
                                   "Name":{
                                   "type":"keyword"
                                }
                              }
                           }
                        }

                    },
                    "importers":{
                        "type":"nested",
                        "properties":{
                           "name": {
                               "type": "text",
                               "fields": {
                                   "Name":{
                                   "type":"keyword"
                                }
                              }
                           }
                        }

                    },
                    "manufacturerCountries":{
                        "type":"nested",
                        "properties":{
                           "country": {
                               "type": "text",
                               "fields": {
                                   "Country":{
                                   "type":"keyword"
                                }
                              }
                           }
                        }

                    },
                    "remedyOptions":{
                        "type":"nested",
                        "properties":{
                           "option": {
                               "type": "text",
                               "fields": {
                                   "Option":{
                                   "type":"keyword"
                                }
                              }
                           }
                        }

                    }
                }
            }
        }
    }
    
    return mappings


