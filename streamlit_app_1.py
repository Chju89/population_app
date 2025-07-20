
import streamlit as st
import pandas as pd
from services.db_handler import insert_citizen, update_citizen, delete_citizen, search_by_perID, search_by_name

st.title("📋 Quản Lý Dân Số (Local - SQLite)")

tab_names = ["🔍 Tìm kiếm", "➕ Thêm", "🛠️ Sửa/Xoá"]

# Gán tab mặc định nếu chưa có
if "active_tab" not in st.session_state:
    st.session_state["active_tab"] = tab_names[0]
if "last_tab" not in st.session_state:
    st.session_state["last_tab"] = tab_names[0]

# So sánh và reset dữ liệu nếu chuyển tab
if st.session_state["active_tab"] != st.session_state["last_tab"]:
    for key in [
        "search_results", "search_perid_result", "query_string",
        "add_name", "add_dob", "add_sex", "add_perid",
        "update_name", "update_dob", "update_sex"
    ]:
        st.session_state.pop(key, None)
    st.session_state["last_tab"] = st.session_state["active_tab"]

# Tabs
tab1, tab2, tab3 = st.tabs(tab_names)

with tab1:
    st.session_state["active_tab"] = tab_names[0]
    st.header("Tìm kiếm công dân")
    search_type = st.radio("Tìm theo:", ["perID", "name"])
    query = st.text_input("Nhập nội dung cần tìm")
    page_size = 20

    if st.button("Tìm"):
        if search_type == "perID":
            result = search_by_perID(query)
            st.session_state["search_perid_result"] = result if result else None
        else:
            results = search_by_name(query)
            st.session_state["search_results"] = results
            st.session_state["query_string"] = query

    if search_type == "perID" and "search_perid_result" in st.session_state:
        result = st.session_state["search_perid_result"]
        if result:
            st.success(result)
        else:
            st.warning("Không tìm thấy.")
    elif search_type == "name" and "search_results" in st.session_state:
        results = st.session_state["search_results"]
        if results:
            df = pd.DataFrame(results, columns=["perID", "Name", "DOB", "Sex"])
            total_results = len(df)
            total_pages = (total_results - 1) // page_size + 1
            page = st.number_input("Trang", min_value=1, max_value=total_pages, value=1, step=1)
            start_idx = (page - 1) * page_size
            end_idx = start_idx + page_size
            st.success(f"Tìm thấy {total_results} kết quả – Trang {page}/{total_pages}")
            st.dataframe(df.iloc[start_idx:end_idx])
        else:
            st.warning("Không tìm thấy.")

with tab2:
    st.session_state["active_tab"] = tab_names[1]
    st.header("Thêm công dân mới")
    name = st.text_input("Họ tên", key="add_name")
    dob = st.date_input("Ngày sinh", key="add_dob")
    sex = st.selectbox("Giới tính", ["M", "F"], key="add_sex")
    perID = st.text_input("Mã định danh (UUID)", key="add_perid")

    if st.button("Thêm"):
        insert_citizen(perID, name, dob.isoformat(), sex)
        st.success("Đã thêm thành công!")

with tab3:
    st.session_state["active_tab"] = tab_names[2]
    st.header("Cập nhật hoặc xoá công dân")
    perID = st.text_input("Nhập mã định danh để cập nhật hoặc xoá", key="update_perid")
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
