# 基于 PEP8 规范的编码规范说明文档

## 1.目的

1. 为了统一项目的编程规范，降低代码维护成本，提高代码质量。
2. 能够使阅读本项目的人员能方便的理解每个目录、变量、类、方法的意义。
3. 保证一致性、统一性。
4. 用于显著提高代码的可读性，并有助于提高代码版本管理的效率。

## 2.Comments - 代码注释
当代码更改或创建之前，应优先更新对应的注释！注释应该是完整的句子

### Block Comments - 块注释
时候块注释时，应跟随缩进到他们对应的代码的锁进级别，块注释每行开头使用 `# ` 符号（#加一个空格）。

### Inline Comments - 行内注释
行内注释应该节制使用。如果该行代码目的是明确或状态明显的，那么行内注释是不必要的。

### Documentation Strings - 文档字符串
需要为所有的公共模块、函数、类以及方法编写文档说明。非公共方法没有必要，但是应该有一个描述方法具体作用的注释。该注释应在 `def` 函数定义之后
1. 多行文档结尾的引号应自成一行
```python
'''This is a multi-line
documentation string.
'''
```
2. 单行文档结尾的引号应与代码在同一行
```python
'''This is a single-line documentation string.'''
```

## 3.Code Layout - 代码布局

### Indentation - 缩进
代码的缩进应使用 4 个空格。
函数调用换行时，参数应与左括号对齐
```python
my_function(arg1, arg2,
            arg3, arg4)
```
或者使用更多的缩进来明确函数调用
```python
my_function(
    arg1, arg2,
    arg3, arg4)
```

### Blank Lines - 空行
空行中不能有任何空格或制表符。
顶层函数和类的定义前后应用两个空行隔开
类方法定义前后应用一个空行隔开
在函数中使用空行来区分逻辑快，但不要滥用。

### imports - 导入
当导入大模块时，应分行导入
```python
import os
import sys
```
但是如果从同一个模块中导入多个方法，可以同行导入
```python
from os import path, system
```

导入总是位于文件头部，在文件注释之后，在变量之前。
导入顺序应按一下顺序进行导入：
1. 标准库的导入

2. 相关第三方库的导入

3. 本地应用/库特定导入

   应该优先使用绝对路径导入，绝对路径导入能够增加可读性并性能更好（报错时也能够快速定位）

   ```python
   from mypkg import func1,func2
   from mypkg.sub import func
   ```



## 4. Naming Conventions 命名规范

每个文件应该严格遵循整个项目的命名规范进行

但如果有个单独的模块采用了不同的风格，该模块应保持其内部的统一

### 重要原则

暴露给用户或其他模块的 `API` 接口的命名，应遵循使用场景命名，而不是实现的原则。

### Naming Styles - 命名约定

#### Names to avoid - 应避免的命名

尽量不要使用

+  `l` (小写的 `L`)
+ `O`（大写的 `o`） 
+ `I` （大写的 `i`）

#### Package and Module Names - 包和模块的命名

模块应该使用简短全小写的名字，如果为了提升可读性，可以使用下划线

#### Class Names - 类名

类名一般首字母大写

类中内置变量大多是单个或两个单词连在一起，首字母大写或全大写应用于异常量或内部常量

#### Function Names - 函数名

应该全小写，如果想提高可读性可以使用下划线分割，大小写混合仅为了兼容类名

#### Constans - 常量

通常定义在模块级中，全大写字母并通过下划线分割单词，如：`MAX_NUMBER`



## 5. Programming Recommendations - 编程建议

+ 字符串的连接不要使用 `+` 符号，而是使用 `.join()` 方法实现

+ 使用运算符时，符号作用两侧应加上空格

+ 若函数中存在多个逻辑分区，应优先处理异常情况，再处理错误情况

  ```python
  def test_func():
  		if (error1):
        	return ...
      if (error2):
        	return ...
      if (error3):
        	return ...
      # if correct
      return ...
  ```

+ 简短的表达式尽量不要使用 `lambda` 进行，使用单行函数实现

  ```python
  #incorrect
  f = lambda x : x*2
  
  #correct
  def f(x): return x*2;
  ```

+ 在有 `=` 参与的判断语句中，应先写目标值，再写被判断的内容

  ```python
  if 5 == nums
  ```

+ 自定义错误类型时，应从 `Exception` 来继承异常，而不是 `BaseException`

+ 在 `try` 语句中，应只填写必要的代码，而不是全部

  ```python
  try:
    	value = doFunc(key);
  except KeyError:
    	return key_not_found(key);
  else:
  		return handle_value(value);  
  ```

+ 当判断的变量类型为布尔值时，不应该用 `==`

  ```python
  right = True
  if right:
  #而不是
  if right == True:
  #更不是
  if right is True:
  ```

  

  
