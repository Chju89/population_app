
import streamlit as st
from services.db_handler import insert_citizen, update_citizen, delete_citizen, search_by_perID, search_by_name

st.title("📋 Quản Lý Dân Số (Local - SQLite)")

tab1, tab2, tab3 = st.tabs(["🔍 Tìm kiếm", "➕ Thêm", "🛠️ Sửa/Xoá"])

with tab1:
    st.header("Tìm kiếm công dân")
    search_type = st.radio("Tìm theo:", ["perID", "name"])
    query = st.text_input("Nhập nội dung cần tìm")
    if st.button("Tìm"):
        if search_type == "perID":
            result = search_by_perID(query)
            if result:
                st.success(result)
            else:
                st.warning("Không tìm thấy.")
        else:
            results = search_by_name(query)
            if results:
                st.success(f"Tìm thấy {len(results)} kết quả")
                st.dataframe(results)
            else:
                st.warning("Không tìm thấy.")

with tab2:
    st.header("Thêm công dân mới")
    name = st.text_input("Họ tên")
    dob = st.date_input("Ngày sinh")
    sex = st.selectbox("Giới tính", ["M", "F"])
    perID = st.text_input("Mã định danh (UUID)")

    if st.button("Thêm"):
        insert_citizen(perID, name, dob.isoformat(), sex)
        st.success("Đã thêm thành công!")

with tab3:
    st.header("Cập nhật hoặc xoá công dân")
    perID = st.text_input("Nhập mã định danh để cập nhật hoặc xoá")

    action = st.radio("Hành động", ["Cập nhật", "Xoá"])
    if action == "Cập nhật":
        name = st.text_input("Tên mới", key="update_name")
        dob = st.date_input("Ngày sinh mới", key="update_dob")
        sex = st.selectbox("Giới tính mới", ["M", "F"], key="update_sex")
        if st.button("Cập nhật"):
            update_citizen(perID, name, dob.isoformat(), sex)
            st.success("Đã cập nhật thành công!")
    else:
        if st.button("Xoá"):
            delete_citizen(perID)
            st.success("Đã xoá thành công!")
