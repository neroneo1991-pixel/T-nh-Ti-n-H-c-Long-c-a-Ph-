import streamlit as st
import base64

# === Hàm chèn ảnh nền ===
def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 📌 Gọi hàm này ở đầu file, trước khi tạo giao diện
set_background("background.png")

st.set_page_config(page_title="🏸 Tính tiền team Hắc Long của Phú 🏸", page_icon="🐉")

st.title("🏸Hắc Long Bang - Càng phang càng thích 🐉")

# Nhập dữ liệu cơ bản
tong_tien = st.number_input("💰 Tổng tiền sân+cầu", min_value=0, step=1000)
so_nam = st.number_input("👦 Số nam (100%)", min_value=0, step=1)
so_nu = st.number_input("👩 Số nữ (70% so với nam, về sớm 1/2 buổi hoặc đi trễ 1/2 tính như nữ luôn)", min_value=0, step=1)

# Phụ thu
st.subheader("➕ Phí phụ thu")
phu_thu = []
so_nguoi_phu_thu = st.number_input("Số người có phụ thu (mua nước, quấn cán, nhậu nhẹt bê tha🤣...)", min_value=0, step=1)

for i in range(so_nguoi_phu_thu):
    col1, col2 = st.columns([2, 1])
    with col1:
        ten = st.text_input(f"Tên người {i+1}", key=f"ten_{i}")
    with col2:
        tien = st.number_input(f"Tiền phụ thu {i+1}", min_value=0, step=1000, key=f"tien_{i}")
    if ten:
        phu_thu.append((ten, tien))

# Tính toán
if st.button("📊 Tính tiền"):
    tong_trong_so = so_nam * 1 + so_nu * 0.7
    tien_mot_trong_so = tong_tien / tong_trong_so if tong_trong_so > 0 else 0

    tien_nam = round(tien_mot_trong_so * 1)
    tien_nu = round(tien_mot_trong_so * 0.7)

    st.success("✅ Kết quả chia tiền:")
    
    # Chỉ hiển thị nếu có nam
    if so_nam > 0:
        st.write(f"👦 Mỗi nam trả: **{tien_nam:,} VND**")

    # Chỉ hiển thị nếu có nữ
    if so_nu > 0:
        st.write(f"👩 Mỗi nữ trả: **{tien_nu:,} VND**")

    if phu_thu:
        st.subheader("🧾 Phụ thu thêm:")
        for ten, tien in phu_thu:
            st.write(f"- {ten}: +{tien:,} VND")

        tong_phu_thu = sum(t for _, t in phu_thu)
        st.info(f"💡 Tổng phụ thu: **{tong_phu_thu:,} VND**")
         # ==== CHÈN QR CHUYỂN KHOẢN Ở ĐÂY ====
    import urllib.parse

    st.subheader("🏦 Thông tin chuyển khoản")
    st.write("📌 Số tài khoản: **7890727041991**")
    st.write("👤 Chủ tài khoản: **Đặng Quang Phú**")
    st.write("🏦 Ngân hàng: **MB Bank**")

    so_tien_mac_dinh = 0  # muốn set sẵn số tiền thì đổi số 0 này
    noi_dung_ck = "Tien cau long Hac Long"

    qr_url = (
        f"https://img.vietqr.io/image/970422-7890727041991-compact.png?"
        f"amount={so_tien_mac_dinh}&addInfo={urllib.parse.quote(noi_dung_ck)}&accountName={urllib.parse.quote('Đặng Quang Phú')}"
    )

    st.image(qr_url, caption="📷 Quét QR để chuyển khoản", width=250)
import streamlit as st
import pandas as pd

st.title("💵 Quản lý đóng tiền")

# Lưu danh sách vào session_state
if "members" not in st.session_state:
    st.session_state.members = []

# Nhập thông tin 1 lần để tạo danh sách
with st.expander("⚙️ Cấu hình chia tiền"):
    tong_tien = st.number_input("Tổng tiền (đ)", value=600000, step=50000)
    so_nam = st.number_input("Số nam", value=6, step=1)
    so_nu = st.number_input("Số nữ", value=0, step=1)

# Nút tạo danh sách
if st.button("Tạo danh sách mới"):
    st.session_state.members = []
    # Tính trọng số
    tong_trong_so = so_nam * 1 + so_nu * 0.7
    if tong_trong_so > 0:
        tien_mot_nam = round(tong_tien / tong_trong_so * 1)
        tien_mot_nu = round(tong_tien / tong_trong_so * 0.7)
    else:
        tien_mot_nam, tien_mot_nu = 0, 0

    # Nam
    for i in range(int(so_nam)):
        st.session_state.members.append({
            "Tên": f"Nam {i+1}",
            "Số tiền": tien_mot_nam,
            "Đã đóng": False
        })
    # Nữ
    for i in range(int(so_nu)):
        st.session_state.members.append({
            "Tên": f"Nữ {i+1}",
            "Số tiền": tien_mot_nu,
            "Đã đóng": False
        })

# Hiển thị danh sách
for i, m in enumerate(st.session_state.members):
    col1, col2, col3 = st.columns([2,1,1])
    with col1:
        st.session_state.members[i]["Tên"] = st.text_input(
            f"Tên {i+1}", m["Tên"], key=f"name_{i}"
        )
    with col2:
        st.write(f"{m['Số tiền']:,} đ")
    with col3:
        st.session_state.members[i]["Đã đóng"] = st.checkbox(
            "Đã đóng", value=m["Đã đóng"], key=f"check_{i}"
        )

# Bảng tổng hợp
if st.session_state.members:
    df = pd.DataFrame(st.session_state.members)
    st.dataframe(df, use_container_width=True)

    # Tổng thu chi
    da_thu = df[df["Đã đóng"]]["Số tiền"].sum()
    con_thieu = tong_tien - da_thu
    st.success(f"✅ Đã thu: {da_thu:,} đ | ❌ Còn thiếu: {con_thieu:,} đ")
