请使用聚合查询回答以下问题。

我们的城市集合中最常用的城市名称是什么？

你一开始可能会发现 None 是最常出现的城市名称。实际上表示很多城市根本没有名称字段。很奇怪此集合中会出现此类文档，根据你的具体情况，你可能需要进一步清理数据。

要立即解答此问题，我们应该忽略没有指定名称的城市。提示下，可以思考哪个管道运算符使我们能够简化过滤器输入？我们如何测试某个字段是否存在？

只需修改“make_pipeline”函数，使其创建并返回一个聚合管道，该管道可以传递到 MongoDB 聚合函数中。和这节课中的示例一样，聚合管道应该是一个包含一个或多个字典对象的列表。如果不熟悉语法，请参阅这节课中的示例。

你的代码将根据我们提供的 MongoDB 实例运行。如果你想在本地机器上运行代码，你需要安装 MongoDB 并下载和插入数据集。要了解 MongoDB 设置和数据集方面的说明，请参阅课程资料。

请注意，你在此处使用的数据集与课程资料中提供的城市集合版本不同。如果你尝试运行我们在习题集中运行过的同一查询，结果可能不同。