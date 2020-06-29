title_suggest ={
    "suggest": {
        "title-suggest" : {
            "prefix" : "hazrd", 
            "completion" : { 
                "field" : "TitleSuggest",
                "fuzzy" : {
                    "fuzziness" : 2,
                    "min_length" : 3
                },
                "size" : 10
            }
        }
    }
}



