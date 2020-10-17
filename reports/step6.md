# Step 6 Report

###### 刘泓尊　2018011446　计84

## 实验目的

　1.　支持`if`语句和条件表达式

## 实验过程

 1. #### 修改文法，支持if语句和条件表达式，同时增加块语句，为下一阶段做准备

    ```antlr4
    block
        : '{' blockitem* '}'
        ;
    blockitem
        : statement           # SingleStatement
        | declaration         # DeclareStatement
        ;
    statement
        : 'return' expr ';'   # RetStatement
        | expr? ';'           # ExprStatement
        | block               # BlockStatement
        | 'if' '(' expr ')' thens=statement ('else' elses=statement)? # IfStatement   
        ;
    conditional
        : logicalOr                             # SingleCond
        | logicalOr '?' expr ':' conditional    # ComplexCond
        ;
    ```

    对于if-else的二义性，在parser阶段已经可以完成，因为anltlr4从左到右匹配if-else语句，遇到`thens=statement`的时候，会优先展开该`statement`．所以if-else实际上采用了**＂`else` 和最近的 `if` 结合＂**的方式解决**悬吊 else**问题．

 2. #### 增加IR指令，支持条件判断

    为了支持跳转，需要增加label，标记一个跳转的目的地，使用一个全局的计数器为跳转创建别名即可．

    同时增加了IrBranch的指令，维护跳转的操作类型和目的地址．

    对于if语句，可以分为if_end和if_else阶段，如果if语句有else配对，则生成的IR指令为：

    1. 首先是 `条件表达式的 IR`：计算条件表达式。
    2. `beqz ELSE_LABEL`：判断条件，若条件不成立则执行 else 子句
    3. 跳转没有执行，说明条件成立，所以之后是 `then 子句的 IR`
    4. `br END_LABEL`：条件成立，执行完 `then` 以后就结束了
    5. `label ELSE_LABEL`，然后是 `else 子句的 IR`
    6. `label END_LABEL`：`if` 语句结束。

    对于单独的if语句，只需要判断条件是否成立，不成立直接跳到`END_LABEL`即可．

    对于三元表达式，参考上述if-else的情况即可，非常类似．

 3. #### 完成IR到汇编的翻译过程

    翻译过程比较简单，对于无条件跳转br，翻译为`j label`

    对于有条件跳转指令`beqz`，翻译为

    ```
    lw t1, 0(sp)
    addi sp, sp, 4
    beqz t1, label
    ```

    `bnez`和`beqz`类似．

    label可以翻译为 `label:`

## 思考题

1. #### Rust 和 Go 语言中的 if-else 语法与 C 语言中略有不同，它们都要求两个分支必须用大括号包裹起来，而且条件表达式不需要用括号包裹起来：

```Rust
if 条件表达式 {
  // 在条件为 true 时执行
} else {
  // 在条件为 false 时执行
}
```

#### 	请问相比 C 的语法，这两种语言的语法有什么优点？

​	避免了悬吊else的问题，不会导致语法的二义性，减轻了编译器语法分析的负担．

​	对应的文法可以写成：

```
statement
    : 'return' expr ';'   # RetStatement
    | expr? ';'           # ExprStatement
    | block               # BlockStatement
    | 'if' expr then=block ('else' elses=block)? # IfStatement   
    ;
```

​	　同时这种设计也给程序更好的可读性，避免代码因为缩进错误导致程序员理解错代码的行为，减少潜在的bug风险．

## Honor Code

​		Step6的内容比较简单，按照实验指导书的步骤即可独立完成．