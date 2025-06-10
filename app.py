
import streamlit as st
import os
import json

# 初始化
os.makedirs("story", exist_ok=True)
os.makedirs("puzzle", exist_ok=True)
os.makedirs("data", exist_ok=True)
progress_path = "data/progress.json"

# 初次建立進度檔
if not os.path.exists(progress_path):
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump({"current_day": 1}, f)

# 載入進度
def load_progress():
    with open(progress_path, "r", encoding="utf-8") as f:
        return json.load(f)

# 儲存進度
def save_progress(data):
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# 讀檔工具
def read_file(folder, day):
    path = f"{folder}/day{day}.txt"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        return f"(尚未建立 {path})"

# 正確答案表
correct_answers = {
    1: "B", 2: "B", 3: "C", 4: "B", 5: "A",
    6: "C", 7: "C", 8: "A", 9: "B", 10: "B",
    11: "B", 12: "C", 13: "B", 14: "C", 15: "C",
    16: "B", 17: "C", 18: "B", 19: "C", 20: "C", 21: "C"
}

# 介面開始
st.set_page_config(page_title="燈下謎影", layout="centered")
st.title("🕯️ 燈下謎影：21 天推理解謎")

progress = load_progress()
current_day = progress["current_day"]
st.markdown(f"### 📅 第 {current_day} 天")

# 顯示故事
st.subheader("📜 今日劇情")
st.text(read_file("story", current_day))

# 顯示題目
st.subheader("🧩 推理解謎")
st.text(read_file("puzzle", current_day))
user_answer = st.radio("你的推理答案：", ["A", "B", "C", "D"])

# 提交解答
if st.button("✅ 提交答案"):
    if user_answer == correct_answers.get(current_day):
        st.success("答對了！已解鎖下一天。")
        if current_day < 21:
            progress["current_day"] += 1
        save_progress(progress)
    else:
        st.error("答錯了，再觀察一下線索吧！")

# 測試用：查看今天內容
if st.checkbox("🔍 顯示故事與題目原文"):
    st.text(read_file("story", current_day))
    st.text(read_file("puzzle", current_day))
