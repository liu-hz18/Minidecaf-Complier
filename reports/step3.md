# Step3 Report

###### 刘泓尊　2018011446　计84

### 实验目的

1. 支持对`+, -, *, /, %`的二元运算．支持结合性`()`

### 实验过程

1. ##### 修改上下文无关文法，支持二元运算以及优先级和结合性

   增加了二元运算的词法，为了保证优先级，将二元运算分为2类：

   ```
   // bi-op
   addOperator
       : '+' | '-'
       ;
   mulOperator
       : '*' | '/' | '%'
       ;
   ```

   增加了对二元运算的语法支持，同时保证了优先级和结合性：

   ```
   expr
       : additive
   
   additive
       : multiplicative                        # SingleAdd
       | additive addOperator multiplicative   # ComplexAdd
       ;
   
   multiplicative
       : unary                                 # SingleMul
       | multiplicative mulOperator unary      # ComplexMul
       ;
   
   unary
       : primary             # SingleUnary
       | unOperator unary    # ComplexUnary
       ;
   
   primary
       : Integer       # atomInteger
       | '(' expr ')'  # ComplexPrimary
       ;
   ```

   

2. ##### 增加Visitor对新增节点的访问处理，增加二元运算的Ir类

   增加了ＩＲ类IrBinary，代表一个二元运算．

   对于每一种二元运算，我抽象出了一个通用函数`_visitBinary(self, op, ctx)`，其余二元运算节点只需要解析运算符后访问该节点即可．

   对于每一个二元运算节点，先解析其孩子节点，即获得子表达式的值，运算符的优先级也由这一步保证．之后，获得本节点运算符类型，如`op = str(ctx.addOperator().getText())`，然后调用`self._visitBinary(op, ctx)`即可将对应的ＩＲ压入ＩＲ指令栈．

   `ComplexPrimary`节点暂时只需要访问其孩子，其余什么都不做．

3. ##### 完成IR到Asm的翻译过程

   按照实验指导书的规范，二元运算是首先将左右操作数压栈，之后取出值，并将计算结果压栈．完成后栈大小加1，栈顶就是二元操作的结果．

   对应的汇编指令如下：

   ```
   add:
   	add lw t1, 4(sp)
   	lw t2, 0(sp)
   	add t1, t1, t2
   	addi sp sp, 4
   	sw t1, 0(sp)
   sub:
   	add lw t1, 4(sp)
   	lw t2, 0(sp)
   	sub t1, t1, t2
   	addi sp sp, 4
   	sw t1, 0(sp)
   mul:
   	add lw t1, 4(sp)
   	lw t2, 0(sp)
   	mul t1, t1, t2
   	addi sp sp, 4
   	sw t1, 0(sp)
   div:
   	add lw t1, 4(sp)
   	lw t2, 0(sp)
   	div t1, t1, t2
   	addi sp sp, 4
   	sw t1, 0(sp)
   rem:
   	add lw t1, 4(sp)
   	lw t2, 0(sp)
   	rem t1, t1, t2
   	addi sp sp, 4
   	sw t1, 0(sp)
   ```

   同时在AsmGenerator中加入解析IrBinary(op)的函数即可．

### 思考题

1. ##### 寄存器`t0`的数值压入栈中的汇编序列：

   ```assembly
   addi sp, sp, -4
   sw t0, 0(sp)
   ```

   栈顶的数值弹出到寄存器`t0`的汇编序列：

   ```assembly
   lw t0, 0(sp)
   addi sp, sp, 4
   ```

2. ##### 即使除法的右操作数不是 0，仍然可能存在未定义行为。请问这时除法的左操作数和右操作数分别是什么？

   ```c
   #include <stdio.h>
   
   int main() {
     int a = -2147483648;
     int b = -1;
     printf("%d\n", a / b);
     return 0;
   }
   ```

   x86-64, gcc (Ubuntu 9.3.0-10ubuntu2) 9.3.0下编译运行的结果：

   ```bash
   ➜  gcc -c test.cpp -O0  
   ➜  gcc -o test test.o   
   ➜  ./test             
   [1]    243495 floating point exception (core dumped)  ./test
   ```

   ​	实际对应的汇编指令是`idivl`，当运算溢出时会发生**除法异常**．

   qemu中编译运行的结果：

   ```bash
   ➜  riscv64-unknown-elf-gcc -march=rv32im -mabi=ilp32 -c test.cpp   
   ➜  riscv64-unknown-elf-gcc -march=rv32im -mabi=ilp32 -o test test.o
   ➜  qemu-riscv32 ./test   
   -2147483648
   ```

   ​	实际对应的汇编指令是`div`, 行为是向0舍入，将数据补码写入目标寄存器，不会报错．

   本质上是因为x86汇编和RISC-V汇编的规范不同．

### Honor Code

​	本节任务较为简单，没有参考样例代码．

