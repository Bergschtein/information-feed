import streamlit as st
import feedparser

st.set_page_config(page_title="Custom Newsfeed", 
                   page_icon="📰", 
                   layout="wide")

st.title("📰 My Custom Newsfeed")

# --- Define your feeds in categories ---
feeds = {
    "Blogs": {
        "Simon Wilson": "https://simonwillison.net/atom/everything/",
        "Daniel Miessler": "https://danielmiessler.com/feed.rss",
        "Jascha's Blog": "https://sohl-dickstein.github.io/feed.xml",
        "Embrace The Red" : "https://embracethered.com/blog/index.xml"
    },
    "Research (arXiv)": {
        "AI (cs.AI)": "http://export.arxiv.org/rss/cs.AI",
        "Machine Learning (cs.LG)": "http://export.arxiv.org/rss/cs.LG",
        "Statistical ML (stat.ML)": "http://export.arxiv.org/rss/stat.ML",
        "Cryptography and Security (cs.CR)" : "https://export.arxiv.org/rss/cs.CR/"
    },
    "Research Blogs": {
        "DeepMind" : "https://blog.google/technology/google-deepmind/rss/",

    }
}

with st.sidebar:
    st.write("This code will be printed to the sidebar.")


# --- Tabs for categories ---
tabs = st.tabs(list(feeds.keys()))

# --- Loop over categories and show feeds ---
for i, (category, sources) in enumerate(feeds.items()):
    with tabs[i]:
        st.header(category)
        for source_name, url in sources.items():
            st.subheader(source_name)
            feed = feedparser.parse(url)
            col1, col2, col3 = st.columns(3, border=True)
            cols = [col1, col2, col3]         

            
            for i, entry in enumerate(feed.entries[:3]):  # show top 3
                
                with cols[i]:
                    st.markdown(f"### [{entry.title}]({entry.link})")
                    if hasattr(entry, "published"):
                        st.caption(entry.published)
                    # if hasattr(entry, "summary"):
                    #     st.html(entry.summary[:200] + "...")
                # if i == 1: st.write("---")

