# 约定
为了方便测试，请你做实验时，遵守以下约定。

* 使用 python3，不用 python2.

* 使用 pip 管理依赖。

| 文件/目录 | 说明 |
| --- | --- |
| `README.md` | 项目说明。随便改。 |
| `.gitlab-ci.yml` | 自动测试配置， **不能改动！** |
| `prepare.sh` | 运行测试前你要运行的命令，例如运行 parser generator。可以改，只要保证能被 bash 运行即可。 |
| `step-until.txt` | 告诉自动测试，你做到哪个 step 了。可以改，须保证内容是 1 到 12 的一个整数。 **做完每个 step 后请及时修改，避免影响评分！** |
| `reports/` | 实验报告，使用 pdf 或 md 格式，命名格式如 `step1.pdf`、`step2.md` 等。 |
| `minidecaf/requirements.txt` | 依赖，使用 pip 安装。 **不能删除！**，没有依赖也要有空的 requirements.txt。 可以改，但需要符合 requirements.txt 标准格式。 |
| `minidecaf/__main__.py` | 你的编译器入口。可以改。 |
| `minidecaf/` | 放你的编译器代码。 |

你的依赖都需要从 pip 安装，自动测试不一定支持其他依赖安装。

# 评分
MiniDecaf 有 6 个阶段，每个阶段的 ddl 截止时，我们会检查你最后一次通过 CI 的 commit。

* 如果 `.gitlab-ci.yml` 没有改动，并且 `step-until.txt` 中的数字大于等于那个阶段的最后一个 step 编号，我们就认为你按时完成了该阶段任务。

* 否则，我们会等待你通过该阶段任务，并且按照指导书所说折算晚交扣分。


实验注意事项

本学期《编译原理》的实验是实现 MiniDecaf 编译器。请阅读指导书 https://decaf-lang.github.io/minidecaf-tutorial/ 、按时完成实验并且将你的代码提交到 https://git.tsinghua.edu.cn/compiler-20/minidecaf-你的学号 中。

 

我们已经把一个初始仓库放到你的仓库里，请阅读初始仓库的 README，然后在初始仓库基础上继续实验。如果你要换语言，请用 https://git.tsinghua.edu.cn/compiler-20/语言-repo 的最新内容覆盖你的仓库后再重新开始实验，其中语言可以是 python/java/cpp/rust/typescript/others，然后告知助教你更换语言。

 

完成 step X (1 <= X <= 12) 的实验后，请把你的实验报告放在 reports/stepX.md 或者 reports/stepX.pdf 中。实验报告内容中你需要包含的内容有：

1. 你的学号姓名

2. 简要叙述，为了完成这个 step 你做了哪些工作（即你的实验内容）

3. 回答指导书上的思考题

4. 如果你复用借鉴了参考代码或其他资源，请明确写出你借鉴了哪些内容。并且，即使你声明了代码借鉴，你也需要自己独立认真完成实验。

 

每个阶段的截止日期在网络学堂作业中，截止后待助教批改完报告就会确定成绩。


评分方法

每次实验满分 10 分，其中代码运行 5 分，报告 5 分。

请不要以非正常手段通过测试（例如但不限于：直接照搬参考实现一字不改、枚举输入输出关系），第一次会导致成绩失效 0 分，第二次开始会按照当次 step 得 -10 分计算。

代码运行评定标准：每个阶段截止后，我们会抓取你最后一次成功的自动测试（无论在哪个分支上）。如果 .gitlab-ci.yml 被修改了那么成绩无效，否则只要你的 step-until.txt 大于等于这个阶段的最后一个 step，代码运行即满分。注意你需要通过一个 step 的所有测例才算通过该 step，因此截止日期时如果你只通过部分测例，你的成绩按满分乘以你通过所有测例时的晚交折算系数计算。

报告评定标准：按照你的工作描述、思考题回答情况决定。描述和回答清晰到点即可，不必冗长。