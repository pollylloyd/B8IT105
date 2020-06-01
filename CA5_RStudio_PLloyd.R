install.packages("ggplot2")
library(ggplot2)
install.packages(c("MASS", "dplyr"))
library(MASS)
library(dplyr)

df <- read.csv('avocado.csv')

# Confirm the class of the data set is a data frame
class(df)
head(df)
summary(df)

# To show the unique values/ attributes of each data column
unique_vals <- lapply(df, unique)
View(unique_vals)

# Example of showing unique names of one characteristic - regions only
unique_vals[["region"]]
#*****
#convert to categorical variable
df$type <-as.factor(df$type)
df$region <-as.factor(df$region)
df$year = as.factor(df$year)
#convert to date type
df$Date <- as.Date(df$Date, "%Y-%m-%d")
# order date
df <- df[order(as.Date(df$Date, format="%Y-%m-%d")),]

class(df$Date) # checks date conversion


#check for null/NA values
is.na(df)  
is.null(df)
#No null values


# To return the MEAN, MEDIAN, RANGE 
summary(df)
summary(df$AveragePrice) # specifically the above for AveragePrice
summary(df$Total.Volume) # specifically the above for Total Volume
sum(df$Total.Volume) # returns the sum of all volumes

#Plot a simple Histogram
hist(df$AveragePrice, main="Distribution of Average Prices",xlab="Average Price in USD $",ylab="Frequency")


# Create basic barchart
ggplot(df, aes(x = year, y = Total.Volume)) +
  geom_col(fill = "purple")+
  labs(x = "Year", y ="Total Volume", title = "Volume of Avocados by Year")


##Volume by Year and Type - Stacked bar chart
options(repr.plot.width= 5, repr.plot.height=5)
ggplot(df, aes(x = year, y = Total.Volume, fill = type)) +
  geom_col() +
  labs(colour = "type", x = "Type", y ="Volume", title = "Volume of Avocados by Year and Type")

##Ave Price by year and type
options(repr.plot.width= 12, repr.plot.height=6)
ggplot(df, aes(type, AveragePrice))+
  geom_boxplot(aes(colour = year))+
  labs(colour = "Year", x = "Type", y ="Average Price USD$", title = "Average Prices of Avocados by Year and Type - with Outliers")


# Create a scatter plot
options(rep.plot.width = 20, repr.plot.height = 20)
ggplot(df, aes(x = AveragePrice, y = Total.Volume)) +
  geom_point(aes(colour = type))+
  labs(colour = "type", x = "Ave Price USD$", y ="Volume", title = "Scatterplot showing Volume and Average Price (in USD$) for all Avocados")

# Average Price by region
options(repr.plot.width= 12, repr.plot.height=6)
ggplot(df, aes(region, AveragePrice))+
  geom_boxplot(aes(colour = region))+
  theme(axis.text.x = element_blank())+
  labs(colour = "region", y ="Average Price USD$", title = "Average Prices by Region")



# Filter by type
organic <- df %>% select(Date, AveragePrice, type, Total.Volume) %>% filter(type == "organic")
conventional <- df %>% select(Date, AveragePrice, type, Total.Volume) %>% filter(type == "conventional")

organic
conventional


groupedyt = df %>% 
  group_by(year, type) %>% 
  select(year, type, AveragePrice) %>%
  summarise(averagePrice = mean(AveragePrice))

groupedyt






