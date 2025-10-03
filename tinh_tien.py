import streamlit as st
import urllib.parse

# ===== HÌNH NỀN =====
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), 
                    url("https://github.com/neroneo1991-pixel/upload-hinh/blob/main/ChatGPT%20Image%2014_24_02%2017%20thg%209,%202025.png?raw=true");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===== CẤU HÌNH APP =====
st.set_page_config(page_title="🏸 Tính tiền team Hắc Long của Phú 🏸", page_icon="🐉")
st.title("🏸 Hắc Long Bang - Càng phang càng thích 🐉")

# ===== NHẬP DỮ LIỆU =====
tong_tien = st.number_input("💰 Tổng tiền sân + cầu", min_value=0, step=1000)
so_nam = st.number_input("👦 Số nam (100%)", min_value=0, step=1)
so_nu = st.number_input("👩 Số nữ (70%)", min_value=0, step=1)
so_50 = st.number_input("🧍‍♂️ Người đóng 50% (đi nửa buổi)", min_value=0, step=1)

# ===== PHỤ THU =====
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

# ===== TÍNH TOÁN =====
if st.button("📊 Tính tiền"):
    tong_trong_so = so_nam * 1 + so_nu * 0.7 + so_50 * 0.5
    tien_mot_trong_so = tong_tien / tong_trong_so if tong_trong_so > 0 else 0

    tien_nam = round(tien_mot_trong_so * 1)
    tien_nu = round(tien_mot_trong_so * 0.7)
    tien_50 = round(tien_mot_trong_so * 0.5)

    st.success("✅ Kết quả chia tiền:")

    if so_nam > 0:
        st.write(f"👦 Mỗi nam trả: **{tien_nam:,} VND**")

    if so_nu > 0:
        st.write(f"👩 Mỗi nữ trả: **{tien_nu:,} VND**")

    if so_50 > 0:
        st.write(f"🧍‍♂️ Mỗi người 50% trả: **{tien_50:,} VND**")

    if phu_thu:
        st.subheader("🧾 Phụ thu thêm:")
        for ten, tien in phu_thu:
            st.write(f"- {ten}: +{tien:,} VND")
        tong_phu_thu = sum(t for _, t in phu_thu)
        st.info(f"💡 Tổng phụ thu: **{tong_phu_thu:,} VND**")

    # ===== QR CHUYỂN KHOẢN =====
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
