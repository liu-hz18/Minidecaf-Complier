# Step 10 Report

###### 刘泓尊　2018011446　计84

## 实验目的

​	1. 增加全局变量

## 实验过程

  1. #### 修改文法，支持全局变量

     ```
     program: globalDeclare+ EOF;
     
     globalDeclare
         : func          # funcGlobalDeclare
         | declaration   # symbolGlobalDeclare
         ;
     ```

  2. #### 名称解析

     在`NameInfo`类中添加字段`globals`来维护全局变量的信息．

     在名称解析阶段遍历AST，遇到`symbolGlobalDeclare`节点时，检查是否存在全局变量重定义，是否存在全局变量和函数名的冲突．无误则创建全局变量，保存它的名称，初始值和大小．如果之前存在声明，则用定义的值去覆盖该变量的值．

     同时还需要保证初始值只能是整数字面量，所以判断这个`expr`节点的具体类型，要求它必须是整数常量，并且获取常量值。

  3. #### IR生成

     增加IR指令`IrGlobalAddr`，用于声明一个全局变量标志．

     在IR生成阶段，遇到变量使用或者赋值节点时，判断该变量是局部变量还是全局变量(通过检测是否有`offset`字段即可)，来决定生成`IrFrameAddr`还是`IrGlobalAddr`．

  4. #### 汇编生成

     汇编可以直接用 `la` 加载全局变量地址，对于IR指令`globaladdr SYMBOL`，可以翻译为

     ```assembly
     	addi sp, sp, -4
     	la t1, SYMBOL
     	sw t1, 0(sp)
     ```

     在汇编代码生成最开始的地方进行全局变量的汇编生成．先在`.data`段完成对有定义的全局变量的初始化，之后在`.bss`段完成对只有声明的全局变量的初始化．

     全局变量定义的汇编代码为

     ```assembly
     	# global symbol definition.
     	.data
     	.align 4
     	.globl a
     	.size a, 4
     ```

     全局变量声明的汇编代码为

     ```assembly
     	# global symbol declaration.
     	.bss
     	.comm b, 4, 4
     ```

## 思考题

 1. #### 请给出将全局变量 `a` 的值读到寄存器 `t0` 所需的 riscv 指令序列.

    ```assembly
    la t1, a      # 加载全局变量地址到t1
    lw t0, 0(t1)  # 将地址t1的内容放到t0
    ```

## Honor Code

​	Step10比较简单, 增加了1个IR指令和1个汇编指令，并进行了相应检查，参照实验指导书即可实现．