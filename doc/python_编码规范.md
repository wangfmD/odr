# Python代码规范   
适用于odr，Python自动化项目
## 编码  
-如无特殊情况, 文件一律使用 UTF-8 编码
如无特殊情况, 文件头部必须加入#-*-coding:utf-8-*-标识
## 空行
- 模块级函数和类定义之间空两行；
- 类成员函数之间空一行；

## 命名规范
### 模块   

- 模块尽量使用小写命名，首字母保持小写，尽量不要用下划线(除非多个单词，且数量不多的情况)  

	```
	# 正确的模块名
	import decoder
	import html_parser
	 
	# 不推荐的模块名
	import Decoder
	```
	
### 类名.   
- 类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头.  

	```
	class Farm():
	    pass
	 
	class AnimalFarm(Farm):
	    pass
	 
	class _PrivateFarm(Farm):
		pass
	```

### 函数. 
- 函数名一律小写，如有多个单词，用下划线隔开. 

	```
	def run():
	    pass
	 
	def run_with_env():
	    pass
	```
- 私有函数在函数前加一个下划线_. 

	```
	class Person():
 
    def _private_func():
        pass
	```  
- 校验方法以verification_xxx起头。


### 变量名. 

- 变量名尽量小写, 如有多个单词，用下划线隔开

	```
	if __name__ == '__main__':
   		count = 0
    	school_name = ''
	```
- 常量采用全大写，如有多个单词，使用下划线隔开
	
	```
	MAX_CLIENT = 100
	MAX_CONNECTION = 1000
	CONNECTION_TIMEOUT = 600
	```


### 常量. 

- 常量使用以下划线分隔的大写命名

	```
	MAX_OVERFLOW = 100
	 
	Class FooBar:
	 
	    def foo_bar(self, print_):
	        print(print_)
	```