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
