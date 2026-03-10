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

# Custom CSS styling
st.markdown("""
<style>
    .goal-card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        border-left: 5px solid #1f77b4;
        margin: 10px 0;
    }
    .metric-container {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .status-badge {
        display: inline-block;
        padding: 5px 12px;
        border-radius: 15px;
        font-weight: bold;
        font-size: 0.9em;
    }
    .status-on-track {
        background-color: #d4edda;
        color: #155724;
    }
    .status-at-risk {
        background-color: #fff3cd;
        color: #856404;
    }
    .status-behind {
        background-color: #f8d7da;
        color: #721c24;
    }
    h1 {
        color: #1f77b4;
        border-bottom: 3px solid #1f77b4;
        padding-bottom: 10px;
    }
    h2 {
        color: #2c3e50;
        margin-top: 30px;
    }
    .stDataFrame {
        border: 1px solid #ddd;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.title("📊 Wealth Team 2026 Annual Goals & Q1 Initiatives")
st.markdown(f"**Last Updated:** {datetime.now().strftime('%B %d, %Y at %I:%M %p')}")

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

    # Q1 Initiatives Section
    st.header("🚀 Q1 2026 Initiatives")
    st.markdown("*Edit Progress, Next Steps, and Blockers directly in the table below. Changes auto-save.*")

    # Configure editable columns
    column_config = {
        "InitiativeID": st.column_config.TextColumn("ID", width=80, disabled=True),
        "InitiativeName": st.column_config.TextColumn("Initiative", width=400, disabled=True),
        "Progress": st.column_config.TextColumn("Progress", width=250),
        "NextSteps": st.column_config.TextColumn("Next Steps", width=300),
        "Blockers": st.column_config.TextColumn("Blockers", width=300),
        "LastUpdated": st.column_config.DateColumn("Last Updated", width=120, disabled=True)
    }

    # Editable data editor
    edited_initiatives = st.data_editor(
        initiatives_df,
        column_config=column_config,
        use_container_width=True,
        hide_index=True,
        num_rows="fixed"
    )

    # Auto-save on edit
    if not edited_initiatives.equals(initiatives_df):
        if dp.save_initiatives(edited_initiatives):
            st.success("✅ Initiatives updated successfully!")
            st.cache_data.clear()
        else:
            st.error("❌ Error saving initiatives. Please try again.")

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
        fig_line.update_traces(line_color='#1f77b4', line_width=3)
        fig_line.update_layout(height=400)
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
                color_continuous_scale='Blues'
            )
            fig_bar.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig_bar, use_container_width=True)

        with col2:
            revenue_by_category = revenue_df[revenue_df['Year'] == 2026].groupby('RevenueCategory')['Revenue_Thousands'].sum().reset_index()

            fig_pie = px.pie(
                revenue_by_category,
                values='Revenue_Thousands',
                names='RevenueCategory',
                title='Revenue by Category (2026)',
                color_discrete_sequence=px.colors.sequential.Blues_r
            )
            fig_pie.update_layout(height=400)
            st.plotly_chart(fig_pie, use_container_width=True)

    with tab2:
        st.subheader("Business Enhancements")

        # Enhancements by status
        col1, col2 = st.columns(2)

        with col1:
            status_counts = enhancements_df['Status'].value_counts().reset_index()
            status_counts.columns = ['Status', 'Count']

            fig_donut = px.pie(
                status_counts,
                values='Count',
                names='Status',
                title='Enhancements by Status',
                hole=0.4,
                color_discrete_sequence=px.colors.sequential.RdBu
            )
            fig_donut.update_layout(height=400)
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
                color_continuous_scale='Greens'
            )
            fig_progress.update_layout(height=400, showlegend=False, yaxis={'categoryorder': 'total ascending'})
            st.plotly_chart(fig_progress, use_container_width=True)

        # Enhancement details table
        st.markdown("**All Enhancements:**")
        display_enhancements = enhancements_df[['EnhancementID', 'ProjectName', 'Category', 'Status', 'PercentComplete', 'EstimatedRevenue_Thousands']]
        display_enhancements = display_enhancements.sort_values('PercentComplete', ascending=False)
        st.dataframe(display_enhancements, use_container_width=True, hide_index=True)

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

            fig_funnel = go.Figure(go.Funnel(
                y=stage_counts['Stage'],
                x=stage_counts['Count'],
                textinfo="value+percent initial",
                marker={"color": ["#deebf7", "#c6dbef", "#9ecae1", "#6baed6", "#4292c6", "#2171b5"]}
            ))
            fig_funnel.update_layout(title='Partnership Pipeline Funnel', height=400)
            st.plotly_chart(fig_funnel, use_container_width=True)

        with col2:
            # Top partnerships by revenue estimate
            top_partners = relationships_df.nlargest(5, 'EstimatedAnnualRevenue_Thousands')[
                ['PartnerName', 'EstimatedAnnualRevenue_Thousands']
            ]

            fig_partner_rev = px.bar(
                top_partners,
                x='EstimatedAnnualRevenue_Thousands',
                y='PartnerName',
                orientation='h',
                title='Top 5 Partners by Est. Annual Revenue',
                labels={'EstimatedAnnualRevenue_Thousands': 'Est. Revenue ($K)', 'PartnerName': 'Partner'},
                color='EstimatedAnnualRevenue_Thousands',
                color_continuous_scale='Purples'
            )
            fig_partner_rev.update_layout(height=400, showlegend=False, yaxis={'categoryorder': 'total ascending'})
            st.plotly_chart(fig_partner_rev, use_container_width=True)

        # Partnership details table
        st.markdown("**All Partnerships:**")
        display_partnerships = relationships_df[['RelationshipID', 'PartnerName', 'PartnerType',
                                                 'RelationshipStage', 'Status', 'EstimatedAnnualRevenue_Thousands']]
        display_partnerships = display_partnerships.sort_values('EstimatedAnnualRevenue_Thousands', ascending=False)
        st.dataframe(display_partnerships, use_container_width=True, hide_index=True)

    # Footer
    st.markdown("---")
    st.markdown("*Dashboard powered by Streamlit | Data updated in real-time from CSV files*")

except Exception as e:
    st.error(f"❌ Error loading dashboard: {str(e)}")
    st.info("Please ensure all data files are present in the data/ directory and properly formatted.")
