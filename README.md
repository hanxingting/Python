# Python项目技术文档之总结说明
姓名：韩星婷

学号：181013015
## URL链接
GitHub代码URL展示链接：[https://github.com/hanxingting/Python/tree/master代码/webapp](https://github.com/hanxingting/Python/tree/master/%E4%BB%A3%E7%A0%81/webapp)

Pythonanywhere的URL展示链接：[http://hanxingting.pythonanywhere.com](http://hanxingting.pythonanywhere.com)

***

## 文档描述
### HTML档描述
* 所有的HTML文件放置在templates文件夹中，results2.html为基模板，展示首页内容。
* static文件夹中添加了css样式，增加了网页背景色与表格的背景色，渲染页面，使页面观看性更高。
### Python档描述
* 由visual_end.py文件运行最终结果。
*  利用flask框架完成Python的web开发，实现前后端的交互。
*  安装并导入pandas、pyecharts等模块，实现数据可视化，展示各样的图表。
*  Flask框架中运用@app.route加入可变参数url，合理的方法get或post展示页面。
### Web App动作描述
* web App主要实现列表循环实现了下拉框对于不同内容的筛选，以及控件和表格图表数据之间的交互。
* 执行 visual_end.py启动服务器。
* Python代码模块和HTML代码块遵循Flask Jinja2规则。

