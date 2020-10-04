# Step 4 Report

###### 刘泓尊　2018011446　计84

### 实验目的

1. 支持比较大小和相等的二元操作
2. 支持逻辑与，逻辑非

### 实验过程

1. ##### 修改上下文无关文法，实现新的二元运算符和优先级

   新增的二元运算在优先级约束下可以编写下列上下文无关文法：

   ```
   expr: logicalOr;
   
   logicalOr
       : logicalAnd                    # SingleOr
       | logicalOr '||' logicalAnd     # ComplexOr
       ;
   
   logicalAnd
       : equality                    # SingleAnd
       | logicalAnd '&&' equality        # ComplexAnd
       ;
   
   equality
       : relational                    # SingleEq
       | equality eqOperator relational # ComplexEq
       ;
   
   relational
       : additive                      # SingleRe
       | relational relOperator additive  # ComplexRe
       ;
   ```

   对应的词法为：

   ```
   eqOperator
       : '==' | '!='
       ;
   
   relOperator
       : '<' | '>' | '<=' | '>='
       ; 
   ```

2. ##### 修改Ir生成的Visitor，支持对应的二元操作

   和Step3区别不大，只需要支持对应二元操作节点的访问即可．每个二元操作节点都要先访问两个子节点，计算出子表达式的值，之后将对应的IR压入栈中．

3. ##### 完成IR到Asm的翻译

   不同二元运算IR对应的RISC-V汇编如下：

   ```assembly
   eq:
   	lw t1, 4(sp)
   	lw t2, 0(sp)
   	sub t1, t1, t2
   	seqz t1, t1
   	addi sp, sp, 4
   	sw t1, 0(sp)
   ne:
   	lw t1, 4(sp)
   	lw t2, 0(sp)
   	sub t1, t1, t2
   	snez t1, t1
   	addi sp, sp, 4
   	sw t1, 0(sp)
   le:
   	lw t1, 4(sp)
   	lw t2, 0(sp)
   	sgt t1, t1, t2
   	seqz t1, t1
   	addi sp, sp, 4
   	sw t1, 0(sp)
   ge:
   	lw t1, 4(sp)
   	lw t2, 0(sp)
   	slt t1, t1, t2
   	seqz t1, t1 
   	addi sp, sp, 4
   	sw t1, 0(sp)
   lt:
   	lw t1, 4(sp)
   	lw t2, 0(sp)
   	slt t1, t1, t2
   	addi sp, sp, 4
   	sw t1, 0(sp)
   gt:
   	lw t1, 4(sp)
   	lw t2, 0(sp)
   	sgt t1, t1, t2
   	addi sp, sp, 4
   	sw t1, 0(sp)
   lor:
   	lw t1, 4(sp)
   	lw t2, 0(sp)
   	or t1, t1, t2
   	snez t1, t1
   	sw t1, 0(sp)
   land:
   	lw t1, 4(sp)
   	lw t2, 0(sp)
   	snez t1, t1
   	snez t2, t2
   	and t1, t1, t2
   	sw t1, 0(sp)
   ```

   

### 思考题

1. ##### 在表达式计算时，对于某一步运算，是否一定要先计算出所有的操作数的结果才能进行运算？

   不需要，比如对于逻辑与`&&`，当计算出左侧操作数为0时，整个表达式的结果必然为0．

   对于逻辑或`||`，当计算出左侧操作数为1时，整个表达式的结果必然为1．

   以上特性是＂短路求值＂，也就是说，不需要计算出所有操作数的结果再计算．

2. ##### 在 MiniDecaf 中，我们对于短路求值未做要求，但在包括 C 语言的大多数流行的语言中，短路求值都是被支持的。为何这一特性广受欢迎？你认为短路求值这一特性会给程序员带来怎样的好处？

   短路求值有时会带来潜在的性能提升．比如如果逻辑运算表达式两侧的计算比较复杂，尤其是右侧表达式计算很复杂，那么短路求值在某些情况下可以不计算右侧表达式的值．因此这一特性广受欢迎．

   这一特性可以允许程序员将复杂表达式放在逻辑运算符右侧，从而期望带来潜在的性能提升．

### Honor Code

​	本节与Step3很相似，也较为简单，没有参考样例代码．

