library("dplyr", "hflights")
data(hflights, package="hflights")
dim(hflights)
head(hflights)

hflights_df <- tbl_df(hflights)

filter(hflights_df, Month == 1 & DayofMonth == 1)

arrange(hflights_df, DayofMonth, Month, Year)

mutate(hflights_df, gain = ArrDelay - DepDelay)

planes <- group_by(hflights_df, TailNum)
delay <- summarize(planes,
  count = n(),
  dist = mean(Distance, na.rm=TRUE))
delay

daily <- group_by(hflights_df, Year, Month, DayofMonth)
per_day <- summarize(daily, flights=n())
per_day

hflights %>%
  group_by(Year, Month, DayofMonth) %>%
  select(Year:DayofMonth, ArrDelay, DepDelay) %>%
  summarize(
    arr = mean(ArrDelay, na.rm=TRUE),
    dep = mean(DepDelay, na.rm=TRUE)
  ) %>%
  filter(arr > 30 | dep > 30)