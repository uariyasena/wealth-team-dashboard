"""
Data processing module for Wealth Team Dashboard.
Handles loading, processing, and saving of all CSV data files.
"""

import pandas as pd
import os
from datetime import datetime

# Base path for data files
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_PATH, "data")


def load_all_data():
    """
    Load all CSV data files from the data directory.

    Returns:
        tuple: (revenue_df, enhancements_df, relationships_df, initiatives_df, goals_config_df)
    """
    try:
        revenue_df = pd.read_csv(os.path.join(DATA_DIR, "WealthRevenueTracking.csv"))
        enhancements_df = pd.read_csv(os.path.join(DATA_DIR, "WealthBusinessEnhancements.csv"))
        relationships_df = pd.read_csv(os.path.join(DATA_DIR, "WealthDistributionRelationships.csv"))
        initiatives_df = pd.read_csv(os.path.join(DATA_DIR, "Q1_Initiatives.csv"))
        goals_config_df = pd.read_csv(os.path.join(DATA_DIR, "Annual_Goals_Config.csv"))

        return revenue_df, enhancements_df, relationships_df, initiatives_df, goals_config_df
    except Exception as e:
        raise Exception(f"Error loading data files: {str(e)}")


def calculate_goal_1_progress(revenue_df):
    """
    Calculate Goal 1 progress: New client wins in 2026.

    Args:
        revenue_df: Revenue tracking DataFrame

    Returns:
        tuple: (current_count, target_count, new_clients_list)
    """
    target = 2

    # Filter for 2026 new clients (Pipeline Conversion or New Client)
    new_clients_2026 = revenue_df[
        (revenue_df['Year'] == 2026) &
        (revenue_df['NewVsExisting'].isin(['New Client', 'Pipeline Conversion']))
    ]['ClientName'].unique()

    current = len(new_clients_2026)

    return current, target, list(new_clients_2026)


def calculate_goal_2_progress(enhancements_df):
    """
    Calculate Goal 2 progress: Completed business enhancements in 2026.

    Args:
        enhancements_df: Business enhancements DataFrame

    Returns:
        tuple: (current_count, target_count, completed_projects_list)
    """
    target = 5

    # Filter for completed enhancements with 2026 completion dates
    completed_2026 = enhancements_df[
        (enhancements_df['Status'] == 'Completed') &
        (enhancements_df['ActualCompletionDate'].notna()) &
        (enhancements_df['ActualCompletionDate'].astype(str).str.startswith('2026'))
    ]

    current = len(completed_2026)
    projects_list = completed_2026[['EnhancementID', 'ProjectName', 'ActualCompletionDate']].to_dict('records')

    return current, target, projects_list


def calculate_goal_3_progress(relationships_df):
    """
    Calculate Goal 3 progress: Active distribution partnerships.

    Args:
        relationships_df: Distribution relationships DataFrame

    Returns:
        tuple: (current_count, target_count, partnerships_list)
    """
    target = 5

    # Filter for active partnerships (Partnership Active or Contract Finalization stages)
    active_partnerships = relationships_df[
        (relationships_df['Status'] == 'Active') &
        (relationships_df['RelationshipStage'].isin(['Partnership Active', 'Contract Finalization']))
    ]

    current = len(active_partnerships)
    partnerships_list = active_partnerships[['RelationshipID', 'PartnerName', 'RelationshipStage']].to_dict('records')

    return current, target, partnerships_list


