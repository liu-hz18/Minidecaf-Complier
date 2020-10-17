# Step 5 Report

###### 刘泓尊　2018011446　计84

## 实验目的

1.　增加变量，实现变量的声明和使用
2.　熟悉栈帧的概念，并利用它实现变量功能

## 实验过程

 1. #### 修改文法，增加变量的声明，赋值．

    增加了词法Identifier，具体定义如下：

    ```antlr4
    fragment IdentLead : [a-zA-Z_];
    Identifier : IdentLead WordChar* ;
    ```

    增加了变量声明和赋值的语句，同时在基本表达式中增加变量（即变量的使用）

    ```antlr4
    statement
        : 'return' expr ';'   # RetStatement
        | expr? ';'           # ExprStatement
        | declaration         # DeclareStatement
        ;
    declaration
        : tp Identifier ('=' expr)? ';'　//变量声明
        ;
    expr: assignment;
    assignment
        : logicalOr                     # SingleAssign
        | Identifier '=' expr           # ComplexAssign　//变量赋值
        ;
    .......
    primary
        : Integer       # atomInteger
        | '(' expr ')'  # ComplexPrimary
        | Identifier    # atomIdentifier //变量的使用
        ;
    ```

    

 2. #### 增加 IR 指令，加入访问物理栈的`load/store`，以及生成栈上地址的`frameaddr`，还增加了弹栈指令`pop`

    本节需要修改的代码较多，主要是参考样例代码引入了多遍遍历，从而实现对变量的检查，包括变量的声明，使用和与函数挂钩的作用域．

    为了支持变量，我引入了类`Variable`，用以统计变量的名称，大小和栈上的偏移．设计了一个全局的计数器，用以区分不同作用域的同名变量．

    为了支持变量和作用域挂钩，我增加了`FuncNameInfo`类，统计当前函数作用域中的变量，同时进行重定义检查．

    同时设计了`NameInfo`类统计所有的变量名和函数名，为后面的名称检查做准备．

    接下来便进行针对变量的遍历，即实现`NameVisitor`类．遍历到函数声明时，会在`NameInfo`注册该函数；遇到函数定义时，会切换作用域，通过`enterScope`和`exitScope`模拟函数调用的压栈和弹栈操作．遇到作用域内的变量声明时，将物理栈大小增加，同时注册该变量的大小和栈上偏移，同时进行重定义检查；遇到作用域内的变量调用时，会检查作用域内是否有该变量，并注册该变量的使用地址，为IR生成做准备．

    IR指令类新增了`IrPop`，`IrLoad`，`IrStore`，`IrFrameAddr`以支持变量的声明和使用; 增加了`IrFunction`来实现函数栈帧的建立和销毁．

    名称检查完成后，将名称信息传递给IR生成的`Visitor`．在遇到函数声明时，其实不对应任何IR;　在函数定义时，会向IR栈压入`IrFunction`，包括函数栈帧的信息和该作用域内新建的变量．遇到变量声明时，向IR栈压入对应大小的栈空间(如果有初始化则初始化); 遇到变量赋值时，需要获得栈上地址`IrFrameAddr`，同时进行存储`IrStore`；遇到变量调用时，需要获得栈上地址`IrFrameAddr`，同时获得它的值`IrLoad`．

 3. #### 增加ＩＲ对应的汇编指令,　支持函数默认返回0

    上述新增的ＩＲ指令对应的汇编指令如下：

    ```assembly
    load:
    	lw t1, 0(sp)
    	lw t1, 0(t1)
    	sw t1, 0(sp)
    store:
    	lw t1, 4(sp)
    	lw t2, 0(sp)
    	addi sp, sp, 4
    	sw sp, sp, 4
    frameaddr k:
    	addi sp, sp, -4
    	addi t1, fp, -12-4*k
    	sw t1, 0(sp)
    pop:
    	addi sp, sp, 4
    ```

    同时由于栈帧是和函数相关的，需要修改每个函数进入和返回时的汇编行为，即生成 `prologue` 和 `epilogue`．在我的实现中，我将该函数相关的指令全部用`IrFunction`维护，遇到`IrFunction`时，先建立栈帧，然后生成该函数的指令，最后销毁栈帧．

    建立栈帧的过程大致如下:

    ```assembly
    	.text
    	.globl <func name>
    <func name>:
    	# 保存ra和fp
    	addi sp, sp, -4
    	sw ra, 0(sp)
    	addi sp, sp, -4
    	sw fp, 0(sp)
    	# 建立fp
    	mv fp, sp
    	# 建立参数空间
    	lw t1, offset(fp)
    	addi sp, sp, -4
    	sw t1, 0(sp)
    	...
    ```

    销毁栈帧的过程大致如下：

    ```assembly
    	#　为了默认返回0，在这里压入0即可
    	addi sp, sp, -4
    	li t1, 0
    	sw t1, 0(sp)
    <func name>_exit:
    	lw a0, 0(sp)
    	mv sp, fp
    	lw fp, 0(sp)
    	addi sp, sp, 4
    	lw ra, 0(sp)
    	addi sp, sp, 4
    	jr ra
    ```

## 思考题

 1. #### 描述程序运行过程中函数栈帧的构成，分成哪几个部分？每个部分所用空间最少是多少？

    从栈底到栈顶，依次为：返回地址，旧栈帧`fp`，参数栈，局部变量栈．对于本实验来讲，其实还有表达式运算栈．

    其中，返回地址占用4 byte; 旧栈帧`fp`占用4 byte；参数栈如果没有参数则为0；局部变量栈如果没有局部变量则大小为0；

    所以汇编栈帧的大小等于`8 + 4*(局部变量个数＋参数个数),` 其中`4 == sizeof(int)`，栈帧最小为8byte.

    汇编栈帧底部还保存了 `fp` 和返回地址，使得函数执行完成后能够返回 `caller` 继续执行，访问变量也可以直接用 `fp` 加上偏移量来完成。 

 2. #### 有些语言允许在同一个作用域中多次定义同名的变量，例如这是一段合法的 Rust 代码（你不需要精确了解它的含义，大致理解即可）：

    ```rust
    fn main() {
      let a = 0;
      let a = f(a);
      let a = g(a);
    }
    ```

    其中`f(a)`中的`a`是上一行的`let a = 0;`定义的，`g(a)`中的`a`是上一行的`let a = f(a);`。

    #### 如果 MiniDecaf 也允许多次定义同名变量，并规定新的定义会覆盖之前的同名定义，请问在你的实现中，需要对定义变量和查找变量的逻辑做怎样的修改？

    这种操作实际上称为重影(Shadowing)．

    对于单遍遍历而言比较简单：

    在定义变量时不再进行重定义检查，而是针对同名变量维护一个变量栈，遇到同名声明则压入对应的栈，这样就可以让后面的定义覆盖前面的定义．需要注意的是，这些变量的栈上地址是相同的．

    在查找变量时，只需要取出该变量栈中栈顶变量即可．

    对于多遍遍历，一种可能的方案是，在名称遍历阶段赋予同名变量不同的名字（比如后缀一个计数器），但是它们的栈上地址是相同的，并维护当前`a`的实际别名．在使用变量时，将该变量视作当前a的实际别名，并查找已声明变量中有没有此变量即可．（可以理解微对源代码的变量名进行了替换，但是均使用同一个地址）．

## Honor Code

​	Step5需要增加的代码较多，其中`NameInfo`类参考了样例代码的实现．