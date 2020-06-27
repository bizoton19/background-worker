aggs_only={
     "size":0,
     "aggs" : {
        "products" : {
            "nested" : {
                "path" : "products"
            },
            "aggs" : {
                "prod_type" : { "terms" : { "field" : "products.Type.keyword" } }
                
            }
        },
         "manufacturers" : {
            "nested" : {
                "path" : "manufacturers"
            },
            "aggs" : {
               "manufacturers" : { "terms" : { "field" : "manufacturers.Name.keyword" } }
                
            }
        },
         "manufacturerCountries" : {
            "nested" : {
                "path" : "manufacturerCountries"
            },
            "aggs" : {
                "manufactuterCountries" : { "terms" : { "field" : "manufacturerCountries.Name.keyword" } }
                
            }
        }
    }
 }

