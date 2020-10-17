# Step 12 Report

###### 刘泓尊　2018011446　计84

## 实验目的

	1. 支持数组的声明和数组/指针下标操作
 	2. 支持指针算术运算

## 实验过程

  1. 增加文法，支持指针声明

     ```
     declaration
         : tp Identifier ('[' Integer ']')* ('=' expr)? ';'
         ;
     ```

  2. 名称解析

     需要在名称解析阶段判断数组长度是否<0或者过大．同时需要在`Variable`中维护变量的大小，因为此时变量不再只是4 byte大小．

  3. 类型检查

     增加了数组类型`OneDimArrayType`和`ArrayType`，其中`ArrayType`是`OneDimArrayType`的包装类，本质上还是`OneDimArrayType`．数组大小是所有维度大小相乘再乘4．

     对于数组下标操作，只需要返回该节点类型的基类型．

     对于指针算术，指针加减`int`得到指针类型，指针减指针得到int类型．

  4. IR生成

     主要增加了对指针算术运算和下标操作的支持．

     对于指针算术运算，`int +int*`类型为:

     ```
     left ir
     const size
     mul
     right ir
     add
     ```

     对于`int* +- int`类型为：

     ```
     left ir
     right ir
     const size
     mul
     add/sub
     ```

     对于`int*  - int*`类型

     ```
     left ir
     right ir
     sub
     const size
     div
     ```

     对于下标操作`postfix '[' expr ']'` 

     ```
     postfix ir
     expr ir
     const size
     mul
     add
     ```

     如果结果不是左值（比如是数组类型），还需要在最后加上`load`指令

     ```
     ...
     load
     ```

## 思考题

1. #### 请分别给出每个函数的返回值（局部变量 `a` 的起始地址都是 `0x1000`(4096), 用一个常量 minidecaf 表达式表示，例如函数 `A` 的返回值是 `*(int*)(4096 + 23 * 4)`

   ```c
   int A() {
       int a[100];
       return a[23];
   }
   
   int B() {
       int *p = (int*) 4096;
       return p[23];
   }
   
   int C() {
       int a[10][10];
       return a[2][3];
   }
   
   int D() {
       int *a[10];
       return a[2][3];
   }
   
   int E() {
       int **p = (int**) 4096;
       return p[2][3];
   }
   ```

   Ａ：`*(int*)(4096+23*4)`

   ```
   	frameaddr -400
       pushi 23
       pushi 4
       mul
       add
       load
   ```

   Ｂ：`*(int*)(4096+23*4)`

   ```
   	pushi 4096
       frameaddr -4
       load
       pushi 23
       pushi 4
       mul
       add
       load
   ```

   Ｃ：`**(int**)(4096 + 2*40 + 3*4)`

   ```
   	frameaddr -400
       pushi 2
       pushi 40
       mul
       add
       pushi 3
       pushi 4
       mul
       add
       load
   ```

   Ｄ：`*((*((int*)*)(4096+2*4))+3*4)`

   ```
   	frameaddr -40
       pushi 2
       pushi 4
       mul
       add
       load
       pushi 3
       pushi 4
       mul
       add
       load
   ```

   Ｅ：`*((*(int**)(4096+2*4))+3*4)`

   ```
   	pushi 4096
       frameaddr -4
       load
       pushi 2
       pushi 4
       mul
       add
       load
       pushi 3
       pushi 4
       mul
       add
       load
   ```

2. #### 如果我们决定支持"一维"的可变长度的数组(即允许类似 `int n = 5; int a[n];` 这种，但仍然不允许类似 `int n = ...; int m = ...; int a[n][m];` 这种)，而且要求数组仍然保存在栈上（即不允许用堆上的动态内存申请，如`malloc`等来实现它），应该在现有的实现基础上做出那些改动？

   因为栈空间的分配不能在编译期决定，所以无法在进入函数时便分配内存，而是运行到这一条指令时分配内存，在其生命期结束时释放内存．

   然后在运行时计算`n`（即数组声明中的表达式）的值，存入寄存器（比如`t0`），然后使用`sub sp, sp, t0`为其分配栈帧．
   
   如果同时存在多个可变长度数组，因为这些数组不定，所以每个数组的大小也需要存放在栈上（比如放在每个数组起始地址前4个byte），并用寄存器或栈维护第一个变长数组的起始地址（也就是`frameaddr`要支持变长）．这样`sp`通过加减数组大小，即可实现对不同数组起始地址的跳转（类似链表的跳转）．
   
   在离开作用域的时候，找到对应数组的大小，通过sp加对应大小，即可释放内存．
   
   针对现有的实现，需要在IR生成阶段针对变长数组生成特殊的指令序列，顺序大致如下:
   
   ```
   # 变长数组声明
   expr ir
   pop t1
   push 0 for t1 times
   push t1
   
   # 对第一个变长数组的调用
   frameaddr addr # 第一个数组的起始地址
   push offset
   add  #计算出元素的栈上地址
   load　#　将元素值放在栈顶
   
   # 对第二个变长数组的调用
   frameaddr addr+4  #第一个数组的大小的地址
   load
   push addr #　第一个数组起始地址压栈
   add 		#　栈顶就是第二个数组的起始地址，类似链表的跳转
   push offset
   add
   load   #　将访问的第二个数组的元素放在栈顶
   ```

## Honor Code

​	本节虽然支持的功能繁琐，但是难度较低，仅仅是对上一节的扩充，根据实验指导书即可实现．

