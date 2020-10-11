acronym <- function(input) {
    filteredString = gsub('-',' ',input)
    return (gsub('_',' ',filteredString)
            %>% strsplit(" ")
            %>% unlist 
            %>% substr(1,1)
            %>% paste(collapse = "")
            %>% toupper)
    }

