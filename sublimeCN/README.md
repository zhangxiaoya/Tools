# sublimeCN

使sublime支持中文输入，修改自[http://www.360doc.com/content/14/1126/15/168576_428234848.shtml](http://www.360doc.com/content/14/1126/15/168576_428234848.shtml)

1. 安装依赖项
	```
	sudo apt-get install build-essential libgtk2.0-dev
	```

2. 编译生成动态链接库
	```
	gcc -shared -o libsublime-imfix.so sublime_imfix.c `pkg-config --libs --cflags gtk+-2.0` -fPIC
	```

3. 拷贝
将生成的libsublime-imfix.so文件拷贝到sublime的安装目录，sublime的安装目录是在`/opt/sublime_text`

4. 修改启动命令
要想使得sublime支持输入中文，就必须加载刚刚生成的动态链接库，可以在在启动的时候，使用命令添加，比如在wsublime的安装目录，执行下面的命令，
```
LD_PRELOAD=./libsublime-imfix.so ./sublime_text
```
这样每次启动的时候都使用绝对路径加载动态链接库，有些麻烦。

平时都是使用subl命令，实质上subl是一个具有执行权限的文本文件，用vim打开并编辑。(用where命令查找subl的绝对路径)
```
sudo vim /usr/bin/subl
```
在执行sublime_text命令之前，添加预加载命令
```
LD_PRELOAD=/opt/sublime_text/libsublime-imfix.so 
```
另外一种方法就是另外以一个脚步，把上面这个命令写入脚本，命名为`sublime`

每次启动sublime，就使用`sublime`命令，取代`subl`

这样在每次输入命令subl命令时就预加载中文输入的动态链接库了。
