# iMovies

[![GitHub license](https://img.shields.io/github/license/Co1lin/iMovies?style=flat-square)](https://github.com/Co1lin/iMovies/blob/master/LICENSE)   [![CodeFactor](https://www.codefactor.io/repository/github/co1lin/imovies/badge/master?style=flat-square)](https://www.codefactor.io/repository/github/co1lin/imovies/overview/master?style=flat-square)  [![GitHub stars](https://img.shields.io/github/stars/Co1lin/iMovies?style=flat-square)](https://github.com/Co1lin/iMovies/stargazers)  [![GitHub forks](https://img.shields.io/github/forks/Co1lin/iMovies?style=flat-square)](https://github.com/Co1lin/iMovies/network)  

A movie information site, the assignment for Web Development Course, in Summer Term 2020.

https://github.com/Co1lin/iMovies

## Demo

https://movies.enjoycolin.top/

本项目已借助 uwcgi + NGINX 部署至服务器。各项功能均可通过上述链接访问网站进行体验。

### 相关数据

以下数据均可在网页的相应位置看到。

电影：1165条

演员：7271条

影评：5825条

搜索时间：无论搜索内容如何，在本人尝试中搜索时间均不到0.001秒，一般在0.0005~0.0007秒之间。

## Implementation

本项目主要分为两个部分：数据爬取与网站搭建。

### 数据爬取

本部分的内容存放在Crawlers中。

在爬取网页过程中，为了应对反爬机制，需要为request增加一些通过浏览器访问豆瓣获取的header随机使用，其中cookie属性很重要。同时，为了避免“秒封IP”，需要在每次爬取之间休眠一点时间。

一下是爬取数据的各步操作。

#### 获取电影表单

访问豆瓣电影分类排行榜：
`https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=`
打开Chrome的Inspect-Network界面，筛选XHR类型，发现以下请求链接：
`https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=1`
将结尾的`limit`改为较大数值，请求该链接，即可获得一份包含了排行榜上电影的简单信息的JSON。
在不同的排行榜页面采取同样的操作，获得一千多条电影信息，存入`index.json`。（它是由`/data/index`文件夹下的文件合并而成的。）

#### 整理电影信息

为了方便后续的前端显示，对`index.json`做简单处理，包括修改电影名称中的特殊字符。用`movie_index.py`完成，存入`movie_index.json`。

#### 爬取电影详情页面

根据刚刚得到的json文件中每个电影的url值，用request方法获取电影详情页的HTML。由于每部电影的演员列表的页面与该页面的链接存在简单的关系，因此顺便也将该页面爬取下来。他们存放在`/data/subjects`中。每部电影对应两个HTML：`xxx.html`与`xxx-celebrites.html`。用`movie page and its celebrity list page.py`完成。

#### 分析电影详情页面以及演员列表页面

利用上一步获得的两种HTML，借助`lxml`库正则表达式，分析电影详情页面的各个内容，以及演员列表页面中含有的每个演员对应的演员详情页。用`parse_movie.py`完成，存入`complete_info.json`文件。

#### 爬取演员详情页面并分析

读取`complete_info.json`，爬取里面每个演员对应的详情页并存储HTML到`/data/celebrities`。用`celebrity page.py`完成。

然后用`parse_actor.py`仿照上面分析电影详情页的方法分析演员详情页，将结果存入`actor_info.json`。

### 网站搭建

#### 后端

利用Miniconda创建 Python3.8 ，Django3环境。

使用Django默认的sqlite数据库。通过编写`models.py`创建数据库，用于存储电影、演员、评论，以及他们之间的关系。

##### 数据导入

利用之前整理出的`complete_info.json`和`actor_info.json`，编写`build_models.py`脚本，将json中的数据导入数据库。

#### 前端

采用Bootstrap框架进行美化与响应式设计，使页面在不同设备不同屏幕尺寸下均有较为良好的视觉与使用体验。

设计过程大致为：利用Bootstrap studio选择合适的“对象”，Copy框架至PyCharm进行修改，借助Chrome预览微调各项CSS。

为减少代码重复，利用Django模板语言中的extends以及include，引用写有相同部分内容的HTML（在`templates/commons/`中）。

#### 各功能以及实现方式

后端数据传送到前端均采用后端传QuerySet到前端Django的模板语言，以下不再赘述。

##### 列表页

影视列表页，即主页，后端在`views.py`中继承Django的模型视图ListView编写视图类IndexView，指定model为数据库中的Movie，页面为`index.html`。

演员列表页、评论列表页同理。

前端使用Bootstrap中灵活性较强的“Card”，以卡片方式呈现每条影视与演员信息。评论页面采用表格呈现。

#### 影视信息页与演员信息页

影视信息页从上到下依次为：

海报、基本信息表格、简介、主要演员、评论。

基本信息表格中为了应对某些电影某项数据缺失的问题，在前端利用Django模板语言进行判断，如果没有就不显示。

主要演员是一个可以横向滑动的表格，内部用Card存储演员海报及其名字。

评论为纵向滑动的表格。

演员信息页同理。

#### 搜索

利用HTML的form（表单）组合一个文本输入框和一个包含三个选项的单选组，指定相应的action，结合后端`urls.py`以及`views.py`中处理搜索跳转连接以及搜索视图的方法，其中调用数据库的filter方法进行筛选、Q函数进行不同字段的组合，来完成搜索功能。

在数据库查询前后利用datetime库中的方法记录时间，作差得到微妙级别的搜索计时结果，并利用Django模板语言传给前端呈现。

#### 分页

后端利用开源项目`pure_pagination`进行适当修改，前端编写`pagination.html`呈现随情况变化的“分页条”。

分页条下部放有页面快速跳转输入框，在前端用JavaScript相应键盘事件实现。

