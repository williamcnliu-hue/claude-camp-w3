import json

CONFIG_FILE = "config.json"
VALID_THEMES = ["dark", "light"]
VALID_LANGUAGES = ["zh", "en"]


def load_config():
    """读取配置文件，文件不存在就返回默认配置"""
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠️ 配置文件不存在，使用默认配置")
        return {"theme": "dark", "language": "zh", "font_size": 14}


def save_config(config):
    """把配置写回文件"""
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    print("✅ 配置已保存")


def validate(key, value):
    """数据验证：返回 (是否合法, 处理后的值 或 错误信息)"""
    if key == "theme":
        if value not in VALID_THEMES:
            return False, f"theme 只能是 {VALID_THEMES}"
        return True, value
    if key == "language":
        if value not in VALID_LANGUAGES:
            return False, f"language 只能是 {VALID_LANGUAGES}"
        return True, value
    if key == "font_size":
        try:
            num = int(value)
        except ValueError:
            return False, "font_size 必须是数字"
        if num < 8 or num > 32:
            return False, "font_size 必须在 8-32 之间"
        return True, num
    return False, f"未知设置项: {key}"


def main():
    config = load_config()
    print("当前配置:", config)

    while True:
        key = input("\n要改哪个设置？(theme/language/font_size，输入 q 退出): ").strip()
        if key == "q":
            break
        if key not in config:
            print(f"⚠️ 没有这个设置项: {key}")
            continue

        value = input(f"{key} 改成什么？: ").strip()
        ok, result = validate(key, value)
        if ok:
            config[key] = result
            print(f"✅ {key} 已改为 {result}")
        else:
            print(f"❌ {result}")

    save_config(config)
    print("最终配置:", config)


if __name__ == "__main__":
    main()
    