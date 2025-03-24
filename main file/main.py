import streamlit as st


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Skills & Experience", "Contact"])


if page == "Home":
    st.title("Welcome to My Portfolio")
   
    st.write("Hi there! I'm DAIYAN, a PYTHON DEVELOPER. Welcome to my portfolio site. Here you'll find information about my projects, skills, experience, and how to contact me.")

    
    

elif page == "Skills & Experience":
    st.title("Skills & Experience")
    skills = ["python", "driving car", "data analysis", "laptop motherboard work", "any work"]
    experience = ["Job 1 ZTE", "Job 2 at HP", "Internship at AN ENTERPRIZE"]
    
    st.subheader("Skills")
    for skill in skills:
        st.markdown(f"- {skill}")
    
    st.subheader("Experience")
    for exp in experience:
        st.markdown(f"- {exp}")

elif page == "Contact":
    st.title("Contact")
    st.write("Feel free to reach out to me through the following channels:http://www.youtube.com/@CuBe_2-0-1-1")
    st.write("Email: (mail:ahnaf.rahman.daiyan@gmail.com)")
    st.write("Phone: +8801407450808")


st.sidebar.title("Improvement Options")
