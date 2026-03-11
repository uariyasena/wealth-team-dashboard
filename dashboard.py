"""
Wealth Team 2026 Annual Goals & Q1 Initiatives Dashboard

Interactive dashboard for tracking Wealth team progress on annual goals,
Q1 initiatives, and key business metrics.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import data_processor as dp

# Page configuration
st.set_page_config(
    page_title="Wealth Team Dashboard 2026",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apex Fintech Solutions Brand Colors (Blue-dominant palette)
APEX_NAVY = "#003B73"  # Primary brand color - Deep navy blue
APEX_BLUE = "#0090FF"  # Secondary - Bright cyan blue
APEX_PURPLE = "#6B46C1"  # Accent - Purple
APEX_FUCHSIA = "#E91E8C"  # Accent - Fuchsia (used sparingly)
APEX_DARK = "#1F2937"  # Dark text
APEX_GRAY = "#6B7280"  # Medium gray
APEX_LIGHT_BLUE = "#4FC3F7"  # Light blue for highlights

# Custom CSS styling - Apex Fintech branded
st.markdown("""
<style>
    /* Global Styling */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Main container background with subtle gradient */
    .main {
        background: linear-gradient(135deg, #F8F9FB 0%, #FFFFFF 100%);
    }

    /* Goal Cards - Apex branded with blue accent */
    .goal-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8F9FB 100%);
        border-radius: 12px;
        padding: 24px;
        border-left: 5px solid #0090FF;
        margin: 15px 0;
        box-shadow: 0 4px 6px rgba(0, 144, 255, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
    }

    .goal-card:hover {
        box-shadow: 0 10px 15px rgba(0, 144, 255, 0.2), 0 4px 6px rgba(0, 0, 0, 0.1);
        transform: translateY(-2px);
    }

    /* Metric Container - Modern cards */
    .metric-container {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8F9FB 100%);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(74, 144, 226, 0.08), 0 1px 2px rgba(0, 0, 0, 0.06);
        border: 1px solid rgba(74, 144, 226, 0.1);
        transition: all 0.3s ease;
    }

    .metric-container:hover {
        box-shadow: 0 4px 8px rgba(74, 144, 226, 0.12), 0 2px 4px rgba(0, 0, 0, 0.08);
        transform: translateY(-1px);
    }

    /* Status Badges - Apex colors */
    .status-badge {
        display: inline-block;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85em;
        letter-spacing: 0.3px;
    }

    .status-on-track {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%);
        color: #FFFFFF;
        box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);
    }

    .status-at-risk {
        background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
        color: #FFFFFF;
        box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);
    }

    .status-behind {
        background: linear-gradient(135deg, #EF4444 0%, #DC2626 100%);
        color: #FFFFFF;
        box-shadow: 0 2px 4px rgba(239, 68, 68, 0.3);
    }

    /* Headers - Apex blue gradient */
    h1 {
        background: linear-gradient(135deg, #003B73 0%, #0090FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 700;
        border-bottom: 3px solid #0090FF;
        padding-bottom: 12px;
        margin-bottom: 20px;
    }

    h2 {
        color: #1F2937;
        font-weight: 600;
        margin-top: 35px;
        margin-bottom: 20px;
    }

    h3 {
        color: #374151;
        font-weight: 600;
    }

    /* Subheader styling */
    .stSubheader {
        color: #0090FF !important;
        font-weight: 600;
    }

    /* Make sure all text is readable - no white text */
    .stMarkdown, .stText {
        color: #1F2937 !important;
    }

    /* Expander details text */
    details summary {
        color: #1F2937 !important;
    }

    /* Data Editor/Tables */
    .stDataFrame {
        border: 1px solid rgba(0, 144, 255, 0.2);
        border-radius: 8px;
        overflow: hidden;
    }

    /* Dataframe header with blue-black gradient - multiple selectors for compatibility */
    .stDataFrame thead tr th,
    [data-testid="stDataFrameResizable"] thead tr th,
    div[data-testid="stDataFrame"] thead tr th,
    .dataframe thead tr th {
        background: linear-gradient(135deg, #003B73 0%, #000000 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        padding: 12px 16px !important;
        border: none !important;
    }

    /* Dataframe header cells */
    .stDataFrame th,
    [data-testid="stDataFrameResizable"] th,
    div[data-testid="stDataFrame"] th,
    .dataframe th {
        background: linear-gradient(135deg, #003B73 0%, #000000 100%) !important;
        color: white !important;
    }

    /* Dataframe rows */
    .stDataFrame tbody tr,
    [data-testid="stDataFrameResizable"] tbody tr {
        border-bottom: 1px solid rgba(0, 144, 255, 0.1) !important;
    }

    .stDataFrame tbody tr:hover,
    [data-testid="stDataFrameResizable"] tbody tr:hover {
        background-color: rgba(0, 144, 255, 0.05) !important;
    }

    /* Target all table headers globally */
    table thead {
        background: linear-gradient(135deg, #003B73 0%, #000000 100%) !important;
    }

    table thead th {
        background: linear-gradient(135deg, #003B73 0%, #000000 100%) !important;
        color: white !important;
        font-weight: 600 !important;
    }

    table th {
        background: linear-gradient(135deg, #003B73 0%, #000000 100%) !important;
        color: white !important;
    }

    /* Text Areas for Q1 Initiatives */
    .stTextArea textarea {
        border: 2px solid rgba(0, 144, 255, 0.2) !important;
        border-radius: 8px !important;
        padding: 12px !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.9em !important;
        transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
        background-color: white !important;
    }

    .stTextArea textarea:focus {
        border-color: #0090FF !important;
        box-shadow: 0 0 0 3px rgba(0, 144, 255, 0.1) !important;
        outline: none !important;
    }

    .stTextArea textarea:hover {
        border-color: rgba(0, 144, 255, 0.4) !important;
    }

    /* Buttons - Apex cyan blue */
    .stButton > button {
        background: linear-gradient(135deg, #0090FF 0%, #0077CC 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 8px 20px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0, 144, 255, 0.3);
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #0077CC 0%, #005FA3 100%);
        box-shadow: 0 4px 8px rgba(0, 144, 255, 0.4);
        transform: translateY(-1px);
    }

    /* Progress bars - Apex blue gradient */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #0090FF 0%, #6B46C1 100%);
    }

    /* Metrics */
    [data-testid="stMetricValue"] {
        color: #0090FF;
        font-weight: 700;
        font-size: 2em;
    }

    [data-testid="stMetricDelta"] {
        color: #6B7280;
        font-weight: 500;
    }

    /* Tabs - Apex styled */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #F3F4F6;
        border-radius: 10px;
        padding: 4px;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
        color: #6B7280;
        background-color: transparent;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #003B73 0%, #0090FF 100%);
        color: white;
    }

    /* Expander - Styled */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #F8F9FB 0%, #FFFFFF 100%);
        border-radius: 10px;
        border-left: 4px solid #0090FF;
        font-weight: 600;
        color: #1F2937 !important;
        padding: 20px 24px;
        box-shadow: 0 2px 4px rgba(0, 144, 255, 0.08);
        transition: all 0.3s ease;
        font-size: 1.1em;
    }

    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, #E8F4FF 0%, #F8F9FB 100%);
        box-shadow: 0 4px 8px rgba(0, 144, 255, 0.12);
        border-left-color: #003B73;
    }

    /* Expander header text - make sure it's dark and readable */
    .streamlit-expanderHeader p,
    .streamlit-expanderHeader span,
    .streamlit-expanderHeader div {
        color: #1F2937 !important;
        font-size: 1.1em;
        line-height: 1.5;
    }

    /* Make bold text in expander headers even bigger and blue */
    .streamlit-expanderHeader strong {
        color: #003B73 !important;
        font-size: 1.3em !important;
        font-weight: 700 !important;
    }

    /* Expander icon/arrow */
    .streamlit-expanderHeader svg {
        fill: #0090FF !important;
        width: 24px !important;
        height: 24px !important;
    }

    /* Expander content */
    .streamlit-expanderContent {
        padding: 20px;
        background-color: #FAFBFC;
        border-radius: 0 0 10px 10px;
    }

    /* Prevent layout shift and shaking */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Stable containers - no shake on click */
    [data-testid="stVerticalBlock"] {
        gap: 0 !important;
    }

    /* Remove unwanted animations */
    .element-container {
        will-change: auto !important;
    }

    /* Info/Success/Warning boxes for initiatives */
    .stAlert {
        border-radius: 8px;
        border-left-width: 4px;
        padding: 16px;
        margin: 12px 0;
    }

    [data-baseweb="notification"] {
        border-radius: 8px;
    }

    /* Divider */
    hr {
        margin: 2rem 0;
        border: none;
        height: 2px;
        background: linear-gradient(90deg, #0090FF 0%, #6B46C1 50%, transparent 100%);
    }

    /* Sidebar (if used) */
    .css-1d391kg {
        background: linear-gradient(180deg, #1F2937 0%, #374151 100%);
    }

    /* Custom markdown text */
    .markdown-text-container {
        color: #374151;
        line-height: 1.6;
    }

    /* Card hover effects */
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column"] > [data-testid="stVerticalBlock"] {
        transition: all 0.3s ease;
    }

    /* Link colors */
    a {
        color: #0090FF;
        text-decoration: none;
        font-weight: 500;
    }

    a:hover {
        color: #003B73;
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# Header Section with Apex Branding
st.markdown("""
<div style="background: linear-gradient(135deg, #003B73 0%, #0090FF 100%); padding: 30px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0, 144, 255, 0.3);">
    <h1 style="color: white; margin: 0; font-weight: 700; font-size: 2.5em; text-align: center; -webkit-text-fill-color: white;">
        Apex Fintech Solutions
    </h1>
    <p style="color: rgba(255,255,255,0.95); text-align: center; font-size: 1.3em; margin: 10px 0 0 0; font-weight: 500;">
        Wealth Team 2026 Annual Goals & Q1 Initiatives
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="text-align: center; color: {APEX_GRAY}; margin-bottom: 20px; font-size: 0.95em;">
    <strong>Last Updated:</strong> {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
</div>
""", unsafe_allow_html=True)

# Refresh button
col1, col2, col3 = st.columns([1, 1, 8])
with col1:
    if st.button("🔄 Refresh Data"):
        st.cache_data.clear()
        st.rerun()

st.markdown("---")

# Load data
@st.cache_data(ttl=300)  # Cache for 5 minutes
def load_data():
    """Load all data with caching."""
    return dp.load_all_data()

try:
    revenue_df, enhancements_df, relationships_df, initiatives_df, goals_config_df = load_data()

    # Calculate goal progress
    goal_details = dp.get_goal_details(revenue_df, enhancements_df, relationships_df)

    # Annual Goals Section
    st.header("🎯 2026 Annual Goals")

    # Create three columns for goals
    col1, col2, col3 = st.columns(3)

    # Goal 1: New Clients
    with col1:
        st.markdown('<div class="goal-card">', unsafe_allow_html=True)
        st.subheader("Goal 1: New Clients")
        st.markdown("Win commitments from **(2) new Wealth clients**")

        # Progress metric
        g1_current = goal_details['goal1']['current']
        g1_target = goal_details['goal1']['target']
        g1_pct = goal_details['goal1']['percentage']

        st.metric(
            label="Progress",
            value=f"{g1_current} / {g1_target}",
            delta=f"{g1_pct:.0f}% Complete"
        )

        # Progress bar
        st.progress(min(g1_pct / 100, 1.0))

        # Status badge
        if g1_pct >= 100:
            status_html = '<span class="status-badge status-on-track">🟢 Goal Met</span>'
        elif g1_pct >= 50:
            status_html = '<span class="status-badge status-on-track">🟢 On Track</span>'
        elif g1_pct >= 25:
            status_html = '<span class="status-badge status-at-risk">🟡 At Risk</span>'
        else:
            status_html = '<span class="status-badge status-behind">🔴 Behind</span>'
        st.markdown(status_html, unsafe_allow_html=True)

        # Detailed breakdown
        with st.expander("📋 View Details"):
            st.markdown("**New Clients in 2026:**")
            for client in goal_details['goal1']['clients']:
                st.markdown(f"- {client}")

            # Revenue from new clients
            new_client_revenue = revenue_df[
                (revenue_df['Year'] == 2026) &
                (revenue_df['ClientName'].isin(goal_details['goal1']['clients']))
            ]['Revenue_Thousands'].sum()
            st.markdown(f"\n**Total Revenue from New Clients:** ${new_client_revenue:,.0f}K")

        st.markdown('</div>', unsafe_allow_html=True)

    # Goal 2: Business Enhancements
    with col2:
        st.markdown('<div class="goal-card">', unsafe_allow_html=True)
        st.subheader("Goal 2: Enhancements")
        st.markdown("Deliver **(5+) Wealth business enhancements**")

        # Progress metric
        g2_current = goal_details['goal2']['current']
        g2_target = goal_details['goal2']['target']
        g2_pct = goal_details['goal2']['percentage']

        st.metric(
            label="Progress",
            value=f"{g2_current} / {g2_target}",
            delta=f"{g2_pct:.0f}% Complete"
        )

        # Progress bar
        st.progress(min(g2_pct / 100, 1.0))

        # Status badge
        if g2_pct >= 100:
            status_html = '<span class="status-badge status-on-track">🟢 Goal Met</span>'
        elif g2_pct >= 60:
            status_html = '<span class="status-badge status-on-track">🟢 On Track</span>'
        elif g2_pct >= 40:
            status_html = '<span class="status-badge status-at-risk">🟡 At Risk</span>'
        else:
            status_html = '<span class="status-badge status-behind">🔴 Behind</span>'
        st.markdown(status_html, unsafe_allow_html=True)

        # Detailed breakdown
        with st.expander("📋 View Details"):
            st.markdown("**Completed Enhancements in 2026:**")
            for project in goal_details['goal2']['projects']:
                st.markdown(f"- **{project['ProjectName']}** (ID: {project['EnhancementID']})")
                st.markdown(f"  *Completed: {project['ActualCompletionDate']}*")

            # In Progress count
            in_progress = enhancements_df[enhancements_df['Status'] == 'In Progress']
            st.markdown(f"\n**In Progress:** {len(in_progress)} enhancements")

        st.markdown('</div>', unsafe_allow_html=True)

    # Goal 3: Distribution Partnerships
    with col3:
        st.markdown('<div class="goal-card">', unsafe_allow_html=True)
        st.subheader("Goal 3: Partnerships")
        st.markdown("Form **(5+) distribution relationships**")

        # Progress metric
        g3_current = goal_details['goal3']['current']
        g3_target = goal_details['goal3']['target']
        g3_pct = goal_details['goal3']['percentage']

        st.metric(
            label="Progress",
            value=f"{g3_current} / {g3_target}",
            delta=f"{g3_pct:.0f}% Complete"
        )

        # Progress bar
        st.progress(min(g3_pct / 100, 1.0))

        # Status badge
        if g3_pct >= 100:
            status_html = '<span class="status-badge status-on-track">🟢 Goal Met</span>'
        elif g3_pct >= 60:
            status_html = '<span class="status-badge status-on-track">🟢 On Track</span>'
        elif g3_pct >= 40:
            status_html = '<span class="status-badge status-at-risk">🟡 At Risk</span>'
        else:
            status_html = '<span class="status-badge status-behind">🔴 Behind</span>'
        st.markdown(status_html, unsafe_allow_html=True)

        # Detailed breakdown
        with st.expander("📋 View Details"):
            st.markdown("**Active Partnerships:**")
            for partnership in goal_details['goal3']['partnerships']:
                st.markdown(f"- **{partnership['PartnerName']}**")
                st.markdown(f"  *Stage: {partnership['RelationshipStage']}*")

            # SSIM highlight
            ssim = relationships_df[relationships_df['PartnerName'] == 'State Street Investment Management']
            if len(ssim) > 0:
                st.markdown("\n**🌟 State Street Investment Management:** Included ✓")

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Q1 Initiatives Section - Beautiful Expandable Cards with Edit Capability
    st.header("🚀 Q1 2026 Initiatives")

    st.markdown("""
    <div style="background: linear-gradient(135deg, #E8F4FF 0%, #FFFFFF 100%);
                padding: 16px;
                border-radius: 10px;
                border-left: 4px solid #0090FF;
                margin-bottom: 20px;">
        <p style="color: #1F2937; margin: 0; font-size: 0.95em;">
            <strong>Instructions:</strong> Expand any initiative to view details. Edit the text fields and click "Save Changes" to update.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Initiative descriptions
    initiative_descriptions = {
        'INIT001': 'Advance State Street and Mercury Broker Dealer project efforts and finalize pending contractual agreements',
        'INIT002': 'Work across Apex to scope, document, resource, and implement Wealth business enhancements including Non-Purpose Loans, Monthly Confirm Report, RIA Trade Away, Apex Advisory solution set and Schedule A updates',
        'INIT003': 'Continued focus on all State Street related initiatives and opportunities',
        'INIT004': 'Negotiate and finalize agreements with State Street Investment Management and Capital Group, develop pipeline of additional distribution opportunities'
    }

    # Display initiatives in beautiful expandable cards with edit capability
    for idx, row in initiatives_df.iterrows():
        initiative_id = row['InitiativeID']
        initiative_desc = initiative_descriptions.get(initiative_id, row['InitiativeName'])

        # Create prominent header with large initiative ID
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #E8F4FF 0%, #FFFFFF 100%);
                    border-radius: 12px 12px 0 0;
                    padding: 20px 24px;
                    border-left: 5px solid #0090FF;
                    margin-top: 20px;">
            <h2 style="margin: 0; color: #003B73; font-size: 1.8em; font-weight: 700;">
                {initiative_id}
            </h2>
            <p style="margin: 8px 0 0 0; color: #1F2937; font-size: 1.05em; line-height: 1.5;">
                {initiative_desc}
            </p>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("📋 View Details", expanded=False):
            st.markdown(f"<p style='color: #6B7280; font-size: 0.9em;'><em>Last updated: {row['LastUpdated']}</em></p>", unsafe_allow_html=True)
            st.markdown("---")

            # Progress section
            st.markdown("### 📊 Current Progress")
            st.markdown(f"""
            <div style="background-color: #E8F4FF; border-left: 4px solid #0090FF; padding: 16px; border-radius: 8px; margin: 10px 0;">
                <p style="color: #1F2937; margin: 0; line-height: 1.6;">{row['Progress']}</p>
            </div>
            """, unsafe_allow_html=True)

            # Next Steps section
            st.markdown("### ⏭️ Next Steps")
            st.markdown(f"""
            <div style="background-color: #D1FAE5; border-left: 4px solid #10B981; padding: 16px; border-radius: 8px; margin: 10px 0;">
                <p style="color: #1F2937; margin: 0; line-height: 1.6;">{row['NextSteps']}</p>
            </div>
            """, unsafe_allow_html=True)

            # Blockers section
            st.markdown("### 🚧 Blockers & Risks")
            if row['Blockers'] and str(row['Blockers']).strip():
                st.markdown(f"""
                <div style="background-color: #FEF3C7; border-left: 4px solid #F59E0B; padding: 16px; border-radius: 8px; margin: 10px 0;">
                    <p style="color: #1F2937; margin: 0; line-height: 1.6;">{row['Blockers']}</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background-color: #D1FAE5; border-left: 4px solid #10B981; padding: 16px; border-radius: 8px; margin: 10px 0;">
                    <p style="color: #1F2937; margin: 0; line-height: 1.6;">No blockers identified</p>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("---")

    # Key Metrics Section
    st.header("📈 Key Metrics")

    metrics = dp.get_key_metrics(revenue_df)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric(
            label="Total 2026 Revenue",
            value=f"${metrics['total_revenue_2026']:,.0f}K",
            delta="Year-to-Date"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric(
            label="Q1 2026 Revenue",
            value=f"${metrics['q1_revenue_2026']:,.0f}K",
            delta="First Quarter"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric(
            label="Active Clients",
            value=f"{metrics['active_clients_2026']}",
            delta="2026 YTD"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric(
            label="Pipeline Value",
            value=f"${metrics['pipeline_value']:,.0f}K",
            delta="New & Converting"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Visualizations Section
    st.header("📊 Analytics & Insights")

    tab1, tab2, tab3 = st.tabs(["💰 Revenue Trends", "🔧 Business Enhancements", "🤝 Distribution Partnerships"])

    with tab1:
        st.subheader("Revenue Trends")

        # Monthly revenue trend
        monthly_revenue = revenue_df[revenue_df['Year'] == 2026].groupby('MonthYear')['Revenue_Thousands'].sum().reset_index()
        monthly_revenue = monthly_revenue.sort_values('MonthYear')

        fig_line = px.line(
            monthly_revenue,
            x='MonthYear',
            y='Revenue_Thousands',
            title='Monthly Revenue Trend (2026)',
            labels={'MonthYear': 'Month', 'Revenue_Thousands': 'Revenue ($K)'},
            markers=True
        )
        fig_line.update_traces(
            line_color=APEX_BLUE,
            line_width=4,
            marker=dict(size=10, color=APEX_BLUE, line=dict(color='white', width=2))
        )
        fig_line.update_layout(
            height=400,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Inter', color='#1F2937', size=12),
            title_font=dict(size=18, color='#1F2937', family='Inter'),
            xaxis=dict(
                showgrid=True,
                gridcolor='rgba(0,0,0,0.05)',
                title_font=dict(color='#1F2937', size=14),
                tickfont=dict(color='#1F2937', size=12)
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgba(0,0,0,0.05)',
                title_font=dict(color='#1F2937', size=14),
                tickfont=dict(color='#1F2937', size=12)
            ),
            legend=dict(
                font=dict(color='#1F2937', size=12)
            )
        )
        st.plotly_chart(fig_line, use_container_width=True)

        # Revenue by client type
        col1, col2 = st.columns(2)

        with col1:
            revenue_by_type = revenue_df[revenue_df['Year'] == 2026].groupby('ClientType')['Revenue_Thousands'].sum().reset_index()
            revenue_by_type = revenue_by_type.sort_values('Revenue_Thousands', ascending=False)

            fig_bar = px.bar(
                revenue_by_type,
                x='ClientType',
                y='Revenue_Thousands',
                title='Revenue by Client Type (2026)',
                labels={'ClientType': 'Client Type', 'Revenue_Thousands': 'Revenue ($K)'},
                color='Revenue_Thousands',
                color_continuous_scale=[[0, '#B3E5FC'], [0.5, '#0090FF'], [1, '#003B73']]
            )
            fig_bar.update_layout(
                height=400,
                showlegend=False,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family='Inter', color='#1F2937', size=12),
                title_font=dict(size=18, color='#1F2937', family='Inter'),
                xaxis=dict(
                    showgrid=False,
                    title_font=dict(color='#1F2937', size=14),
                    tickfont=dict(color='#1F2937', size=12)
                ),
                yaxis=dict(
                    showgrid=True,
                    gridcolor='rgba(0,0,0,0.1)',
                    title_font=dict(color='#1F2937', size=14, family='Inter'),
                    tickfont=dict(color='#1F2937', size=16, family='Inter')
                ),
                coloraxis=dict(
                    colorbar=dict(
                        title=dict(
                            text="Revenue ($K)",
                            font=dict(color='#1F2937', size=12, family='Inter')
                        ),
                        tickfont=dict(color='#1F2937', size=12, family='Inter'),
                        tickcolor='#1F2937',
                        outlinecolor='#1F2937',
                        outlinewidth=1
                    )
                )
            )
            # Make Y-axis tick labels darker and more visible
            fig_bar.update_yaxes(tickcolor='#1F2937', tickwidth=2, ticklen=8)
            st.plotly_chart(fig_bar, use_container_width=True)

        with col2:
            revenue_by_category = revenue_df[revenue_df['Year'] == 2026].groupby('RevenueCategory')['Revenue_Thousands'].sum().reset_index()

            # Apex branded color palette for pie chart - blue dominant with fuchsia accent
            apex_colors = ['#0090FF', '#003B73', '#6B46C1', '#4FC3F7', '#E91E8C']

            fig_pie = px.pie(
                revenue_by_category,
                values='Revenue_Thousands',
                names='RevenueCategory',
                title='Revenue by Category (2026)',
                color_discrete_sequence=apex_colors
            )
            fig_pie.update_layout(
                height=400,
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family='Inter', color='#1F2937', size=12),
                title_font=dict(size=18, color='#1F2937', family='Inter'),
                legend=dict(
                    font=dict(color='#1F2937', size=12)
                )
            )
            fig_pie.update_traces(
                textfont=dict(size=14, family='Inter', color='white'),
                marker=dict(line=dict(color='white', width=2)),
                textposition='inside'
            )
            st.plotly_chart(fig_pie, use_container_width=True)

    with tab2:
        st.subheader("Business Enhancements")

        # Enhancements by status
        col1, col2 = st.columns(2)

        with col1:
            status_counts = enhancements_df['Status'].value_counts().reset_index()
            status_counts.columns = ['Status', 'Count']

            # Status colors: Completed, In Progress, Planning
            status_colors = {'Completed': '#10B981', 'In Progress': '#0090FF', 'Planning': '#6B46C1'}

            fig_donut = px.pie(
                status_counts,
                values='Count',
                names='Status',
                title='Enhancements by Status',
                hole=0.45,
                color='Status',
                color_discrete_map=status_colors
            )
            fig_donut.update_layout(
                height=400,
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family='Inter', color='#1F2937', size=12),
                title_font=dict(size=18, color='#1F2937', family='Inter'),
                legend=dict(
                    font=dict(color='#1F2937', size=12)
                )
            )
            fig_donut.update_traces(
                textfont=dict(size=13, family='Inter', color='#1F2937'),
                marker=dict(line=dict(color='white', width=2))
            )
            st.plotly_chart(fig_donut, use_container_width=True)

        with col2:
            # Top enhancements by progress
            top_enhancements = enhancements_df.nlargest(5, 'PercentComplete')[['ProjectName', 'PercentComplete']]

            fig_progress = px.bar(
                top_enhancements,
                x='PercentComplete',
                y='ProjectName',
                orientation='h',
                title='Top 5 Enhancements by % Complete',
                labels={'PercentComplete': 'Percent Complete', 'ProjectName': 'Project'},
                color='PercentComplete',
                color_continuous_scale=[[0, '#B3E5FC'], [0.5, '#0090FF'], [1, '#10B981']]
            )
            fig_progress.update_layout(
                height=400,
                showlegend=False,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family='Inter', color='#1F2937', size=12),
                title_font=dict(size=18, color='#1F2937', family='Inter'),
                xaxis=dict(
                    showgrid=True,
                    gridcolor='rgba(0,0,0,0.05)',
                    title_font=dict(color='#1F2937', size=14),
                    tickfont=dict(color='#1F2937', size=12)
                ),
                yaxis=dict(
                    categoryorder='total ascending',
                    showgrid=False,
                    title_font=dict(color='#1F2937', size=14),
                    tickfont=dict(color='#1F2937', size=11)
                )
            )
            st.plotly_chart(fig_progress, use_container_width=True)

        # Interactive Project Cards
        st.markdown("### 🎯 All Enhancement Projects")

        # Sort by status priority and percent complete
        status_order = {'Completed': 0, 'In Progress': 1, 'Planning': 2}
        display_enhancements = enhancements_df.copy()
        display_enhancements['status_order'] = display_enhancements['Status'].map(status_order)
        display_enhancements = display_enhancements.sort_values(['status_order', 'PercentComplete'], ascending=[True, False])

        # Create 2-column grid layout
        cols_per_row = 2
        for i in range(0, len(display_enhancements), cols_per_row):
            cols = st.columns(cols_per_row)
            for j in range(cols_per_row):
                if i + j < len(display_enhancements):
                    project = display_enhancements.iloc[i + j]
                    with cols[j]:
                        # Determine status color and styling
                        if project['Status'] == 'Completed':
                            border_color = '#10B981'
                            bg_color = '#D1FAE5'
                            status_icon = '✅'
                            status_badge = 'Completed'
                        elif project['Status'] == 'In Progress':
                            border_color = '#0090FF'
                            bg_color = '#E8F4FF'
                            status_icon = '🔄'
                            status_badge = 'In Progress'
                        else:
                            border_color = '#6B46C1'
                            bg_color = '#EDE9FE'
                            status_icon = '📋'
                            status_badge = 'Planning'

                        # Priority badge
                        if project['Priority'] == 'Critical':
                            priority_badge = '🔥 Critical'
                            priority_color = '#DC2626'
                        elif project['Priority'] == 'High':
                            priority_badge = '⚡ High'
                            priority_color = '#F59E0B'
                        else:
                            priority_badge = '📌 Medium'
                            priority_color = '#6B7280'

                        # Card HTML
                        card_html = f"""
                        <div style="background: {bg_color}; border-left: 6px solid {border_color}; border-radius: 12px; padding: 20px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 280px;">
                            <div style="display: flex; justify-content: space-between; margin-bottom: 12px;">
                                <span style="font-size: 1.5em;">{status_icon}</span>
                                <span style="color: #6B7280; font-size: 0.85em; font-weight: 600;">{project['EnhancementID']}</span>
                            </div>
                            <h4 style="color: #1F2937; margin: 0 0 12px 0; font-size: 1.1em; font-weight: 700;">{project['ProjectName']}</h4>
                            <div style="margin-bottom: 16px;">
                                <span style="background: {border_color}; color: white; padding: 4px 12px; border-radius: 12px; font-size: 0.75em; font-weight: 600; margin-right: 8px;">{status_badge}</span>
                                <span style="background: {priority_color}; color: white; padding: 4px 12px; border-radius: 12px; font-size: 0.75em; font-weight: 600; margin-right: 8px;">{priority_badge}</span>
                                <span style="background: #E5E7EB; color: #374151; padding: 4px 12px; border-radius: 12px; font-size: 0.75em; font-weight: 600;">{project['Category']}</span>
                            </div>
                            <div style="margin-top: 40px;">
                                <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                                    <span style="color: #6B7280; font-size: 0.85em; font-weight: 600;">Progress</span>
                                    <span style="color: {border_color}; font-size: 1.1em; font-weight: 700;">{int(project['PercentComplete'])}%</span>
                                </div>
                                <div style="background: rgba(0,0,0,0.1); border-radius: 10px; height: 12px; overflow: hidden;">
                                    <div style="background: {border_color}; width: {project['PercentComplete']}%; height: 100%; border-radius: 10px;"></div>
                                </div>
                            </div>
                            <div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid rgba(0,0,0,0.1);">
                                <div style="display: flex; justify-content: space-between;">
                                    <span style="color: #6B7280; font-size: 0.85em;">Est. Revenue</span>
                                    <span style="color: #1F2937; font-size: 0.95em; font-weight: 700;">${int(project['EstimatedRevenue_Thousands'])}K</span>
                                </div>
                            </div>
                        </div>
                        """
                        st.markdown(card_html, unsafe_allow_html=True)

    with tab3:
        st.subheader("Distribution Partnerships")

        # Partnerships by stage (funnel)
        col1, col2 = st.columns(2)

        with col1:
            stage_counts = relationships_df['RelationshipStage'].value_counts().reset_index()
            stage_counts.columns = ['Stage', 'Count']

            # Order stages logically
            stage_order = ['Discovery', 'Proposal Stage', 'Negotiation', 'Integration Testing',
                         'Contract Finalization', 'Partnership Active']
            stage_counts['Stage'] = pd.Categorical(stage_counts['Stage'], categories=stage_order, ordered=True)
            stage_counts = stage_counts.sort_values('Stage')

            # Apex gradient colors for funnel stages - blue dominant with purple/fuchsia accent
            funnel_colors = ['#B3E5FC', '#4FC3F7', '#0090FF', '#003B73', '#6B46C1', '#E91E8C']

            fig_funnel = go.Figure(go.Funnel(
                y=stage_counts['Stage'],
                x=stage_counts['Count'],
                textinfo="value+percent initial",
                marker={
                    "color": funnel_colors[:len(stage_counts)],
                    "line": {"color": "white", "width": 2}
                },
                textfont={"size": 13, "family": "Inter", "color": "white"}
            ))
            fig_funnel.update_layout(
                title='Partnership Pipeline Funnel',
                height=400,
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(family='Inter', color='#1F2937', size=12),
                title_font=dict(size=18, color='#1F2937', family='Inter'),
                yaxis=dict(
                    title_font=dict(color='#1F2937', size=14),
                    tickfont=dict(color='#1F2937', size=12)
                )
            )
            st.plotly_chart(fig_funnel, use_container_width=True)

        with col2:
            # Top partnerships by revenue estimate
            top_partners = relationships_df.nlargest(5, 'EstimatedAnnualRevenue_Thousands')[
                ['PartnerName', 'EstimatedAnnualRevenue_Thousands']
            ]
            # Sort for better display
            top_partners = top_partners.sort_values('EstimatedAnnualRevenue_Thousands', ascending=True)

            fig_partner_rev = px.bar(
                top_partners,
                x='PartnerName',
                y='EstimatedAnnualRevenue_Thousands',
                title='Top 5 Partners by Est. Annual Revenue',
                labels={'EstimatedAnnualRevenue_Thousands': 'Est. Revenue ($K)', 'PartnerName': 'Partner'},
                color='EstimatedAnnualRevenue_Thousands',
                color_continuous_scale=[[0, '#B8A3E8'], [0.5, '#6B46C1'], [1, '#003B73']]
            )
            fig_partner_rev.update_layout(
                height=400,
                showlegend=False,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family='Inter', color='#1F2937', size=12),
                title_font=dict(size=18, color='#1F2937', family='Inter'),
                xaxis=dict(
                    showgrid=False,
                    title_font=dict(color='#1F2937', size=14),
                    tickfont=dict(color='#1F2937', size=11),
                    tickangle=-45
                ),
                yaxis=dict(
                    showgrid=True,
                    gridcolor='rgba(0,0,0,0.05)',
                    title_font=dict(color='#1F2937', size=14),
                    tickfont=dict(color='#1F2937', size=12)
                )
            )
            st.plotly_chart(fig_partner_rev, use_container_width=True)

        # Partnership details table with gradient header
        st.markdown("#### All Partnerships")

        display_partnerships = relationships_df[['RelationshipID', 'PartnerName', 'PartnerType',
                                                 'RelationshipStage', 'Status', 'EstimatedAnnualRevenue_Thousands']]
        display_partnerships = display_partnerships.sort_values('EstimatedAnnualRevenue_Thousands', ascending=False)

        st.dataframe(
            display_partnerships,
            use_container_width=True,
            hide_index=True,
            column_config={
                'RelationshipID': st.column_config.TextColumn('Relationship ID', width='small'),
                'PartnerName': st.column_config.TextColumn('Partner Name', width='medium'),
                'PartnerType': st.column_config.TextColumn('Partner Type', width='small'),
                'RelationshipStage': st.column_config.TextColumn('Relationship Stage', width='medium'),
                'Status': st.column_config.TextColumn('Status', width='small'),
                'EstimatedAnnualRevenue_Thousands': st.column_config.NumberColumn('Est. Revenue ($K)', format='%d')
            }
        )

    # Footer - Apex branded
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 30px 0; margin-top: 40px;">
        <div style="background: linear-gradient(135deg, #F8F9FB 0%, #FFFFFF 100%); padding: 25px; border-radius: 12px; border-top: 3px solid #0090FF; box-shadow: 0 -2px 10px rgba(0,0,0,0.05);">
            <p style="color: #1F2937; font-size: 1.1em; font-weight: 600; margin: 0 0 8px 0;">
                <span style="background: linear-gradient(135deg, #003B73 0%, #0090FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
                    Apex Fintech Solutions
                </span> | Wealth Team Dashboard
            </p>
            <p style="color: #6B7280; font-size: 0.9em; margin: 0;">
                Powered by Streamlit • Real-time data updates • Cloud-native infrastructure
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

except Exception as e:
    st.error(f"❌ Error loading dashboard: {str(e)}")
    st.info("Please ensure all data files are present in the data/ directory and properly formatted.")
