def exact_product_type(term):
    return {
        "size":"20",
        "query": {
            "nested" : {
                "path" : "products",
                "query" : {
                "term" : {"products.Type.keyword": term}       
                }
        }    
        }
    }
def exact_manufacturer(term):
    return {
        "size":"20",
        "query": {
            "nested" : {
                "path" : "manufacturers",
                "query" : {
                "term" : {"manufacturers.Name.keyword": term}       
                }
        }    
        }
    }
fulltext_queryString = {
    "query": {
        "query_string" : {
            "default_field" : "fulltext",
            "query" : "(chair) AND (target)" 
        }
    }
}

exact_phrase_match =  {
    "query": {
        "match_phrase" : {
            "fulltext" : "IKEA North America, of Conshohocken, Pa."
            

        }
    }
}