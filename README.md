# Claude Camp Week 3 · 数据处理 + 文件 I/O + Git 进阶

Phase 0 收官周。三个项目,每个用独立 feature branch 开发,完整跑通 Git 分支工作流。

## 项目 1 · CSV 学员数据分析器 (`analyzer.py`)
- pandas 读 CSV → 统计各国人数、对赌完成率
- **脏数据防御**:检测空邮箱 (`isna`)、坏日期 (`pd.to_datetime errors='coerce'`)
- 输出结构化 `report.json`

## 项目 2 · JSON 配置读写器 (`config_editor.py`)
- 读 `config.json` → 命令行交互改设置 → 存回
- **数据验证**:font_size 范围 8-32、theme/language 枚举检查、类型检查
- 非法输入一律挡在门外

## 项目 3 · 字符串工具库 + pytest (`string_utils.py` / `test_string_utils.py`)
- 三个函数:`reverse_words` / `count_vowels` / `is_palindrome`(含类型验证 + docstring)
- **pytest 三类用例**:每个函数测正常 / 边界 / 异常,共 9 个测试全过
- 异常用 `pytest.raises(TypeError)`

## 学习感悟
W3 自发踩平三个真实工程坑:`root-commit` 新仓库没 main(用 `git branch -M main` 修)、venv 虚拟环境隔离 pandas、pytest 靠 `test_` 前缀找测试文件。
工具会过时,拆解问题、定位 bug 的能力永远值钱。
