import streamlit as st
# Tiêu đề chính
st.title("Ứng dụng Góp ý Khách hàng")
st.write("Hãy cho chúng tôi biết ý kiến của bạn để cải thiện dịch vụ.")
col1, col2, col3 = st.columns(3)
image = ""
video = ""


# Kiểm tra nút nào được bấm
with col1:
    if st.button("M1917 Rifle"):
        image = "https://tse1.mm.bing.net/th?id=OIF.e1mPzN0IQ2F08%2fp6sI9KEg&pid=Api&P=0&h=180"
        video = "https://youtu.be/IhuBvUVqfO8"
with col2:
    if st.button("AWM sniper"):
        image = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/AWM-338-white.jpg/1200px-AWM-338-white.jpg"
        video = "https://youtu.be/0XYtL8dFXFc"
with col3:
    if st.button("SPAS 12"):
        image= "https://tse4.mm.bing.net/th/id/OIP.w7rsSjpgEOy9JUHkeZnVIAHaEi?pid=Api&P=0&h=180"
        video= "https://youtu.be/6LV-UYS5vOQ"
if image != "" and video != "":
    st.image(image)
    st.video(video)
# Form
with st.form("form_gopy"):
    st.subheader("Góp ý khách hàng")
    
    ho_ten = st.text_input("Nhập họ tên:")
    email = st.text_input("Nhập địa chỉ email:")
    
    san_pham = st.selectbox("Chọn sản phẩm:", ["M1917 Rifle", "AWM sniper", "SPAS 12"])
    
    gop_y = st.text_area("Nhập nội dung góp ý:")
    
    chat_luong = st.slider("Đánh giá chất lượng sản phẩm:", 1, 5)
    
    submit = st.form_submit_button("Gửi góp ý")

# Xử lý sau khi gửi
if submit:
    if ho_ten and email and gop_y:
        st.success("Cảm ơn bạn đã gửi góp ý! 🎉")
        st.balloons()
        
        with st.expander("Xem Lại Góp Ý"):
            st.write("**Họ tên:**", ho_ten)
            st.write("**Email:**", email)
            st.write("**Sản phẩm:**", san_pham)
            st.write("**Nội dung góp ý:**", gop_y)
            st.write("**Đánh giá chất lượng:**", chat_luong)
    else:
        st.error("Vui lòng nhập đầy đủ thông tin!")
