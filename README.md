# flask

## 项目背景介绍

#### 这个项目主要是基于flask的一个博客界面。
#### 区别于jekyll的静态网页，这个网页对后端进行了规划。
#### 利用bootstrap进行了响应式布局与美化

## 安装和运行方式
### 如果在gitpod内运行首先安装flask,
<code> pip install flask </code>

### 创建一个项目文件夹，然后创建一个虚拟环境。创建完成后项目文件夹中会有一个 venv 文件夹：
<code>python3 -m venv venv</code>

### 在bash环境下运行
<code>export FLASK_APP=flaskr</code>
<br></br>
<code>export FLASK_ENV=development</code>
<br></br>
<code> flask init-db </code>

### 由于Gitpod做了NAT，所以你得指定监听地址是 0.0.0.0
<code>flask run -h 0.0.0.0</code>

## Maintainers
#### @Happy-orange-juice

## Contributors
#### @895201599 
#### @vincentwoody

## License
#### MIT © Richard Littauer
