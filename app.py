import streamlit as st
import feedparser

st.set_page_config(page_title="Custom Newsfeed", page_icon="📰", layout="wide")
st.title("📰 My Custom Newsfeed")

# --- Define your feeds in categories ---
feeds = {
    "Technical Blogs": {
        "Real Python": "https://realpython.com/atom.xml",
        "Towards Data Science": "https://towardsdatascience.com/feed",
        "KDnuggets": "https://www.kdnuggets.com/feed"
    },
    "Research (arXiv)": {
        "AI (cs.AI)": "http://export.arxiv.org/rss/cs.AI",
        "Machine Learning (cs.LG)": "http://export.arxiv.org/rss/cs.LG",
        "Statistical ML (stat.ML)": "http://export.arxiv.org/rss/stat.ML",
        "DeepMind" : "https://deepmind.google/research/publications/",
    },
    "News": {
        "BBC": "http://feeds.bbci.co.uk/news/rss.xml",
        "Reuters": "http://feeds.reuters.com/reuters/topNews",
        "CNN": "http://rss.cnn.com/rss/edition.rss"
    }
}

# --- Tabs for categories ---
tabs = st.tabs(list(feeds.keys()))

# --- Loop over categories and show feeds ---
for i, (category, sources) in enumerate(feeds.items()):
    with tabs[i]:
        st.header(category)
        for source_name, url in sources.items():
            st.subheader(source_name)
            feed = feedparser.parse(url)

            for entry in feed.entries[:5]:  # show top 5
                st.markdown(f"### [{entry.title}]({entry.link})")
                if hasattr(entry, "published"):
                    st.caption(entry.published)
                if hasattr(entry, "summary"):
                    st.write(entry.summary[:200] + "...")
                st.write("---")
