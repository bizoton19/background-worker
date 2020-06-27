nested_term_query={
    "query": {
        "nested" : {
            "path" : "products",
            "query" : {
              "match" : {"products.Type": "Furniture and Furnishings and Decorations"}       
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