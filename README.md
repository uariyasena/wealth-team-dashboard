# Wealth Team 2026 Dashboard

Interactive dashboard for tracking the Wealth team's 2026 annual goals, Q1 initiatives, and key business metrics.

## 🎯 Overview

This dashboard provides real-time tracking and visualization of:
- **3 Annual Goals**: New client wins, business enhancements, and distribution partnerships
- **Q1 Initiatives**: 4 key initiatives with editable progress tracking
- **Key Metrics**: Revenue, client counts, pipeline value
- **Analytics**: Interactive charts and insights

## 🚀 Quick Start

### Prerequisites
- Python 3.12 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository** (or download the files)
   ```bash
   git clone <your-repo-url>
   cd "Wealth Enhancment"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the dashboard**
   ```bash
   streamlit run dashboard.py
   ```

4. **Open in browser**
   - The dashboard will automatically open at `http://localhost:8501`
   - If not, navigate to the URL shown in the terminal

## 📊 Features

### Annual Goals Tracking
- **Goal 1**: Win commitments from (2) new Wealth clients
- **Goal 2**: Deliver (5+) Wealth business enhancements at Apex
- **Goal 3**: Form (5+) Wealth product distribution relationships including State Street Investment Management

Each goal displays:
- Current progress vs. target
- Completion percentage
- Status indicator (On Track, At Risk, Behind)
- Detailed breakdown of contributing items

### Q1 Initiatives Management
- 4 key initiatives tracked with editable fields
- Update Progress, Next Steps, and Blockers directly in the dashboard
- Changes auto-save to CSV files
- Last updated timestamp for each initiative

### Key Metrics
- **Total 2026 Revenue**: Year-to-date revenue in thousands
- **Q1 2026 Revenue**: First quarter performance
- **Active Clients**: Unique client count
- **Pipeline Value**: Revenue from new and converting clients

### Interactive Visualizations
- **Revenue Trends**: Monthly trends, client type breakdown, revenue category distribution
- **Business Enhancements**: Status distribution, progress tracking, project details
- **Distribution Partnerships**: Pipeline funnel, top partners, relationship stages

## 📁 Project Structure

```
Wealth Enhancment/
├── data/
│   ├── WealthRevenueTracking.csv           # Revenue data by month/client
│   ├── WealthBusinessEnhancements.csv      # Business enhancement projects
│   ├── WealthDistributionRelationships.csv # Partnership relationships
│   ├── Q1_Initiatives.csv                  # Q1 initiative tracking
│   └── Annual_Goals_Config.csv             # Goal definitions
├── dashboard.py                             # Main Streamlit application
├── data_processor.py                        # Data processing logic
├── requirements.txt                         # Python dependencies
├── .gitignore                              # Git ignore rules
└── README.md                               # This file
```

## 🔄 Updating Data

### Method 1: Edit CSV Files Directly

1. Navigate to the `data/` folder
2. Open any CSV file in Excel or a text editor
3. Make your changes
4. Save the file
5. Refresh the dashboard (click "🔄 Refresh Data" button)

### Method 2: Edit Q1 Initiatives in Dashboard

1. Open the dashboard
2. Scroll to "Q1 2026 Initiatives" section
3. Click on cells in Progress, Next Steps, or Blockers columns
4. Edit the text
5. Changes save automatically

### Data Files

**WealthRevenueTracking.csv**
- Update monthly after revenue close
- Add new rows for new revenue entries
- Required columns: MonthYear, RevenueType, ClientName, ClientType, Revenue_Thousands, etc.

**WealthBusinessEnhancements.csv**
- Update when project status changes
- Mark ActualCompletionDate when projects complete
- Required columns: EnhancementID, ProjectName, Status, ActualCompletionDate, etc.

**WealthDistributionRelationships.csv**
- Update as partnerships progress through stages
- Add Q1/Q2/Q3/Q4 progress notes
- Required columns: RelationshipID, PartnerName, RelationshipStage, Status, etc.

**Q1_Initiatives.csv**
- Best edited directly in dashboard
- Can also edit in Excel if needed
- Required columns: InitiativeID, InitiativeName, Progress, NextSteps, Blockers, LastUpdated

## 🎨 Customization

### Adding New Goals
1. Edit `data/Annual_Goals_Config.csv`
2. Add new row with goal details
3. Update `data_processor.py` with calculation logic
4. Update `dashboard.py` to display the new goal

### Adding New Initiatives
1. Edit `data/Q1_Initiatives.csv`
2. Add new row with initiative details
3. Dashboard will automatically display the new initiative

### Changing Visual Styling
- Edit the `<style>` section in `dashboard.py` (lines 25-65)
- Modify colors, borders, fonts, etc.
- Changes apply immediately on refresh

## 🚢 Deployment

### Option 1: Streamlit Cloud (Recommended)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository, branch (main), and main file (dashboard.py)
   - Click "Deploy"

3. **Share with team**
   - Copy the deployed URL (e.g., `https://your-app.streamlit.app`)
   - Share with team members
   - Anyone with the link can view the dashboard

### Option 2: Local Network

1. **Run with network access**
   ```bash
   streamlit run dashboard.py --server.address=0.0.0.0
   ```

2. **Share local network URL**
   - Find your IP address
   - Share URL: `http://<your-ip>:8501`
   - Team members on same network can access

## 🔧 Troubleshooting

### Dashboard won't load
- Ensure Python 3.12+ is installed: `python --version`
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check that all CSV files exist in `data/` folder

### Data not updating
- Click "🔄 Refresh Data" button in dashboard
- Verify CSV files are saved properly
- Check for data validation warnings at bottom of dashboard

### CSV file errors
- Ensure all required columns are present
- Check for proper date formats (YYYY-MM-DD)
- Verify no special characters in text fields
- Use UTF-8 encoding when saving CSV files

### Git/GitHub issues
- Ensure Git is installed: `git --version`
- Verify GitHub credentials are configured
- Check repository permissions

## 📈 Goal Calculation Logic

### Goal 1: New Clients (Target: 2)
Counts unique clients in 2026 where:
- `NewVsExisting` = "New Client" OR "Pipeline Conversion"

### Goal 2: Business Enhancements (Target: 5)
Counts enhancements where:
- `Status` = "Completed"
- `ActualCompletionDate` starts with "2026"

### Goal 3: Distribution Partnerships (Target: 5)
Counts partnerships where:
- `Status` = "Active"
- `RelationshipStage` = "Partnership Active" OR "Contract Finalization"

## 🤝 Contributing

### Adding Features
1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make changes to code
3. Test locally
4. Commit and push: `git push origin feature/your-feature`
5. Create pull request on GitHub

### Reporting Issues
- Open an issue on GitHub
- Include error messages and screenshots
- Describe steps to reproduce

## 📝 License

Internal use only - Wealth Team Dashboard

## 📧 Support

For questions or support:
- Contact: Wealth Team Leadership
- Documentation: See this README
- Technical Issues: Open GitHub issue

---

**Built with:**
- [Streamlit](https://streamlit.io/) - Dashboard framework
- [Pandas](https://pandas.pydata.org/) - Data processing
- [Plotly](https://plotly.com/) - Interactive visualizations
- Python 3.12

**Last Updated:** March 2026
