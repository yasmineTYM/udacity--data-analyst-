In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up.
在此习题集中，你将处理城市 infobox 数据，对数据进行审核，然后想出清理方法并清理数据。

In the previous quiz you recognized that the "name" value can be an array (or
list in Python terms). It would make it easier to process and query the data
later if all values for the name are in a Python list, instead of being
just a string separated with special characters, like now.
在上一道测验中，你意识到“name”值可以是数组（或用 Python 术语来说的话，是列表）。如果名称的所有值是 Python 列表（而不是用特殊字符分隔的字符串，例如现在的状况），则稍后更容易处理和查询数据。

Finish the function fix_name(). It will recieve a string as an input, and it
will return a list of all the names. If there is only one name, the list will
have only one item in it; if the name is "NULL", the list should be empty.
The rest of the code is just an example on how this function can be used.
请完成函数fix_name()。它将获得字符串输入，并返回所有名称列表。如果只有一个名称，列表将只有一项。如果名称是“NULL”，该列表应该为空。代码的其余部分只是可以用来展示如何使用该函数的示例。
