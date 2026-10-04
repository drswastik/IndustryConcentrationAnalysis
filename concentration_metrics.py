import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_metrics(df):
    """
    Calculates CR4 and HHI from a dataframe containing company market shares.
    Assumes columns: 'Year', 'Firm1_Share', 'Firm2_Share', 'Firm3_Share', 'Firm4_Share', 'Other_Firms_Shares'
    """
    # Isolate the share columns for the top 4 firms
    share_columns = [col for col in df.columns if 'Share' in col]
    top_4_shares = df[share_columns[:4]]
    
    # Calculate CR4 (Sum of top 4 market shares / 100 for ratio)
    df['CR4'] = top_4_shares.sum(axis=1) / 100
    
    # Calculate HHI (Sum of squared market shares)
    # Note: In standard economics, whole percentages are squared (e.g., 20% -> 20^2 = 400)
    df['HHI'] = df[share_columns].apply(lambda x: sum(i**2 for i in x.dropna()), axis=1)
    
    return df

def plot_trends(df, industry_name):
    """
    Generates and saves dual-axis line charts for CR4 and HHI trends.
    """
    sns.set_theme(style="whitegrid")
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot CR4 on primary Y-axis
    color = 'tab:blue'
    ax1.set_xlabel('Years', fontweight='bold')
    ax1.set_ylabel('CR4 Ratio', color=color, fontweight='bold')
    ax1.plot(df['Year'], df['CR4'], color=color, marker='o', linewidth=2, markersize=8, label='CR4')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_ylim(0, 1.0)
    ax1.set_xticks(df['Year'])

    # Instantiate a second axes that shares the same x-axis for HHI
    ax2 = ax1.twinx()  
    color = 'tab:green'
    ax2.set_ylabel('HHI', color=color, fontweight='bold')  
    ax2.plot(df['Year'], df['HHI'], color=color, marker='s', linewidth=2, markersize=8, label='HHI')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim(0, 2500)

    plt.title(f'{industry_name} Industry: Concentration Trends (2015-2024)', fontsize=14, fontweight='bold')
    fig.tight_layout()  
    
    # Save the figure programmatically
    filename = f"{industry_name.lower().replace(' ', '_')}_trends.png"
    plt.savefig(filename, dpi=300)
    print(f"Saved visualization to {filename}")
    plt.show()

if __name__ == "__main__":
    # Example usage: Replace 'market_data.csv' with your actual exported CSV file
    try:
        # Load the data
        print("Loading market data...")
        # data = pd.read_csv('market_data.csv') 
        
        # --- Mock Data for testing the script locally before you link the CSV ---
        data = pd.DataFrame({
            'Year': range(2015, 2025),
            'UltraTech_Share': [27.6, 25.4, 23.1, 26.2, 31.6, 30.5, 31.0, 31.7, 31.5, 37.5],
            'Ambuja_Share': [11.4, 9.9, 10.0, 9.8, 9.1, 8.5, 10.0, 10.0, 10.2, 9.8],
            'ACC_Share': [13.9, 11.8, 12.6, 12.9, 12.3, 10.2, 11.5, 13.8, 10.2, 11.4],
            'Shree_Share': [7.8, 5.9, 8.2, 8.5, 9.2, 8.8, 8.9, 9.1, 8.5, 10.6]
        })
        
        # Process and plot
        analyzed_df = calculate_metrics(data)
        plot_trends(analyzed_df, "Cement")
        
    except FileNotFoundError:
        print("Please ensure your CSV file is in the same directory.")