def save_initiatives(initiatives_df):
    """
    Save Q1 initiatives DataFrame back to CSV with timestamp update.

    Args:
        initiatives_df: Updated initiatives DataFrame

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Update LastUpdated timestamp
        initiatives_df['LastUpdated'] = datetime.now().strftime('%Y-%m-%d')

        # Save to CSV
        initiatives_df.to_csv(os.path.join(DATA_DIR, "Q1_Initiatives.csv"), index=False)
        return True
    except Exception as e:
        print(f"Error saving initiatives: {str(e)}")
        return False


def get_key_metrics(revenue_df):
    """
    Calculate key metrics for the dashboard.

    Args:
        revenue_df: Revenue tracking DataFrame

    Returns:
        dict: Dictionary containing key metrics
    """
    # Total 2026 revenue
    total_revenue_2026 = revenue_df[revenue_df['Year'] == 2026]['Revenue_Thousands'].sum()

    # Q1 2026 revenue
    q1_revenue_2026 = revenue_df[
        (revenue_df['Year'] == 2026) & (revenue_df['Quarter'] == 'Q1')
    ]['Revenue_Thousands'].sum()

    # Active clients in 2026
    active_clients_2026 = revenue_df[revenue_df['Year'] == 2026]['ClientName'].nunique()

    # Pipeline value (assuming clients with NewVsExisting containing 'Pipeline' or 'New')
    pipeline_clients = revenue_df[
        (revenue_df['Year'] == 2026) &
        (revenue_df['NewVsExisting'].str.contains('Pipeline|New', case=False, na=False))
    ]
    pipeline_value = pipeline_clients['Revenue_Thousands'].sum()

    return {
        'total_revenue_2026': total_revenue_2026,
        'q1_revenue_2026': q1_revenue_2026,
        'active_clients_2026': active_clients_2026,
        'pipeline_value': pipeline_value
    }


def get_goal_details(revenue_df, enhancements_df, relationships_df):
    """
    Get detailed breakdown for each goal.

    Args:
        revenue_df: Revenue tracking DataFrame
        enhancements_df: Business enhancements DataFrame
        relationships_df: Distribution relationships DataFrame

    Returns:
        dict: Detailed information for each goal
    """
    # Goal 1 details
    goal1_current, goal1_target, goal1_clients = calculate_goal_1_progress(revenue_df)

    # Goal 2 details
    goal2_current, goal2_target, goal2_projects = calculate_goal_2_progress(enhancements_df)

    # Goal 3 details
    goal3_current, goal3_target, goal3_partnerships = calculate_goal_3_progress(relationships_df)

    return {
        'goal1': {
            'current': goal1_current,
            'target': goal1_target,
            'clients': goal1_clients,
            'percentage': (goal1_current / goal1_target * 100) if goal1_target > 0 else 0
        },
        'goal2': {
            'current': goal2_current,
            'target': goal2_target,
            'projects': goal2_projects,
            'percentage': (goal2_current / goal2_target * 100) if goal2_target > 0 else 0
        },
        'goal3': {
            'current': goal3_current,
            'target': goal3_target,
            'partnerships': goal3_partnerships,
            'percentage': (goal3_current / goal3_target * 100) if goal3_target > 0 else 0
        }
    }


def validate_data(revenue_df, enhancements_df, relationships_df):
    """
    Validate data quality and return any warnings.

    Args:
        revenue_df: Revenue tracking DataFrame
        enhancements_df: Business enhancements DataFrame
        relationships_df: Distribution relationships DataFrame

    Returns:
        list: List of validation warnings
    """
    warnings = []

    # Check for missing revenue values
    if revenue_df['Revenue_Thousands'].isna().sum() > 0:
        warnings.append(f"Warning: {revenue_df['Revenue_Thousands'].isna().sum()} revenue entries have missing values")

    # Check for enhancements without completion dates
    completed_no_date = enhancements_df[
        (enhancements_df['Status'] == 'Completed') &
        (enhancements_df['ActualCompletionDate'].isna())
    ]
    if len(completed_no_date) > 0:
        warnings.append(f"Warning: {len(completed_no_date)} completed enhancements missing completion dates")

    # Check for relationships without progress notes
    no_progress = relationships_df[relationships_df['Q1_Progress'].isna()]
    if len(no_progress) > 0:
        warnings.append(f"Warning: {len(no_progress)} relationships missing Q1 progress notes")

    return warnings
