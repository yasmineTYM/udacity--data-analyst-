Exercise1:create a scatterplot of price vs x
----------------------------
```{r}
ggplot(aes(x=x,y=price),data=diamonds)+
  geom_point()
```
Exercise3:Correlation between price and x,price and y, price and z
----------------------------
```{r}
with(diamonds,cor.test(price,x))
with(diamonds,cor.test(price,y))
with(diamonds,cor.test(price,z))
```
<p>
Pearson's product-moment correlation

data:  price and x <br />
t = 440.16, df = 53938, p-value < 2.2e-16 <br />
alternative hypothesis: true correlation is not equal to 0 <br />
95 percent confidence interval: <br />
 0.8825835 0.8862594 <br />
sample estimates: <br />
      cor <br />
0.8844352 <br />


Pearson's product-moment correlation

data:  price and y<br />
t = 401.14, df = 53938, p-value < 2.2e-16 <br />
alternative hypothesis: true correlation is not equal to 0 <br />
95 percent confidence interval: <br />
 0.8632867 0.8675241 <br />
sample estimates: <br />
      cor  <br />
0.8654209  <br />

Pearson's product-moment correlation<br />

data:  price and z<br />
t = 393.6, df = 53938, p-value < 2.2e-16<br />
alternative hypothesis: true correlation is not equal to 0<br />
95 percent confidence interval:<br />
 0.8590541 0.8634131<br />
sample estimates:<br />
      cor <br />
0.8612494 <br />
</p>

Exercise4:Scatterplot of Price vs Depth
----------------------------
```{r}
ggplot(aes(x=price,y=depth),data=diamonds)+
  geom_point()
```

Exercise5:Make Transparency and Mark the x-ais
----------------------------
```{r}
ggplot(data = diamonds, aes(x = depth, y = price)) + 
  geom_point(alpha=0.01)+
  scale_x_continuous(breaks = seq(50,75,2))
```
Exercise7:The correlation of depth vs. price
----------------------------
```{r}
with(diamonds,cor.test(depth,price))
```

Pearson's product-moment correlation <br />

data:  depth and price<br />
t = -2.473, df = 53938, p-value = 0.0134<br />
alternative hypothesis: true correlation is not equal to 0<br />
95 percent confidence interval:<br />
 -0.019084756 -0.002208537<br />
sample estimates:<br />
       cor <br />
-0.0106474 <br />

Exercise9:Scatterplot of price vs. carat
----------------------------
```{r}
ggplot(aes(x=carat,y=price),data=diamonds)+
  geom_point()
```

Exercise9`:Omit the top1% of Price and Carat
----------------------------
```{r}
top_price <- quantile(diamonds$price,probs = 0.99)
top_carat <- quantile(diamonds$carat, probs = 0.99)
data <- subset(diamonds, diamonds$price < top_price & diamonds$carat < top_carat)

ggplot(data = data,
       aes(x = carat, y = price)) + geom_point()
```
Exercise9``: New Variable for Volume
----------------------------
```{r}
diamonds$volume<-diamonds$x*diamonds$y*diamonds$z
ggplot(aes(x=volume,y=price),data=diamonds)+
  geom_point()
```
Exercise11: Correlation of Price and Volume
----------------------------
```{r}
diamonds_right_volume<-subset(diamonds,diamonds$volume!=0 & diamonds$volume<800)
with(diamonds_right_volume,cor.test(price,volume))
```

```{r}
diamonds_right_volume<-subset(diamonds,diamonds$volume!=0 & diamonds$volume<800)
ggplot(aes(x=volume,y=price),data=diamonds_right_volume)+
  geom_point(alpha=0.01)+
  geom_smooth(method='lm')
```
Exercise12: New data Frame by Clarity
----------------------------
```{r}
library(dplyr)
clarity_groups<-group_by(diamonds,clarity)
diamondsByClarity<-summarise(clarity_groups,
          mean_price=mean(as.numeric(price)),
          median_price=median(as.numeric(price)),
          min_price=min(as.numeric(price)),
          max_price=max(as.numeric(price)),
          n=n())
```
Exercise14: Create Two Bar Plots on one output
----------------------------
```{r}
data(diamonds)
library(dplyr)

diamonds_by_clarity <- group_by(diamonds, clarity)
diamonds_mp_by_clarity <- summarise(diamonds_by_clarity, mean_price = mean(price))


diamonds_by_color <- group_by(diamonds, color)
diamonds_mp_by_color <- summarise(diamonds_by_color, mean_price = mean(price))


library(gridExtra)
p1<-ggplot(aes(x=clarity,y=mean_price),data=diamonds_mp_by_clarity)+
  geom_bar(stat = "identity")
p2<-ggplot(aes(x=color,y=mean_price),data=diamonds_mp_by_color)+
geom_bar(stat = "identity")
grid.arrange(p1,p2,ncol=1)
```


