## Baseball project for data visualization
### Introduction of the dataset 
#### This dataset includes 1157 baseball players with five attributes, handness(left hand or right hand), height, weight , avg and score

### Visualization Design 
##### I want to focus on the avg, and figure out which kind of players perform better in competition, thus I plot height, weight as x,y, 
##### and I use the size of the circle to indicate the avg, the bigger the cicle, the higher the avg.

##### After I plot all the points, I find out that all the points overlap together, I want to figure out a good solution to avoid overlapping, however I change my mind, I want to design some filters using the handness, thus I divide the data set into three subsets, the subsets is small enough to see each point clearly and can identify the different size. Also, I made another improvement, I add the exact number of different groups, since sometimes users want to figure out which group has the largest number which can not achieved through the scatterplot.

### Feadback
##### Advice1
```
" There are too many points to see it clearly "
```
##### 我在legend上面添加了方法，允许用户对不同的组别进行进一步的分析，这样子点会少一些会更容易看清楚
##### Advice2
```
可视化可以成功加载，并且包含有悬浮框，可以提供一定的交互功能。对代码块给出了注释，解释清楚。代码的格式性不错。

可视化的中心具体明确，尝试来说明身高、体重、handedness与棒球选手得分的关系。

可视化在传递发现上面并不够清楚，从你的可视化中我无法看出数据中的趋势以及你要传递的发现。你可以尝试添加几个按钮，可以查看不同handedness对应的点的情况，这样不同组别之间的差异会更加一目了然一些。

不同的颜色对应的handedness没有进行说明。点的大小的含义也并没有进行说明。

点的重叠现象还是稍微有一些严重，你可以尝试在x轴这一变量上添加jitter（可以使用一定范围内的随机数）将数据在一定的程度上分散开。

你并没有说明你从可视化中发现的观点和关系，请进行一下说明。本项目的目标是传递一个有意义的发现，而不是仅仅对数据进行可视化。

一般来说我们可以先对数据进行探索，可以使用R或python等其他的工具找到一个或几个有趣的关系，然后再尝试用dimple.js/d3等互动性的可视化来向读者展示。

你并没有收集足够多的反馈意见，请尝试将你的可视化发送给你的朋友、家人、或者学习同一门课程的同学。不同的人可能有不同的观察侧重点，可能会给出你更多的帮助。

请尝试对可视化根据上面的反馈进行改进，并且同时上传改进前和改进之后的多个版本。如果没有采纳读者的反馈建议，也对没有采纳的原因进行一下解释。
```
##### improvement

##### 1.由于之前没有找到D3的jitter function，我采取了建议并转换了一下思路，使用了一个math.random()使它jitter。

2.其实我是有button的，我直接用了legend作为button，帮助用户对于不同的组别进行过滤。如果mouseover和mouseout会选择出相应的组别；点的大小我有做说明，并进行了一些调整，用了（avg*10）^2 所以这样子点的差异会更明显一些，点越大表示用户的击球率越高。还有一个信息是用户的总分信息，我是放在了tooltip里面

3.在最开始的时候我是用R做了一些分析，发现其实体重和身高是有对应关系的，二者是正比的关系，对于不同的组别，可以看到both组的明显人数较少，但是三组都有一个
共同的特点就是一般来说，击球率较高的广泛的分布在中等的体重范围，基本上在70以上，但是总有那么几名优秀的outlier
##### Advice3
```
" I can not tell which group has the largest number of players, if you give me a number, I feel better "
```
##### 我在svg的上方添加了一个text，当用户对不同组别进行选择的时候，text中会显示具体的数字，当用户没有选择的时候，就显示总计的数值
### Resource
##### I use an example from the d3js offical website, here is the link :https://bl.ocks.org/mbostock/3887118
