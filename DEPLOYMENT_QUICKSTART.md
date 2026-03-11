# 🚀 Deployment Quick Start Guide

Get your Wealth Team Dashboard live in 10 minutes!

---

## Prerequisites Check ✅

Before deploying, ensure:
- ✅ Git is installed (`git --version`)
- ✅ GitHub account exists (create at github.com if needed)
- ✅ All code is committed locally (check: `git status`)

---

## Step 1: Create GitHub Repository (2 minutes)

### Option A: GitHub Website (Easiest)

1. Go to https://github.com/new
2. Fill in:
   - **Repository name:** `wealth-team-dashboard`
   - **Description:** "Interactive dashboard for Wealth team 2026 goals"
   - **Visibility:** Select **Public** (required for free Streamlit Cloud)
   - **DO NOT** check "Add README" or ".gitignore" (we have them)
3. Click **"Create repository"**
4. Copy the repository URL shown (looks like: `https://github.com/YOUR_USERNAME/wealth-team-dashboard.git`)

### Option B: GitHub CLI (If you have `gh` installed)

```bash
cd "C:\Users\uariyasena\Projects\Wealth Enhancment"
gh repo create wealth-team-dashboard --public --source=. --remote=origin --push
```

✅ **Done!** Skip to Step 3 if using GitHub CLI.

---

## Step 2: Push Code to GitHub (2 minutes)

Open terminal in the project directory and run these commands:

```bash
cd "C:\Users\uariyasena\Projects\Wealth Enhancment"

# Add GitHub as remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/wealth-team-dashboard.git

# Rename branch to main (GitHub standard)
git branch -M main

# Push all code to GitHub
git push -u origin main
```

**Expected output:**
```
Enumerating objects: XX, done.
Counting objects: 100% (XX/XX), done.
Writing objects: 100% (XX/XX), done.
Total XX (delta X), reused 0 (delta 0)
To https://github.com/YOUR_USERNAME/wealth-team-dashboard.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

✅ **Verify:** Go to `https://github.com/YOUR_USERNAME/wealth-team-dashboard` and see your files!

---

## Step 3: Deploy to Streamlit Cloud (5 minutes)

### 3.1 Sign In to Streamlit Cloud

1. Go to https://share.streamlit.io
2. Click **"Sign in with GitHub"**
3. Authorize Streamlit to access your repositories
4. You'll be redirected to the Streamlit Cloud dashboard

### 3.2 Create New App

1. Click the **"New app"** button (top right)
2. Fill in the deployment form:
   - **Repository:** `YOUR_USERNAME/wealth-team-dashboard`
   - **Branch:** `main`
   - **Main file path:** `dashboard.py`
   - **App URL (optional):** Leave default or customize (e.g., `wealth-team-2026.streamlit.app`)
3. Click **"Deploy!"**

### 3.3 Watch Deployment

- You'll see a live log of the deployment process
- Takes about 2-3 minutes
- Look for these successful steps:
  ```
  ✓ Cloning repository...
  ✓ Installing dependencies...
  ✓ Running dashboard.py...
  ✓ App is live!
  ```

### 3.4 Success!

Once deployed, you'll see:
- **Your dashboard URL:** `https://your-app-name.streamlit.app`
- Live dashboard loaded in browser
- "App is running" status indicator

✅ **Test immediately:**
- Do all 3 goals show correct numbers?
- Can you edit Q1 Initiatives?
- Do all charts load?

---

## Step 4: Share with Team (1 minute)

### Send to Team Members

**Email Template:**
```
Subject: 📊 NEW: Wealth Team 2026 Dashboard is Live!

Hi team,

Our new interactive dashboard for tracking 2026 annual goals and Q1 initiatives is now live!

🔗 Dashboard: https://your-app-name.streamlit.app

Features:
✅ Real-time progress on our 3 annual goals
✅ Editable Q1 initiatives (you can update Progress, Next Steps, Blockers)
✅ Revenue trends and partnership analytics
✅ Beautiful visualizations

No login required - just click and use!

For questions, see the README: https://github.com/YOUR_USERNAME/wealth-team-dashboard

Thanks!
```

### Bookmark It
- Add to team Slack/Teams channel
- Pin to browser favorites
- Add to team wiki/intranet

---

## 🎉 You're Done!

Your dashboard is now:
- ✅ Live on the internet
- ✅ Accessible to your entire team
- ✅ Auto-updating when you push changes
- ✅ Backed by version control

---

## Common Deployment Issues & Fixes

### Issue: "Repository not found"
**Fix:** Ensure repository is **public**, not private (Streamlit Cloud free tier requires public repos)

### Issue: "No module named 'streamlit'"
**Fix:** Check that `requirements.txt` is in the root directory and contains all dependencies

### Issue: "File not found: data/WealthRevenueTracking.csv"
**Fix:** Verify all CSV files are committed and pushed to GitHub

### Issue: "Application error"
**Fix:** Check Streamlit Cloud logs (click "Manage app" → "Logs") for specific error message

### Issue: Changes not appearing
**Fix:**
1. Verify changes are committed and pushed to GitHub
2. Wait 1-2 minutes for auto-redeployment
3. Hard refresh browser (Ctrl+F5)
4. Or manually trigger reboot in Streamlit Cloud settings

---

## Updating the Dashboard After Deployment

### To Update Code
```bash
# Make changes to dashboard.py or other files
git add .
git commit -m "Describe your changes"
git push origin main
# Streamlit Cloud auto-redeploys in 1-2 minutes
```

### To Update Data
```bash
# Edit CSV files in data/ directory
git add data/*.csv
git commit -m "Update [revenue/initiatives/partnerships] data"
git push origin main
# Dashboard updates automatically
```

### To Update Q1 Initiatives (No Git Needed!)
1. Open dashboard in browser
2. Edit cells in Q1 Initiatives table
3. Click outside cell to save
4. Changes persist immediately
5. (Optional) Commit `data/Q1_Initiatives.csv` to Git later

---

## Advanced: Custom Domain (Optional)

Want `dashboard.apex-wealth.com` instead of `your-app.streamlit.app`?

1. Upgrade to Streamlit Teams plan (starts at $250/month)
2. Go to App Settings → Custom Domain
3. Follow DNS configuration instructions
4. Add CNAME record to your domain

**Note:** Not required - the default `.streamlit.app` domain works great!

---

## Need Help?

- **Streamlit Docs:** https://docs.streamlit.io
- **Streamlit Community:** https://discuss.streamlit.io
- **GitHub Issues:** Create issue in your repo
- **README:** See comprehensive guide in `README.md`

---

## 🎯 Quick Reference Commands

### Check Status
```bash
git status
```

### View Logs
```bash
git log --oneline
```

### Update Dashboard
```bash
git add .
git commit -m "Your message"
git push origin main
```

### Run Locally (Testing)
```bash
py -m streamlit run dashboard.py
```

---

**Deployment Status:** ⏳ Pending (follow steps above)
**Once Complete:** 🎉 Dashboard will be live at your Streamlit Cloud URL!

Good luck! 🚀
