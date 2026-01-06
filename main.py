import streamlit as st

st.title("📏 圓形與扇形幾何計算器")
st.write("適合國小數學教學，圓周率以 **3.14** 計算")

# 使用下拉選單
shape = st.selectbox("請選擇要計算的圖形：", ["請選擇", "圓形", "扇形"])

pi_val = 3.14

if shape == "圓形":
    # value=None 會讓輸入框預設為空
    radius = st.number_input("請輸入圓的半徑（公分）：", min_value=0.0, step=0.1, value=None)

    if radius is not None and radius > 0:
        c = 2 * pi_val * radius
        d = pi_val * (radius ** 2)

        st.success(f"### 圓形計算結果")
        st.write(f"👉 **圓周長**：{round(c, 2)} 公分")
        st.write(f"👉 **圓面積**：{round(d, 2)} 平方公分")

elif shape == "扇形":
    # 兩欄預設皆為空值
    radius = st.number_input("請輸入扇形的半徑（公分）：", min_value=0.0, step=0.1, value=None)
    # step=1 且輸入整數，會自動限制為整數輸入框
    angle = st.number_input("請輸入扇形的中心角度（整數）：", min_value=0, max_value=359, step=1, value=None)

    if radius is not None and angle is not None:
        if radius > 0 and angle > 0:
            # 計算邏輯
            arc_length = 2 * pi_val * radius * (angle / 360)  # 弧長
            perimeter = arc_length + (2 * radius)  # 周長 (弧長 + 2條半徑)
            area = pi_val * (radius ** 2) * (angle / 360)  # 面積

            st.success(f"### 扇形計算結果")
            st.write(f"👉 **弧長**：{round(arc_length, 2)} 公分")
            st.write(f"👉 **扇形周長** (含半徑)：{round(perimeter, 2)} 公分")
            st.write(f"👉 **扇形面積**：{round(area, 2)} 平方公分")

elif shape == "請選擇":
    st.info("請在上方選單選擇一個圖形開始計算。")