# Step 9 Report

###### 刘泓尊　2018011446　计84

## 实验目的

​	1. 增加函数功能，实现函数的声明，定义和调用

## 实验过程

 1. #### 修改文法，支持多函数，函数声明，函数调用和参数列表

    ```
    program: func+ EOF;
    func
        : tp Identifier '(' paramlist ')' block   # funcDefine
        | tp Identifier '(' paramlist ')' ';'     # funcDeclare
        ;
    paramlist
        : (paramDeclare (',' paramDeclare)*)?
        ;
    paramDeclare
        : tp Identifier
        ;
    postfix
        : primary                       # SinglePostfix
        | Identifier '(' exprlist ')'   # ComplexPostfix　　//　func call
        ;
    ```

 2. #### IR生成，语义检查，检查函数重定义，形参实参匹配

    在名称检查阶段，支持对函数参数的定义，即对参数列表，定义对应的变量并加入符号表即可．

    在IR生成阶段，需要支持对函数参数的生成，同时进行重定义检查和参数匹配检查．

    首先在`IrFunction`类中添加参数类型列表字段，以进行参数匹配检查．

    在函数定义语句，需要解析出该函数的参数个数，参数类型和参数名．如果有重名参数则报错．如果该函数定义和之前声明的同名函数冲突，则报错．

    在函数声明语句，同样要解析出该函数的参数个数，参数类型和参数名．如果有重名参数则报错．如果该函数声明和之前定义的同名函数冲突，则报错．

    在函数调用语句，将当前调用函数名和之前已声明或定义的函数参数列表对比，如果存在参数个数或参数类型的不一致，则报错．没有出错则需要**将参数逆序压栈**，最后向IR栈中压入`IrCall`指令．

 3. #### 完成IR到汇编的翻译

    需要支持IrCall指令，对应的汇编如下：

```assembly
	call <func_name>
	addi sp, sp, {4*(num_param-1)} # 有几个参数就执行几次 pop,我将其合并为一个语句
	sw a0, 0(sp)
```

## 思考题

1. MiniDecaf 的函数调用时参数求值的顺序是未定义行为。试写出一段 MiniDecaf 代码，使得不同的参数求值顺序会导致不同的返回结果。

   ```c
   int add(int a, int b) {
   	return a + b;
   }
   int main() {
       int a = 10;
       int c = add(a = a + 1, a = a + 2);
       return 0;
   }
   ```

   如果先执行`a = a  + 1`, 那么传入参数实际为`add(11, 13)`, 返回值`c = 24`

   如果先执行`a = a + 2`, 那么传入参数实际是`add(13, 12),` 返回值`c = 25`

   所以不同的参数求值顺序会导致不同的返回结果．

   在我的实现中，该函数会返回`25`，也就是从右向左求值，这是因为参数逆序压栈同时进行IR生成的结果．

## Honor Code

​	本节内容比较简单，因为step 5中已经支持了函数建立栈帧和销毁栈帧，主要内容是语义检查，按照实验指导书即可实现．