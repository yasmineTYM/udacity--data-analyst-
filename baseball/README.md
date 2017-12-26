## Baseball project for data visualization
### Introduction of the dataset 
#### This dataset includes 1157 baseball players with five attributes, handness(left hand or right hand), height, weight , avg and score

### Visualization Design 
##### I want to focus on the avg, and figure out which kind of players perform better in competition, thus I plot height, weight as x,y, 
##### and I use the size of the circle to indicate the avg, the bigger the cicle, the higher the avg.

##### After I plot all the points, I find out that all the points overlap together, I want to figure out a good solution to avoid overlapping, however I change my mind, I want to design some filters using the handness, thus I divide the data set into three subsets, the subsets is small enough to see each point clearly and can identify the different size. Also, I made another improvement, I add the exact number of different groups, since sometimes users want to figure out which group has the largest number which can not achieved through the scatterplot.

### Feadback
##### I just send it to my boyfriends, and according to his advice, I made two improvement:
```
" There are too many points to see it clearly "

" I can not tell which group has the largest number of players, if you give me a number, I feel better "

##### I am going to submit it and see if tutor give me more advice

### Resource
##### I use an example from the d3js offical website, here is the link :https://bl.ocks.org/mbostock/3887118
