space_age <- function(seconds, planet) {
  earthyears <- seconds/31557600;
  
  switch (planet,
    "earth" = years <- earthyears,
    "mercury" = years <- earthyears/0.2408467,
    "venus" = years <- earthyears/0.61519726,
    "mars" = years <- earthyears/1.8808158,
    "jupiter" = years <- earthyears/11.862615,
    "saturn" = years <- earthyears/29.447498,
    "uranus" = years <- earthyears/84.016846,
    "neptune" = years <- earthyears/164.79132,
    
  )
  return (round(years, digits = 2))
}
