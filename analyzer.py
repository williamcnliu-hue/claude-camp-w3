import pandas as pd
import json

# 1. 读取 CSV
df = pd.read_csv('students.csv')

# 2. 基础统计
total = len(df)
country_count = df['country'].value_counts().to_dict()
status_count = df['bet_status'].value_counts().to_dict()
completed = status_count.get('completed', 0)
completion_rate = round(completed / total * 100, 1)

# 3. 脏数据检测(Candy 扎实派核心）
email_missing = int(df['email'].isna().sum())
parsed_dates = pd.to_datetime(df['joined_date'], errors='coerce')
date_unparseable = int(parsed_dates.isna().sum())

# 4. 打印到屏幕看一眼
print(f"总人数: {total}")
print(f"各国人数: {country_count}")
print(f"对赌完成率: {completion_rate}%")
print(f"⚠️ 空邮箱: {email_missing} 个")
print(f"⚠️ 坏日期: {date_unparseable} 个")

# 5. 存成 report.json
report = {
    'total': total,
    'country_count': country_count,
    'completion_rate': completion_rate,
    'email_missing': email_missing,
    'date_unparseable': date_unparseable
}
with open('report.json', 'w') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print("✅ 报告已存到 report.json")
