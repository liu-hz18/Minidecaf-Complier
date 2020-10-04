# Step1 Report

###### 刘泓尊   2018011446   计84

## 实验目的

1. 配置环境，跑测试
2. 在不同输入上，运行 `minilexer`, `miniparser` 和 `minivisitor`
3. 支持仅一个`return`的`main`函数

## 实验内容

整个过程为：编写上下文无关文法，使用`antlr`生成AST，使用`Visitor`模式遍历AST生成IR，将IR翻译成RISC-V汇编。

1. ##### 编写antlr的上下文无关文法，支持带有return的main函数

   文法参考实验指导书上的设计，即

   ```antlr
   program
       : function
   function
       : type Identifier '(' ')' '{' statement '}'
   type
       : 'int'
   statement
       : 'return' expr ';'
   expr
       : Integer
   ```

   语法符号:

   ```antlr4
   fragment WhitespaceChar : [ \t\n\r];
   fragment Digit : [0-9];
   fragment WordChar : [0-9a-zA-Z];
   
   Whitespace : WhitespaceChar+ -> skip;
   Integer : Digit+;
   ```

   运行

   ```
   java -jar /usr/local/lib/antlr-4.8-complete.jar -Dlanguage=Python3 -visitor -o minidecaf/generated minidecaf/Expr.g4
   ```

   可以生成对应的`minilexer`和`miniparser`。放在`generated`文件夹下, 生成的类名为`ExprParser`, `ExprLexer`, `ExprVsitor`

   注意设置`parser._errHandler = BailErrorStrategy()`

2. ##### 遍历AST，生成IR

   本阶段的IR生成较为简单，实际上只需要支持`Ret`和`Const`的IR。

   为了支持后面的多遍，每个IR指令都作为一个类，以`IrBaseInstraction`为基类，派生出若干个IR指令类。

   继承`ExprVisitor`实现`StackIRVisitor`, 实现了`visitStatement`和`visitExpr`两个函数。`AST`遍历到`Statement`时，只需要生成`IrRet`；遍历到`IrExpr`时，只需要将`IrConst(int(ctx.Integer().getText()))`生成。

   生成的同时进行**数值检查**，当数值属于`[0, 2^31-1]`是视为正确，否则报错．

3. ##### 将IR转换为RISC-V语言

   类似IR，我将每个`RISC-V`指令划分为类，以~为基类，派生出`AsmInstruction`代表指令类，`AsmLabel`代表汇编标号，`AsmComment`便于添加注释，`AsmDirective`用于汇编指导语句。

   针对每个IR，生成对应的汇编指令，并封装成函数。

   对于常量IrConst(v)， 只需要将数值放在栈顶。我将其封装为`push_im()`函数。实际的汇编指令为：

   ```assembly
   addi sp, sp, -4
   li t1, v
   sw t1, 0(sp)
   ```

   对于指令`IrRet()`，将栈顶的返回值加载到寄存器后返回即可。我将其封装为`pop_reg(reg)`函数将栈顶数值放到寄存器reg中。对应的汇编指令如下：

   ```assembly
   lw a0, 0(sp)
   addi sp, sp, 4
   jr ra
   ```

   在生成汇编指令之前，应该先生成一些指导语句：

   ```assembly
   	.text
   	.globl main
   main:
   	# other instructions
   ```

   最后，只需要遍历IR，将IR翻译成等价的RISC-V即可。我将这一过程封装为了`AsmGenerator`类.

## 思考题

1. ##### 修改 `minilexer` 的输入（`lexer.setInput` 的参数），使得 lex 报错，给出一个简短的例子。

   只需要出现lexer不能识别的字符即可，比如`.`

   ```c
   int main()  {
     return 0.;
   }
   ```

   这段代码在我的实现下会报错：

   ```
   line 2:10 token recognition error at: '.'
   ```

   

2. ##### 修改 `minilexer` 的输入，使得 `lexer` 不报错但 `parser` 报错，给出一个简短的例子。

   满足lexer的要求只需要输入正确的token即可．让parser报错则只需要构造文法无法解析的语法．下面这段代码就无法被parse.

   ```c
   int main()  {
     return 0
   }
   ```

   这段代码在我的实现下会报错：

   ```
   antlr4.error.Errors.ParseCancellationException: None
   ```

3. ##### 在 riscv 中，哪个寄存器是用来存储函数返回值的？

   `a0`寄存器保存返回值。

## Honor Code

1. 上下文无关文法与实验指导书一致。
2. 通读了参考实现的代码，决定参考其多遍的思路，分别进行IR生成、类型检查、左值检查和汇编生成。因此代码骨架和参考实现一致。
  3. 借鉴了参考实现中“将IR指令到汇编的翻译过程抽象为函数”的思路，封装了`push_im, push_reg, pop, pop_reg`等函数，并借助装饰器将他们转换为`AsmInstruction`类的变量。


