parse_phone_number <- function(number_string) {
  all_nums <- gsub("\\D", "", number_string)
  re <- "^(1|)([2-9][0-9]{2}[2-9][0-9]{6})$"
  if (grepl(re, all_nums)) {
    gsub(re, "\\2", all_nums)
  } else {
    NULL
  }
}
