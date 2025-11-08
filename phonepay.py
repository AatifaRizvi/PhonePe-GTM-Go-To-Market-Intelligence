import streamlit as st
import pandas as pd
from newsapi import NewsApiClient
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Config
API_KEY = "f86b4d24190b40b2af791c6c2c02262e" 
COMPANY = "PhonePe"
QUERY = COMPANY + " fintech India"
MAX_ARTICLES = 10

# Initialize NewsAPI client
newsapi = NewsApiClient(api_key=API_KEY)

# Fetch latest news

def fetch_news(query, max_articles=10):
    dt_from = (datetime.datetime.utcnow() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    all_articles = newsapi.get_everything(
        q=query,
        from_param=dt_from,
        language='en',
        sort_by='publishedAt',
        page_size=max_articles
    )
    articles = all_articles.get('articles', [])
    rows = []
    for art in articles:
        rows.append({
            "PublishedAt": art.get('publishedAt'),
            "Source": art.get('source', {}).get('name'),
            "Title": art.get('title'),
            "Description": art.get('description'),
            "URL": art.get('url')
        })
    return pd.DataFrame(rows)

# Classify news into GTM categories

def classify_news(df):
    categories = []
    for _, row in df.iterrows():
        text = str(row['Title']) + " " + str(row['Description'])
        text_lower = text.lower()
        if any(k in text_lower for k in ["funding", "ipo", "revenue", "growth", "profit", "loss"]):
            categories.append("Timing / Growth")
        elif any(k in text_lower for k in ["launch", "product", "feature", "payments", "upi", "service"]):
            categories.append("Product / ICP")
        elif any(k in text_lower for k in ["partner", "partnership", "integration"]):
            categories.append("Partnerships")
        elif any(k in text_lower for k in ["compliance", "rbi", "license", "regulation"]):
            categories.append("Compliance")
        elif any(k in text_lower for k in ["fraud", "security", "protect", "safe", "risk"]):
            categories.append("Customer Sentiment / Security")
        elif any(k in text_lower for k in ["brand", "media", "recognition", "award"]):
            categories.append("Brand Power / Messaging")
        elif any(k in text_lower for k in ["cost", "spend", "margin", "efficiency"]):
            categories.append("Ops / Efficiency")
        else:
            categories.append("Other")
    df['Category'] = categories
    return df

# Static GTM signals with Score

data = [
    {"Data Point": "Revenue rose ~40-41% in FY25 to ~₹7,115 crore; loss narrowed to ~₹1,727 crore", "Category": "Timing / Growth", "GTM Insight": "Strong top-line growth & improved margin trend", "GTM Recommendation": "Highlight growth & trust", "Score":5},
    {"Data Point": "Received RBI approval to operate as online payment aggregator", "Category": "Timing / Compliance & Partnerships", "GTM Insight": "Regulatory nod expands capabilities", "GTM Recommendation": "Emphasize aggregator status", "Score":4},
    {"Data Point": "Transitioned to Public Limited entity as part of IPO preparation", "Category": "Timing / Messaging", "GTM Insight": "Pre-IPO posture gives credibility", "GTM Recommendation": "Use messaging for enterprise clients", "Score":4},
    {"Data Point": "Announced ESOP program worth ~₹700-800 crore ahead of IPO", "Category": "Tech & Ops / Hiring & Culture", "GTM Insight": "Strong talent retention", "GTM Recommendation": "Promote culture of innovation", "Score":3},
    {"Data Point": "Plan to bring feature-phone users into UPI ecosystem via GSPay stack", "Category": "Market Trend / Product & ICP", "GTM Insight": "Untapped user base → new segment", "GTM Recommendation": "Target rural/feature-phone markets", "Score":4},
    {"Data Point": "Partnered with SIDBI for digital-first Udyam Assist registration for MSMEs", "Category": "Partnerships / ICP", "GTM Insight": "Push into MSME segment", "GTM Recommendation": "Target MSMEs with full-stack payments", "Score":4},
    {"Data Point": "Launched 'PhonePe Protect' to block payments to flagged fraud numbers", "Category": "Messaging / Product & Customer Sentiment", "GTM Insight": "Builds trust in payment safety", "GTM Recommendation": "Promote security", "Score":3},
    {"Data Point": "India’s UPI transaction limits updated from 15 Sept", "Category": "Market Trend / Compliance", "GTM Insight": "Allows larger transactions via UPI", "GTM Recommendation": "Communicate ease of larger payments", "Score":3},
    {"Data Point": "Over 600+ million registered users and millions of merchants", "Category": "ICP / Growth", "GTM Insight": "Massive reach provides credibility", "GTM Recommendation": "Use user-base stats in pitches", "Score":5},
    {"Data Point": "Core payments still ~85-90% of revenue; non-payments small but growing", "Category": "Product / Growth Strategy", "GTM Insight": "Diversification underway", "GTM Recommendation": "Highlight payments strength", "Score":3},
    {"Data Point": "Advertising/promotional spend decreased (~22% YOY)", "Category": "Ops Efficiency / Messaging", "GTM Insight": "Efficiency improving", "GTM Recommendation": "Emphasize smart spending", "Score":3},
    {"Data Point": "Payment processing charges up ~45% YOY", "Category": "Ops / Threats", "GTM Insight": "Costs rising → margin pressure", "GTM Recommendation": "Emphasize cost efficiency", "Score":2},
    {"Data Point": "Strong competition; UPI market cap regulation", "Category": "Market Trend / Competitive Moves", "GTM Insight": "Regulation + competition", "GTM Recommendation": "Showcase leadership & innovation", "Score":4},
    {"Data Point": "Feature-phone payments expansion", "Category": "ICP / Product Innovation", "GTM Insight": "New growth frontier", "GTM Recommendation": "Campaigns for rural users", "Score":3},
    {"Data Point": "Brand/media recognition due to IPO talks & UPI dominance", "Category": "Messaging / Brand Power", "GTM Insight": "Strong brand builds trust", "GTM Recommendation": "Leverage brand in GTM", "Score":4}
]

df_static = pd.DataFrame(data)

# Map broad categories for cleaner visuals
category_map = {
    "Timing / Growth": "Timing",
    "Timing / Compliance & Partnerships": "Timing",
    "Timing / Messaging": "Timing",
    "Tech & Ops / Hiring & Culture": "Ops",
    "Market Trend / Product & ICP": "Market Trend",
    "Partnerships / ICP": "Partnerships",
    "Messaging / Product & Customer Sentiment": "Messaging",
    "Market Trend / Compliance": "Market Trend",
    "ICP / Growth": "ICP",
    "Product / Growth Strategy": "Product",
    "Ops Efficiency / Messaging": "Ops",
    "Ops / Threats": "Ops",
    "Market Trend / Competitive Moves": "Market Trend",
    "ICP / Product Innovation": "ICP",
    "Messaging / Brand Power": "Messaging"
}
df_static['Broad Category'] = df_static['Category'].map(category_map)

# Streamlit Layout
st.set_page_config(page_title="PhonePe GTM Dashboard", layout="wide")
st.title("PhonePe GTM Intelligence Dashboard")
st.subheader("Fintech Company: PhonePe")
st.markdown("This dashboard shows static GTM signals, live news, and visual comparisons.")

# Live News
if st.button("Fetch & Classify Live News"):
    st.info("Fetching live news…")
    df_live = fetch_news(QUERY, MAX_ARTICLES)
    if not df_live.empty:
        df_live = classify_news(df_live)
        st.success("Fetched and classified live news!")
        st.subheader("Live News Signals (Auto-Classified)")
        st.dataframe(df_live)
    else:
        st.warning("No recent news found.")

# Static GTM Signals Table
st.subheader("Static GTM Signals")
st.dataframe(df_static)

# Plots
# 1. Number of signals per broad category (color-coded)
st.subheader("Number of GTM Signals per Broad Category")
broad_counts = df_static['Broad Category'].value_counts()
fig, ax = plt.subplots(figsize=(4,3))
colors = ['#1f77b4' if x < 4 else '#ff7f0e' for x in broad_counts]
sns.barplot(x=broad_counts.values, y=broad_counts.index, palette=colors, ax=ax)
ax.set_xlabel("Number of Signals")
ax.set_ylabel("Broad Category")
ax.set_title("GTM Signals Distribution by Broad Category")
st.pyplot(fig)

# 2. Average impact per broad category
st.subheader("Average Impact Score per Broad Category")
broad_score = df_static.groupby('Broad Category')['Score'].mean().sort_values(ascending=False)
fig2, ax2 = plt.subplots(figsize=(4,3))
sns.barplot(x=broad_score.values, y=broad_score.index, palette="coolwarm", ax=ax2)
ax2.set_xlabel("Average Impact Score")
ax2.set_ylabel("Broad Category")
ax2.set_title("Average GTM Impact by Broad Category")
st.pyplot(fig2)

# 3. Heatmap of average impact
st.subheader("Heatmap: Average Impact by Broad Category")
pivot = df_static.pivot_table(index='Broad Category', values='Score', aggfunc='mean')
fig3, ax3 = plt.subplots(figsize=(3,3))
sns.heatmap(pivot, annot=True, cmap="YlGnBu", cbar_kws={'label':'Average Score'}, ax=ax3)
st.pyplot(fig3)

# 4. Comparison: Number of Signals vs Average Impact
st.subheader("Comparison: Number of Signals vs Average Impact")
fig4, ax4 = plt.subplots(figsize=(3,7))
ax4.bar(broad_counts.index, broad_counts.values, alpha=0.7, label="Number of Signals", color="#1f77b4")
ax4.plot(broad_score.index, broad_score.values, color='red', marker='o', label="Average Impact")
ax4.set_ylabel("Count / Score")
ax4.set_title("Number of Signals vs Average Impact by Broad Category")
ax4.legend()
plt.xticks(rotation=45, ha='right')
st.pyplot(fig4)

# -------------------------
# GTM Insights Summary
# -------------------------
st.subheader("GTM Insights Summary")

st.markdown("""
### Key Insights:
- **Momentum & Trust Building:** PhonePe shows strong top-line growth (~40% YoY) and a narrowing loss, signaling operational momentum. Leverage this in marketing and partner communications to build trust with merchants, enterprises, and users.
- **Expanding ICP & Product Reach:** Large registered base (~600M users) and MSME partnerships present growth opportunities. Feature-phone inclusion and GSPay integration indicate focus on untapped rural markets.
- **Regulation & Compliance as Advantage:** RBI approvals and UPI compliance provide credibility; emphasizing these strengthens user and partner confidence.
- **Operational Efficiency & Scale:** Decreasing promotional spend and growing core payment revenues reflect cost-efficient operations and potential for sustainable profitability.
- **Brand & Messaging Power:** IPO chatter and media recognition give PhonePe leverage to position itself as a market leader and innovative fintech brand.
- **Competitive Pressures & Market Trends:** The UPI ecosystem is highly competitive, and rising processing costs pose margin risks.

### Noted Flaw in Strategy:
- **Heavy Dependence on Core Payments:** ~85-90% of revenue still comes from core payments; non-payment offerings are small, limiting revenue diversification.  
**Recommendation:** Accelerate development of financial services, lending, insurance, and wealth products to broaden revenue streams and reduce exposure to transaction fees.

### Actionable Recommendations:
1. Promote **regulatory approvals and trust-building initiatives** in GTM messaging.  
2. Target **MSMEs and feature-phone users** aggressively through tailored product offerings.  
3. Highlight **brand credibility** through media campaigns and IPO visibility.  
4. Focus on **product diversification** (wealth, insurance, lending) to complement core payments.  
5. Maintain **operational efficiency** to offset rising processing charges.  
6. Monitor **competitive moves and UPI regulations** to stay ahead of market changes.

### Overall Summary:
This dashboard integrates static GTM signals and live news to provide a **holistic view of PhonePe's go-to-market posture**. Visualizations highlight the most impactful GTM areas, show category-wise strengths and weaknesses, and provide actionable insights for strategy refinement. By addressing the dependency on core payments and leveraging regulatory, operational, and brand advantages, PhonePe can further strengthen its leadership position in India’s fintech ecosystem.
""")

