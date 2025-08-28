import streamlit as st

st.set_page_config(page_title="🏸 Tính tiền team Hắc Long của Phú 🏸", page_icon="🏸")

st.title("🏸 Tính tiền team Hắc Long của Phú 🏸")

# Nhập dữ liệu cơ bản
tong_tien = st.number_input("💰 Tổng tiền sân", min_value=0, step=1000)
so_nam = st.number_input("👦 Số nam (100%)", min_value=0, step=1)
so_nu = st.number_input("👩 Số nữ (70%)", min_value=0, step=1)

# Phụ thu
st.subheader("➕ Phí phụ thu")
phu_thu = []
so_nguoi_phu_thu = st.number_input("Số người có phụ thu (mua nước, ăn vặt...)", min_value=0, step=1)

for i in range(so_nguoi_phu_thu):
    col1, col2 = st.columns([2,1])
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
    st.write(f"👦 Mỗi nam trả: **{tien_nam:,} VND**")
    st.write(f"👩 Mỗi nữ trả: **{tien_nu:,} VND**")

    if phu_thu:
        st.subheader("🧾 Phụ thu thêm:")
        for ten, tien in phu_thu:
            st.write(f"- {ten}: +{tien:,} VND")

        tong_phu_thu = sum(t for _, t in phu_thu)
        st.info(f"💡 Tổng phụ thu: **{tong_phu_thu:,} VND**")
