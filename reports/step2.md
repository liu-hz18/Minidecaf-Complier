# Step2 Report

###### 刘泓尊　2018011446　计84

### 实验目的

1.　支持一元运算`-, ~, !`

### 实验内容

1. ##### 修改上下文无关文法

   ```
   //expr: Integer;  //step1
   expr: unary;
   unary
       : Integer           # atomInteger
       | UnOperator unary  # opAndUnary
       ;
   ```

   同时定义

   ```
   UnOperator: '-' | '~' | '!'　;
   ```

   便实现了对单目运算符的词法和语法支持．

2. ##### 增加Visitor对应的节点访问函数，增加IR指令

   增加了ＩＲ类：IrUnary(op), 用于单目运算符的中间代码生成．

   因为增加了atomInteger和opAndUnary的ＡＳＴ，所以需要重写对应节点的处理函数．

   对于atomInteger，只需要将该整数压栈即可，生成ＩＲ为`IrConst(v)`

   对于opAndUnary，需要在ＩＲ指令栈中压入IrUnary(op).　分为neg, not, lnot. 为后续汇编生成做准备．

3. ##### 增加IR指令到Asm的翻译

   对于IrUnary(op)节点，需要将其翻译成对应的汇编指令，对应关系为：

   ```assembly
   neg:  lw t1, 0(sp)
   	  neg t1, t1
   	  sw t1, 0(sp)
   not:  lw t1, 0(sp)
   	  not t1, t1
   	  sw t1, 0(sp)
   lnot: lw t1, 0(sp)
   	  seqz t1, t1
   	  sw t1, 0(sp)
   ```

   同时在AsmGenerator中实现对IrUnary的支持即可．

### 思考题

越界的表达式：

```
-~2147483647
```

`~2147483647`得到的结果是`-2147483648`，再取负出现越界，得到结果`-2147483648`．

### Honor Code

本节较为简单，没有参考示例代码．

