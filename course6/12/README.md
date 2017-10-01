Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in the range as described above,
  write that line to the output_good file
- if the value of the field is not a valid year as described above, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.
你的任务是检查 DBPedia 自动数据文件的“productionStartYear”并获取有效的值。应该完成以下任务：
-    检查字段“productionStartYear”是否包含年份
-    检查该年份是否在 1886 至 2014 范围内
-    将字段值转换为年份（而不是整个日期时间）
-    字段的其他部分和值应该保持不变
-    如果字段的值是如上所述范围内的有效年份，则将该行写入 output_good 文件中
-    如果字段的值不是如上所述的有效年份，则将该行写入 output_bad 文件中
-    你应该采用提供的数据读取和写入方式（DictReader 和 DictWriter），它们将会对标题进行处理。

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
你可以编写辅助函数来检查数据并编写文件，但是我们将仅调用包含三个参数（inputfile、output_good、output_bad）的“process_file”文件。
