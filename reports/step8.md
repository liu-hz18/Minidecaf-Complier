# Step 8 Report

###### 刘泓尊　2018011446　计84

## 实验目的

1. 增加循环语句和 `break/continue` 的支持

## 实验过程

 1. #### 修改文法，支持for, while, do-while语句和 break, continue语句

    ```
    statement
        : 'return' expr ';'   # RetStatement
        | expr? ';'           # ExprStatement
        | block               # BlockStatement
        | 'if' '(' expr ')' thens=statement ('else' elses=statement)? # IfStatement  
        // 新增的语句
        | 'for' '(' expr? ';' expr? ';' expr? ')' statement  # forNaiveStatement
        | 'for' '(' declaration expr? ';' expr? ')' statement  # forDeclareStatement
        | 'while' '(' expr ')' statement        # WhileStatement
        | 'do' statement 'while' '(' expr ')' ';'  # doWhileStatement
        | 'break' ';'               # BreakStatement
        | 'continue' ';'            # ContinueStatement
        ;
    ```

 2. #### 遍历AST，生成循环语句对应的IR

    对于三种不同的循环，都可以抽象成如下过程：

    ```c++
    { // pre 里面可能有声明，所以需要这个作用域
        pre;                // 可能是空、也可能是一个 declaration 或者 expression
        while (cond) {      // 可能是空、也可能是一个 expression
            body;
            // body 里的 continue 会跳转到这里
            post;           // 是一个 expression
        }
        // break 跳转到这里
    }
    ```

    同时，为了标注每个`break`和`continue`的目的地址，同样引入全局计数器并用表维护`break`标号栈和`continue`标号栈．遇到 `Loop(...)` 就创建这个循环的 `break` 标号和 `continue` 标号（以及起始标号），把两个标号压入各自栈里，离开 `Loop` 的时候弹栈．每次遇到 `break` 语句，其跳转目标就是 `break` 标号栈的栈顶，如果栈为空就报错。`continue` 语句类似．

    上述Ｃ代码对应的IR如下

    ```
    pre 的IR
    label BEGINLOOP_LABEL: //开始下一轮迭代
    cond 的 IR
    beqz BREAK_LABEL //条件不满足就终止循环
    body 的 IR
    label CONTINUE_LABEL: //continue 跳到这
    post 的 IR
    br BEGINLOOP_LABEL  //本轮迭代完成
    label BREAK_LABEL: //条件不满足，或者 break 语句都会跳到这儿
    ...
    ```

    对于`for` 循环，对应`loop(pre, cond, body, post)`

    ​	需要注意的是，如果`pre`中有变量声明，需要在最后把变量`pop`出来．

    对于`while`循环，对应`loop(_, cond, body, _)`

    对于`do-while`循环，对应`loop(body, cond, body, _)`

 3. #### 没有新增IR指令，所以不需要修改汇编生成

# 思考题

1. #### 将循环语句翻译成 IR 有许多可行的翻译方法，例如 `while` 循环可以有以下两种翻译方式：

   第一种（即实验指导中的翻译方式）：

   1. `label BEGINLOOP_LABEL`：开始下一轮迭代
   2. `cond 的 IR`
   3. `beqz BREAK_LABEL`：条件不满足就终止循环
   4. `body 的 IR`
   5. `label CONTINUE_LABEL`：continue 跳到这
   6. `br BEGINLOOP_LABEL`：本轮迭代完成
   7. `label BREAK_LABEL`：条件不满足，或者 break 语句都会跳到这儿

   第二种：

   1. `cond 的 IR`
   2. `beqz BREAK_LABEL`：条件不满足就终止循环
   3. `label BEGINLOOP_LABEL`：开始下一轮迭代
   4. `body 的 IR`
   5. `label CONTINUE_LABEL`：continue 跳到这
   6. `cond 的 IR`
   7. `bnez BEGINLOOP_LABEL`：本轮迭代完成，条件满足时进行下一次迭代
   8. `label BREAK_LABEL`：条件不满足，或者 break 语句都会跳到这儿

#### 从执行的指令的条数这个角度（`label` 指令不计算在内，假设循环体至少执行了一次），请评价这两种翻译方式哪一种更好？

​			先从一个例子入手，考虑如下C代码根据两种方式生成的汇编代码：

```C
i = 0;
while(i < 10) {
	i+=1;
}
```

​		采用第一种方式，得到的IR代码为:

```
BEGIN_LOOP:
	i < 10 ?
	beqz BREAK_LABEL
	i += 1
CONTINUE_LABEL:
	br BEGIN_LOOP
BREAK_LABEL:
```

​		采用第二种方式，得到的IR代码为：

```
	i < 10 ? 
	beqz BREAK_LABEL
BEGIN_LOOP:
	i += 1
CONTINUE_LABEL:
	i < 10 ?
	bnez BEGIN_LOOP
BREAK_LABEL:
```

​	可以看到, 循环进行了`10`次，第一段代码有4 x 10 + 2 = 42条．第二段代码有2 + 3 x 10 = 32条．

​	如果添加了`break`语句，两者增加的语句条数是相同的．

​	如果添加了`continue`语句，因为都要跳转到`CONTINUE_LABEL`，所以两者增加的语句也是相同的．

​	所以对于`while`循环，采用**第二种方式**，指令条数更少．原因在于后者`bnez BEGIN_LOOP`一次跳转即可代替前者`br BEGIN_LOOP`，`beqz BREAK_LABEL`两次跳转．

## Honor Code

​	Step8较为简单，按照实验指导书编写代码即可．