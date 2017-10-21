
##1st:
###Diamonds

```r
> library(ggplot2)
> data(diamonds)
> 
> dim(diamonds)
[1] 53940    10
> str(diamonds)
Classes 'tbl_df', 'tbl' and 'data.frame':    53940 obs. of  10 variables:
 $ carat  : num  0.23 0.21 0.23 0.29 0.31 0.24 0.24 0.26 0.22 0.23 ...
 $ cut    : Ord.factor w/ 5 levels "Fair"<"Good"<..: 5 4 2 4 2 3 3 3 1 3 ...
 $ color  : Ord.factor w/ 7 levels "D"<"E"<"F"<"G"<..: 2 2 2 6 7 7 6 5 2 5 ...
 $ clarity: Ord.factor w/ 8 levels "I1"<"SI2"<"SI1"<..: 2 3 5 4 2 6 7 3 4 5 ...
 $ depth  : num  61.5 59.8 56.9 62.4 63.3 62.8 62.3 61.9 65.1 59.4 ...
 $ table  : num  55 61 65 58 58 57 57 55 61 61 ...
 $ price  : int  326 326 327 334 335 336 336 337 337 338 ...
 $ x      : num  3.95 3.89 4.05 4.2 4.34 3.94 3.95 4.07 3.87 4 ...
 $ y      : num  3.98 3.84 4.07 4.23 4.35 3.96 3.98 4.11 3.78 4.05 ...
 $ z      : num  2.43 2.31 2.31 2.63 2.75 2.48 2.47 2.53 2.49 2.39 ...
> str(diamonds$color)
 Ord.factor w/ 7 levels "D"<"E"<"F"<"G"<..: 2 2 2 6 7 7 6 5 2 5 ...
```
##2nd:
###histogram of diamonds price
```r
> ggplot(diamonds)+geom_histogram(aes(x=price),color='black',fill='blue')
```
##3rd: 
###the summary of the diamonds price
```r
> summary(diamonds$price)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    326     950    2401    3933    5324   18823 
```
##4th:
###Diamond Counts
```r
> nrow(subset(diamonds,price<500))
[1] 1729
> nrow(subset(diamonds,price<250))
[1] 0
> nrow(subset(diamonds,price>=15000))
[1] 1656
```
##5th:
###Exploring the Peak
```r
> ggplot(diamonds)+
+   geom_histogram(aes(x=price),binwidth = 5,color='black',fill='lightgreen')+
+   scale_x_continuous(limits=c(0,1200))
```
##6th:
###Price by cut histogram
```r
> ggplot(diamonds)+
+   geom_histogram(aes(x=price),binwidth = 5,color='black',fill='lightblue')+
+   facet_wrap(~cut)
```
##7th:
### Price by Cut
```r
> summary(diamonds$price)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    326     950    2401    3933    5324   18823 
> #diamonds[diamonds$price==18823,]
> #diamonds[diamonds$price==326,]
> by(diamonds$price,diamonds$cut,summary)
diamonds$cut: Fair
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    337    2050    3282    4359    5206   18574 
------------------------------------------------------ 
diamonds$cut: Good
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    327    1145    3050    3929    5028   18788 
------------------------------------------------------ 
diamonds$cut: Very Good
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    336     912    2648    3982    5373   18818 
------------------------------------------------------ 
diamonds$cut: Premium
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    326    1046    3185    4584    6296   18823 
------------------------------------------------------ 
diamonds$cut: Ideal
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    326     878    1810    3458    4678   18806 
```
##8th:
###Scales and Multiple Histograms
```r
> ggplot(aes(x=price),data=diamonds)+
+   geom_histogram()+
+   facet_wrap(~cut,scales = 'free_y',ncol=2)
```
##9th:
###Price per Carat by Cut
```r
> ggplot(aes(x=price/carat),data=diamonds)+
+   geom_histogram(binwidth = 0.05,color='blue',fill='lightblue')+
+   scale_x_log10()+
+   facet_wrap(~cut,ncol = 2)
```
##10th:
###Price Box Plots:
```r
> by(diamonds$price,diamonds$clarity,summary)
diamonds$clarity: I1
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    345    2080    3344    3924    5161   18531 
------------------------------------------------------ 
diamonds$clarity: SI2
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    326    2264    4072    5063    5777   18804 
------------------------------------------------------ 
diamonds$clarity: SI1
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    326    1089    2822    3996    5250   18818 
------------------------------------------------------ 
diamonds$clarity: VS2
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    334     900    2054    3925    6024   18823 
------------------------------------------------------ 
diamonds$clarity: VS1
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    327     876    2005    3839    6023   18795 
------------------------------------------------------ 
diamonds$clarity: VVS2
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
  336.0   794.2  1311.0  3283.7  3638.2 18768.0 
------------------------------------------------------ 
diamonds$clarity: VVS1
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    336     816    1093    2523    2379   18777 
------------------------------------------------------ 
diamonds$clarity: IF
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    369     895    1080    2865    2388   18806 
> ggplot(aes(x=clarity,y=price),data=diamonds)+
+   geom_boxplot()+
+   coord_cartesian(ylim=c(0,10000))
>   scale_y_continuous(breaks = seq(0,10000,2000))
```
##11th:
###Interquartile range - IQR
```r

> by(diamonds$price,diamonds$color,summary)
diamonds$color: D
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    357     911    1838    3170    4214   18693 
------------------------------------------------------ 
diamonds$color: E
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    326     882    1739    3077    4003   18731 
------------------------------------------------------ 
diamonds$color: F
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    342     982    2344    3725    4868   18791 
------------------------------------------------------ 
diamonds$color: G
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    354     931    2242    3999    6048   18818 
------------------------------------------------------ 
diamonds$color: H
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    337     984    3460    4487    5980   18803 
------------------------------------------------------ 
diamonds$color: I
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    334    1120    3730    5092    7202   18823 
------------------------------------------------------ 
diamonds$color: J
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    335    1860    4234    5324    7695   18710 
> IQR(subset(diamonds, color=='J')$price)
[1] 5834.5
> IQR(subset(diamonds, color=='D')$price)
[1] 3302.5
```
##12th:
###Price per Carat Box Plots by Color
```r
> ggplot(aes(x=color,y=price/carat),data=diamonds)+
+   geom_boxplot()+
+   ggtitle('price per carat by color')
```
##13th:
###Carat frequency polygon
```r
> ggplot(aes(x=carat),data=diamonds)+
+   geom_freqpoly(binwidth = 0.02)+
+   scale_x_continuous(limits = c(0,1.5),breaks = seq(0,1.5,0.1))
```
##14th:
###Gapminder data
http://note.youdao.com/noteshare?id=cf5b36b2df849af9dcd24bb3da8c1cd6
##15th:
###Birthday Histograms
```r
#load and cleaning data
library(lubridate)
birthdays <- read.csv("birthdays.csv")
birthdays$dates <- mdy(birthdays$dates)
birthdays$month <- month(birthdays$dates)
birthdays$day <- day(birthdays$dates)
#some basic analysis:
summary(birthdays)
table(birthdays$month)
table(birthdays$day)
##how many people share your birthday?
my<-subset(birthdays,month==02 & day==11)
nrow(my)
##which mongth contains the most number of birthdays?
ggplot(aes(x=month),data=birthdays)+
  geom_histogram(color='black',fill='blue',binwidth = 1)+
  scale_x_discrete()+
  scale_y_discrete()+
  ggtitle('birthdays in each month')
##how many birthdays are in each month?
table(birthdays$month)
##which day of the year has the most number of birthdays?
ggplot(aes(x=day),data=birthdays)+
  geom_histogram(color='black',fill='blue',binwidth = 1)+
  scale_x_discrete()+
  scale_y_discrete()+
  ggtitle('birthdays in each day')
##do you have at least 365 friends that have birthday on everyday of the year?
length(unique(birthdays$dates))
```


















