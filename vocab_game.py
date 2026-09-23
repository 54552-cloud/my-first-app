import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 📌 จุดที่ 1: เพิ่มการกำหนดค่าเริ่มต้นใน session_state ans3_val และ ans4_val[cite: 1]
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""


# 📌 จุดที่ 2: เพิ่มการเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่ st.session_state.ans3_val และ st.session_state.ans4_val[cite: 1]
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2
    st.session_state.ans3_val = ""  # เคลียร์ค่าช่องข้อ 3
    st.session_state.ans4_val = ""  # เคลียร์ค่าช่องข้อ 4
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
# 📌 จุดที่ 8 (ส่วนรับพารามิเตอร์): เพิ่มการรับค่า ans3 และ ans4 เข้าฟังก์ชัน[cite: 1]
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    # 📌 จุดที่ 3: สรุปผลการเล่นเกมใน MessageBox u_ans3 = ans3.strip().lower() และ u_ans4 = ans4.strip().lower()[cite: 1]
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    # ตรวจข้อ 1
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # 📌 จุดที่ 4: เพิ่มตรวจข้อ 3 และตรวจข้อ 4[cite: 1]
    if u_ans3 == "dog":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    if u_ans4 == "cat":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    # 📌 จุดที่ 5: เพิ่มคะแนน score == 4[cite: 1]
    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ (ใช้ value ผูกกับตัวแปรตรงๆ เพื่อสั่งเคลียร์ได้)
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans2_val,
)

# 📌 จุดที่ 6: เพิ่มช่องรับคำตอบ ans3 = st.text_input และ ans4 = st.text_input[cite: 1]
ans3 = st.text_input(
    "ข้อ 3: A `d _ g` is man's best friend. 🐶",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: A `c _ t` likes to chase mice. 🐱",
    value=st.session_state.ans4_val,
)

# 📌 จุดที่ 7: เพิ่มการอัปเดตค่าล่าสุดเข้าตัวแปร st.session_state.ans3_val = ans3 และ st.session_state.ans4_val = ans4[cite: 1]
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4

# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 📌 จุดที่ 8: เพิ่มการแสดง Dialog ผลลัพธ์ ans3, ans4[cite: 1]
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4)

st.divider()
st.write("นาย รัชชาพงษ์ เกษพรหม เลขที่ 21 ม.4/4")
