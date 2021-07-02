# flask

# 运行方式
## 如果在gitpod内运行首先安装flask,
<code> pip install flask </code>

## 创建一个项目文件夹，然后创建一个虚拟环境。创建完成后项目文件夹中会有一个 venv 文件夹：
<code>python3 -m venv venv</code>

## 在bash环境下运行
<code>export FLASK_APP=flaskr</code>
<code>export FLASK_ENV=development</code>
<code> flask init-db </code>

### 由于Gitpod做了NAT，所以你得指定监听地址是 0.0.0.0
<code>flask run -h 0.0.0.0</code>

## 在powershell环境下运行就在"env:..."前面加上一个$即可