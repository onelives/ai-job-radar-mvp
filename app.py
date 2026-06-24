import streamlit as st
from jobs_db import JOBS
from matcher import match_jobs
from resume_parser import parse_pdf
from backend import generate_cover, optimize_resume

st.title("🚀 AI Job Radar MVP")

file = st.file_uploader("上传简历 PDF")

if file:
    text = parse_pdf(file)
    results = match_jobs(text, JOBS)

    st.subheader("匹配结果")

    for job in results:
        st.markdown("---")
        st.write("岗位：", job["title"])
        st.write("匹配分：", job["score"])

        if job["score"] > 0:
            st.success("推荐投递")

            st.write(generate_cover(job["title"]))
            st.write(optimize_resume(text, job["title"]))