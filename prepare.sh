#!/bin/bash
echo "这里面放你在运行前要跑的命令，比如运行 parser generator 等。"
pip install -r minidecaf/requirements.txt
antlr4 -visitor -no-listener -Dlanguage=Python3 ./minidecaf/Expr.g4 -o ./minidecaf/generated
