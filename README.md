**PhonePe GTM Intelligence Platform**
🚀 Turning market signals into actionable GTM intelligence.

**Author**
Aatifa Rizvi

**Project Overview**
**Problem Statement – GTM Intelligence for Fintech**

Fintech companies operate in dynamic environments where market timing, compliance, and user trust are crucial.
However, identifying actionable Go-To-Market (GTM) signals from scattered data sources remains a major challenge.

**Challenge**:
How can we transform market updates, funding signals, and regulatory changes into real-time GTM insights that guide business strategy?

**Our Solution** – PhonePe GTM Intelligence Dashboard

PhonePe GTM Intelligence Platform is a Streamlit-based data intelligence prototype that aggregates, classifies, and visualizes key GTM signals for the fintech giant PhonePe.
It transforms raw data points into insights for strategic decision-making — focusing on timing, messaging, compliance, and customer segments.

**Live Prototype**

🔗 GitHub Repository:
👉 https://github.com/AatifaRizvi/PhonePe-GTM-Dashboard

Interactive Streamlit dashboard with GTM signal visualization and live news integration.

**Key Features**
 Feature                                     Description
--------------------------                  -------------------------------------------------------------------
 GTM Signal Dashboard               	      Displays 10–15 key PhonePe signals categorized by Timing, Compliance,                                             ICP, etc.
 -------------------------                  --------------------------------------------------------------------
 Live News Integration                      Fetches and classifies real-time news via NewsAPI.
 -------------------------                  --------------------------------------------------------------------
 Category Insights	                        Calculates average impact score and trends by GTM type.
 -------------------------                  --------------------------------------------------------------------   Interactive Charts                        	Includes bar charts, pie charts, and heatmaps for better                                                          visualization.
--------------------------                  ---------------------------------------------------------------------
Actionable Recommendations                  Provides strategic takeaways for PhonePe’s future GTM approach.


**Tech Stack**
Frontend : Streamlit
Backend / Logic : Python (pandas, matplotlib, seaborn)
Data : Static GTM Dataset + Live News API
Deployment: Streamlit Cloud / Local
API : APIsNewsAPI (for real-time news updates)

Run Locally
# Clone this repository
git clone https://github.com/AatifaRizvi/PhonePe-GTM-Dashboard.git
cd PhonePe-GTM-Dashboard

# Create virtual environment
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_dashboard.py

Then open 👉 http://localhost:8501 in your browser!

**GTM Insights Summary**

Momentum & Trust: PhonePe’s ~40% YoY revenue growth and narrowing losses strengthen brand equity.
Regulatory Strength: RBI approval for online payment aggregation adds compliance advantage.
User-Centric ICP: Expanding into rural and MSME markets increases inclusivity.
Innovation Edge: Transition to Public Limited entity positions PhonePe for IPO readiness.

**Real-Life Flaw**: Overdependence on UPI-based transactions (≈85–90% revenue) — a risk if regulations or competition shift.

**Recommendation**: Diversify through lending, insurance, and wealth-tech verticals for sustainable profitability.

**Impactful Outcome**
The dashboard helps GTM strategists quickly identify:
-> Which market moves matter most
-> Where PhonePe’s strengths and weaknesses lie
-> How to adapt future GTM plans in real time

**Future Enhancements**

-> Automated news scraping for real-time GTM signal updates.
-> Sentiment analysis to classify tone (positive/neutral/negative).
-> AI-driven insight generation for each signal.
-> Cloud deployment with dashboard analytics history.

 Development Journey
- Built as part of Wavess 2.0 GTM Challenge (2025).
- Designed, coded, and tested with a focus on real-world fintech strategy and market readiness.

**License**
--This project is licensed under the MIT License.
See the LICENSE file for details.


