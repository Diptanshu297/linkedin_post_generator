import streamlit as st
from post_generator import generate_post, rewrite_post, enhance_post

st.set_page_config(page_title="LinkedIn Job Simulator", layout="centered")

st.title("💼 LinkedIn Job Simulator")
st.caption("Generate relatable LinkedIn-style posts powered by AI")

# Input fields
length = st.selectbox("Select post length", ["Short", "Medium", "Long"])
language = st.selectbox("Select post language", ["English", "Hinglish"])
tone = st.selectbox("Select tone/style", ["Professional", "Relatable", "Funny", "Motivational"])
tag = st.text_input("Topic / Tag", placeholder="e.g., Motivation, Career Growth")

# Generate Post
if st.button("Generate Post"):
    with st.spinner("Crafting your post..."):
        try:
            post, _ = generate_post(length, language, tag, tone)
            st.text_area("Generated Post", value=post, height=300)
            st.session_state.generated_post = post
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Rewrite Feature
if "generated_post" in st.session_state:
    st.markdown("### ✏️ Want to modify the post?")
    rewrite_instruction = st.text_input("Rewrite instruction", placeholder="e.g., make it shorter, sound more confident")
    if st.button("Rewrite Post"):
        with st.spinner("Rewriting your post..."):
            try:
                rewritten_post = rewrite_post(st.session_state.generated_post, rewrite_instruction)
                st.text_area("Rewritten Post", value=rewritten_post, height=300)
            except Exception as e:
                st.error(f"Rewrite failed: {e}")

# Enhance Feature
if "generated_post" in st.session_state:
    if st.button("Enhance with CTA + Hashtags"):
        with st.spinner("Enhancing post..."):
            try:
                enhanced = enhance_post(st.session_state.generated_post)
                st.text_area("Enhanced Post", value=enhanced, height=300)
            except Exception as e:
                st.error(f"Enhancement failed: {e}")


