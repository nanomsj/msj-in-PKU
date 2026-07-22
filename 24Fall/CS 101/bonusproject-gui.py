import pandas as pd
import easygui
from collections import Counter

file_path = easygui.fileopenbox("请选择CSV文件", filetypes=["*.csv"])

def main():
    try:
        df = pd.read_csv(file_path)
        if "time" not in df.columns:
            easygui.msgbox('格式错误')
        else:
            df["hour"] = pd.to_datetime(df["time"]).dt.hour
            hour_counts = Counter(df["hour"])
            sorted_counts = sorted(hour_counts.items(), key=lambda x: x[1], reverse=True)
            result = "地震发生次数按小时排序:\n\n"
            for hour, count in sorted_counts:
                result += f"{count} 次, 时间: {hour}时\n"
            
            #结果
            easygui.textbox("结果", "每小时地震发生次数", result)
    except Exception as e:
        easygui.msgbox(f"错误: {e}")

main()