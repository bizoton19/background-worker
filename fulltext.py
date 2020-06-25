
mappings_index = "cpsc-recalls-search"
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
                    "title": {
                        "type": "completion"
                    },
                    "recallNumber": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    }
                }
            }
        }
    }
    
    return mappings


