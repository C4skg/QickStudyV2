from . import article

from flask import jsonify

@article.route('/getdata')
def getData():
	context = """
# 函数的间断点

> 本节需要在函数的连续性基础上学习

## 间断点定义

由函数的连续性，若 $f(x)$ 在 $x=x_0$ 处连续，那么
$$
\lim\limits_{x \to x^-_0}{f(x)} = \lim\limits_{x \to x^+_0}{f(x)} = f(x_0)
$$
在此基础上，如果函数 $f(x)$ 有下列三种情况之一：

1. $f(x_0)$ 不存在，即 $x_0$ 没有定义
2. 虽然 $x_0$ 有定义且 $\lim\limits_{x \to x_0}{f(x)}$ 存在，但 $\lim\limits_{x \to x_0}{f(x)} \neq f(x_0)$
3. 虽然 $x_0$ 有定义，但 $\lim\limits_{x \to x_0}{f(x)}$ 不存在(三种情况)

$$
\lim\limits_{x \to x_0}{f(x)} = \begin{cases}
	\lim\limits_{x \to x^-_0}{f(x)} \neq \lim\limits_{x \to x^+_0}{f(x)}\\
	\lim\limits_{x \to x^-_0}{f(x)} {或} \lim\limits_{x \to x^+_0}{f(x)} {为} \infin \\
	\lim\limits_{x \to x^-_0}{f(x)} {或} \lim\limits_{x \to x^+_0}{f(x)} {值不唯一}
\end{cases}
$$

那么称函数 $f(x)$ 在点 $x_0$ 不连续，而点 $x_0$ 称为函数 $f(x)$ 的 `不连续点` 或 `间断点`



## 间断点的分类

### 第一类间断点

左右极限都存在的间断点

#### 可去间断点

左极限 = 右极限 但不等于函数值

(包括函数值不存在，极限值存在的情况)，即
$$
\lim\limits_{x \to x^-_0}{f(x)} = \lim\limits_{x \to x^+_0}{f(x)} = A \neq f(x_0)
$$
则 $x=x_0$ 为 $f(x)$ 的可去间断点



#### 跳跃间断点

左极限值 != 右极限值，即
$$
\lim\limits_{x \to x^-_0}{f(x)} = A {,}
\lim\limits_{x \to x^+_0}{f(x)} = B {,}
A \neq B
$$
则 $x=x_0$ 为 $f(x)$ 的跳跃间断点 

### 第二类间断点

$f(x)$ 在 $x_0$ 的左、右极限中 `至少`有一个不存在的间断点

#### 无穷间断点

至少满足 $\lim\limits_{x \to x^-_0}{f(x)} = \infin$ 或 $\lim\limits_{x \to x^+_0}{f(x)} = \infin$ 

那么 $x = x_0$ 是该函数的无穷间断点

#### 振荡间断点

至少满足  $\lim\limits_{x \to x^-_0}{f(x)}$ 或 $\lim\limits_{x \to x^+_0}{f(x)}$ 中至少有一个值不趋向于唯一常数

即函数值有多个值（介于某个数之间）时，极限不存在

那么 $x = x_0$ 是该函数的振荡间断点


## 间断点可能出现的位置

1. 函数的无定义点处
2. 分段函数的分段点处

""";
	return jsonify({
        "context": context
	});