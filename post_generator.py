# post_generator.py
from llm_helper import llm
from few_shot import FEW_SHOT_EXAMPLES

def generate_post(length: str, language: str, tag: str, tone: str) -> tuple[str, str]:

    prompt = f"""
You are a professional LinkedIn influencer. 
Generate a post that is:
- Emotionally engaging
- Written in {language}
- About: {tag}
- Length: {length}

Example Posts:
{FEW_SHOT_EXAMPLES}

Begin your new post now:
"""

    response = llm.invoke(prompt)
    text = response.content.strip()

    # Prompt for image generation
    image_prompt = f"Professional, LinkedIn-style image representing '{tag}' in {language}. Minimalist, motivational, and clean design."

    return text, image_prompt


def rewrite_post(original: str, instruction: str) -> str:
    prompt = f"""
You are a helpful LinkedIn editor. Rewrite the post below with this instruction: "{instruction}"

Original Post:
{original}

Rewritten Post:
"""
    response = llm.invoke(prompt)
    return response.content.strip()



def enhance_post(post: str) -> str:
    prompt = f"""
Improve the following LinkedIn post by:
- Adding a call-to-action (CTA) at the end (like "What do you think?")
- Adding 3–5 relevant hashtags at the end

Here’s the post:
{post}

Enhanced Version:
"""
    response = llm.invoke(prompt)
    return response.content.strip()
