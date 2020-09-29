#!/bin/bash
echo "这里面放你在运行前要跑的命令，比如运行 parser generator 等。"
apt install parallel
pip install -r minidecaf/requirements.txt
java -jar /usr/local/lib/antlr-4.8-complete.jar -Dlanguage=Python3 -visitor -o minidecaf/generated minidecaf/Expr.g4
