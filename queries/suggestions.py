title_suggest ={
    "suggest": {
        "song-suggest" : {
            "prefix" : "hazrd", 
            "completion" : { 
                "field" : "title_suggest",
                "fuzzy" : {
                    "fuzziness" : 2,
                    "min_length" : 3
                },
                "size" : 10
            }
        }
    }
}



