library(ggplot2)
data("diamonds")
names(diamonds)
summary(diamonds)
?diamonds

qplot(x = price, data = diamonds)
summary(diamonds$price)

sum(diamonds$price < 500)
sum(diamonds$price < 250)
sum(diamonds$price >= 15000)

qplot(x = price, data = diamonds, binwidth = 1000) + 
  scale_x_continuous(lim = c(0, 10000), breaks = seq(0, 10000, 5000))

qplot(x = price, data = diamonds) +
  facet_wrap(~cut, scales = "free") 

qplot(x = price, data = diamonds, geom = 'freqpoly', color = cut)

table(diamonds$cut)
by(diamonds$price, diamonds$cut, summary)

qplot(x = price/carat, data = diamonds) +
  facet_wrap(~cut, scales = "free") +
  scale_x_log10()

qplot(x = color, y = price, 
      data = diamonds, 
      geom = 'boxplot')

by(diamonds$price, diamonds$color, summary)

qplot(x = color, y = price/carat, 
      data = diamonds, 
      geom = 'boxplot')

by(diamonds$price/diamonds$carat, diamonds$color, summary)

qplot(x = carat, data = diamonds, geom = 'freqpoly', xlim = c(0,3), bindwidth = .5)

table(diamonds$carat)


library(gridExtra)


