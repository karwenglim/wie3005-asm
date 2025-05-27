import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Dashboard", page_icon="🏥", layout="wide")
st.title("🏥 Medical History Dashboard")

@st.cache_data
def generate_sample_data():
    np.random.seed(42)
    
    # Patient basic info
    patient_info = {
        'Name': 'Ali',
        'Age': 45,
        'Gender': 'Male',
        'Blood Type': 'A+',
        'Height': '175 cm',
        'Weight': '78 kg',
        'BMI': 25.5
    }
    
    # Generate vital signs data over time
    dates = pd.date_range(start='2023-01-01', end='2024-12-31', freq='M')
    vitals_data = []
    
    for date in dates:
        vitals_data.append({
            'Date': date,
            'Systolic_BP': np.random.normal(130, 15),
            'Diastolic_BP': np.random.normal(85, 10),
            'Heart_Rate': np.random.normal(75, 8),
            'Temperature': np.random.normal(98.6, 0.5),
            'Weight': np.random.normal(78, 2),
            'Blood_Sugar': np.random.normal(100, 20)
        })
    
    vitals_df = pd.DataFrame(vitals_data)
    
    # Lab results
    lab_data = {
        'Test': ['Hemoglobin', 'White Blood Cells', 'Cholesterol', 'HDL', 'LDL', 'Triglycerides', 'Creatinine', 'BUN'],
        'Value': [14.2, 6.8, 195, 45, 125, 150, 1.1, 18],
        'Unit': ['g/dL', '10³/μL', 'mg/dL', 'mg/dL', 'mg/dL', 'mg/dL', 'mg/dL', 'mg/dL'],
        'Reference_Range': ['13.5-17.5', '4.0-11.0', '<200', '>40', '<100', '<150', '0.7-1.3', '7-20'],
        'Status': ['Normal', 'Normal', 'Borderline High', 'Low', 'High', 'Normal', 'Normal', 'Normal']
    }
    lab_df = pd.DataFrame(lab_data)
    
    # Medical history
    medical_history = [
        {'Date': '2023-03-15', 'Condition': 'Hypertension', 'Status': 'Ongoing', 'Medication': 'Lisinopril 10mg'},
        {'Date': '2022-11-20', 'Condition': 'Type 2 Diabetes', 'Status': 'Controlled', 'Medication': 'Metformin 500mg'},
        {'Date': '2023-08-10', 'Condition': 'High Cholesterol', 'Status': 'Ongoing', 'Medication': 'Atorvastatin 20mg'},
        {'Date': '2024-01-05', 'Condition': 'Anxiety', 'Status': 'Managed', 'Medication': 'Sertraline 50mg'}
    ]
    history_df = pd.DataFrame(medical_history)
    
    # Medications
    medications = [
        {'Medication': 'Lisinopril', 'Dosage': '10mg', 'Frequency': 'Once daily', 'Start_Date': '2023-03-15', 'Purpose': 'Blood pressure control'},
        {'Medication': 'Metformin', 'Dosage': '500mg', 'Frequency': 'Twice daily', 'Start_Date': '2022-11-20', 'Purpose': 'Blood sugar control'},
        {'Medication': 'Atorvastatin', 'Dosage': '20mg', 'Frequency': 'Once daily', 'Start_Date': '2023-08-10', 'Purpose': 'Cholesterol management'},
        {'Medication': 'Sertraline', 'Dosage': '50mg', 'Frequency': 'Once daily', 'Start_Date': '2024-01-05', 'Purpose': 'Anxiety management'}
    ]
    medications_df = pd.DataFrame(medications)
    
    return patient_info, vitals_df, lab_df, history_df, medications_df


# Load data
patient_info, vitals_df, lab_df, history_df, medications_df = generate_sample_data()

# Sidebar for patient selection and filters
st.sidebar.header("Patient Information")
st.sidebar.info(f"""
**{patient_info['Name']}**  
Age: {patient_info['Age']}  
Gender: {patient_info['Gender']}  
Blood Type: {patient_info['Blood Type']}  
BMI: {patient_info['BMI']}
""")


# Main dashboard content
tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "💓 Vital Signs", "🧪 Lab Results",  "💊 Medications"])

with tab1:
    st.header("Patient Overview & Key Insights")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        latest_bp = f"{vitals_df['Systolic_BP'].iloc[-1]:.0f}/{vitals_df['Diastolic_BP'].iloc[-1]:.0f}"
        st.metric("Latest Blood Pressure", latest_bp, delta="Normal Range")
    
    with col2:
        latest_hr = f"{vitals_df['Heart_Rate'].iloc[-1]:.0f} bpm"
        st.metric("Heart Rate", latest_hr, delta="Normal")
    
    with col3:
        latest_weight = f"{vitals_df['Weight'].iloc[-1]:.1f} kg"
        st.metric("Current Weight", latest_weight, delta=f"{vitals_df['Weight'].iloc[-1] - vitals_df['Weight'].iloc[0]:+.1f}")
    
    with col4:
        active_conditions = len(history_df[history_df['Status'].isin(['Ongoing', 'Controlled'])])
        st.metric("Active Conditions", active_conditions)
    
    st.markdown("---")
    
    # Clinical insights and alerts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Clinical Insights")
        
        # Analyze trends
        bp_trend = "increasing" if vitals_df['Systolic_BP'].iloc[-3:].mean() > vitals_df['Systolic_BP'].iloc[:3].mean() else "stable"
        weight_change = vitals_df['Weight'].iloc[-1] - vitals_df['Weight'].iloc[0]
        
        insights = [
            f"Blood pressure trend: {bp_trend.upper()}",
            f"Weight change over period: {weight_change:+.1f} kg",
            f"Patient has [ {len(history_df)} ] documented conditions",
            f"Currently on [ {len(medications_df)} ] medications"
        ]
        
        for insight in insights:
            st.write(f"• {insight}")
    
    with col2:
        st.subheader("⚠️ Health Alerts")
        
        # Check for alerts based on latest values
        alerts = []
        latest_systolic = vitals_df['Systolic_BP'].iloc[-1]
        latest_sugar = vitals_df['Blood_Sugar'].iloc[-1]
        
        if latest_systolic > 140:
            alerts.append("High blood pressure detected [Please consult physician]")
        if latest_sugar > 126:
            alerts.append("Elevated blood sugar [Please monitor closely]")
    
        # Check lab results
        high_lab_values = lab_df[lab_df['Status'].str.contains('High|Borderline')]
        for _, row in high_lab_values.iterrows():
            alerts.append(f"**{row['Test']}** -  {row['Status']} - {row['Value']} {row['Unit']}")
        
        if alerts:
            for alert in alerts:
                st.markdown(f'⚠️ {alert}')
        else:
            st.markdown('✅ No critical alerts at this time')
        
        st.caption(f"*Refer to the Lab Results tab for detailed analysis.*")

    st.markdown("---")

    # Medical History Section
    st.header("Medical History")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.subheader("Condition Timeline")
        
        # Convert dates and sort
        history_display = history_df.copy()
        history_display['Date'] = pd.to_datetime(history_display['Date'])
        history_display = history_display.sort_values('Date', ascending=False)
        
        for _, row in history_display.iterrows():
            status_color = {
                'Ongoing': '🔴',
                'Controlled': '🟡',
                'Managed': '🟢',
                'Resolved': '✅'
            }.get(row['Status'], '⚪')
            
            st.markdown(f"""
            **{row['Date'].strftime('%Y-%m-%d')}** - {status_color} **{row['Condition']}**  
            Status: {row['Status']} | Medication: {row['Medication']}
            """)
            st.markdown("---")

        st.caption("Status: 🔴- Ongoing  🟡- Controlled, 🟢- Managed ")
    
    with col2:
        st.subheader("Condition Status")
        
        status_counts = history_df['Status'].value_counts()
        fig_status = px.bar(
            x=status_counts.values,
            y=status_counts.index,
            orientation='h',
            title="Current Status Distribution",
            labels={"x": "Number of Records", "y": "Status Type"}
        )
        st.plotly_chart(fig_status, use_container_width=True)


#===========================================================================================================

with tab2:
    col1, col2 = st.columns([3, 1]) 
    
    with col1:   
        st.header("Vital Signs Monitoring")

    with col2:
        date_range = st.date_input(
            "Select Date Range",
            value=(vitals_df['Date'].min(), vitals_df['Date'].max()),
            min_value=vitals_df['Date'].min(),
            max_value=vitals_df['Date'].max()
        )  
    
    # Filter data based on date range
    mask = (vitals_df['Date'] >= pd.to_datetime(date_range[0])) & (vitals_df['Date'] <= pd.to_datetime(date_range[1]))
    filtered_vitals = vitals_df.loc[mask]
    
    # Blood pressure chart
    fig_bp = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig_bp.add_trace(
        go.Scatter(x=filtered_vitals['Date'], y=filtered_vitals['Systolic_BP'], 
                  name='Systolic BP', line=dict(color='red', width=2)),
        secondary_y=False,
    )
    
    fig_bp.add_trace(
        go.Scatter(x=filtered_vitals['Date'], y=filtered_vitals['Diastolic_BP'], 
                  name='Diastolic BP', line=dict(color='blue', width=2)),
        secondary_y=False,
    )
    
    # Reference lines for chart
    fig_bp.add_hline(y=140, line_dash="dash", line_color="red", annotation_text="High BP Threshold")
    fig_bp.add_hline(y=90, line_dash="dash", line_color="orange", annotation_text="High Diastolic Threshold")
    
    fig_bp.update_layout(title="Blood Pressure Trends", height=400)
    fig_bp.update_xaxes(title_text="Date")
    fig_bp.update_yaxes(title_text="Blood Pressure (mmHg)", secondary_y=False)
    
    st.plotly_chart(fig_bp, use_container_width=True)
    
    # Other vital signs
    col1, col2 = st.columns(2)
    
    with col1:
        fig_hr = px.line(filtered_vitals, x='Date', y='Heart_Rate', 
                        title='Heart Rate Over Time',
                        labels={'Heart_Rate': 'Heart Rate (bpm)'})
        fig_hr.add_hline(y=100, line_dash="dash", line_color="red", annotation_text="High HR")
        fig_hr.add_hline(y=60, line_dash="dash", line_color="blue", annotation_text="Low HR")
        st.plotly_chart(fig_hr, use_container_width=True)
    
    with col2:
        fig_weight = px.line(filtered_vitals, x='Date', y='Weight', 
                           title='Weight Tracking',
                           labels={'Weight': 'Weight (kg)'})
        st.plotly_chart(fig_weight, use_container_width=True)
    
    # Blood sugar monitoring
    fig_sugar = px.line(filtered_vitals, x='Date', y='Blood_Sugar', 
                       title='Blood Sugar Levels',
                       labels={'Blood_Sugar': 'Blood Sugar (mg/dL)'})
    fig_sugar.add_hline(y=126, line_dash="dash", line_color="red", annotation_text="Diabetes Threshold")
    fig_sugar.add_hline(y=100, line_dash="dash", line_color="orange", annotation_text="Pre-diabetes")
    st.plotly_chart(fig_sugar, use_container_width=True)


#===========================================================================================================

with tab3:
    st.header("Laboratory Results")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Latest Lab Results")
        
        # Create a styled dataframe
        lab_styled = lab_df.copy()
        lab_styled['Status_Icon'] = lab_styled['Status'].map({
            'Normal': '✅',
            'High': '🔴',
            'Low': '🔵',
            'Borderline High': '🟡'
        })
        
        st.dataframe(
            lab_styled[['Test', 'Value', 'Unit', 'Reference_Range', 'Status_Icon', 'Status']],
            use_container_width=True,
            hide_index=True
        )
    
    with col2:
        st.subheader("Lab Status Summary")
        
        status_counts = lab_df['Status'].value_counts()
        fig_pie = px.pie(values=status_counts.values, names=status_counts.index,
                        title="Lab Results Distribution")
        st.plotly_chart(fig_pie, use_container_width=True)
    
    # Detailed analysis
    st.subheader("Lab Results Analysis")
    
    # Cholesterol panel visualization
    cholesterol_data = lab_df[lab_df['Test'].isin(['Cholesterol', 'HDL', 'LDL', 'Triglycerides'])]
    
    fig_chol = go.Figure()
    
    colors = ['red' if status in ['High', 'Borderline High'] else 'green' if status == 'Normal' else 'blue' 
              for status in cholesterol_data['Status']]
    
    fig_chol.add_trace(go.Bar(
        x=cholesterol_data['Test'],
        y=cholesterol_data['Value'],
        marker_color=colors,
        text=cholesterol_data['Value'],
        textposition='auto',
    ))
    
    fig_chol.update_layout(
        title="Cholesterol Panel Results",
        xaxis_title="Test",
        yaxis_title="Value (mg/dL)",
        height=400
    )
    
    st.plotly_chart(fig_chol, use_container_width=True)
    
#===========================================================================================================

with tab4:
    st.header("Current Medications")
    
    st.subheader("Active Prescriptions")
    
    # Display medications 
    for _, med in medications_df.iterrows():
        with st.expander(f"💊 {med['Medication']} - {med['Dosage']}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Dosage:** {med['Dosage']}")
                st.write(f"**Frequency:** {med['Frequency']}")
                st.write(f"**Start Date:** {med['Start_Date']}")
            
            with col2:
                st.write(f"**Purpose:** {med['Purpose']}")
                
                # Add some medication-specific notes (IF-THEN)
                if 'Lisinopril' in med['Medication']:
                    st.info("Monitor blood pressure regularly. Report any persistent cough.")
                elif 'Metformin' in med['Medication']:
                    st.info("Take with food. Monitor blood sugar levels.")
                elif 'Atorvastatin' in med['Medication']:
                    st.info("Take in the evening. Annual liver function tests recommended.")
                elif 'Sertraline' in med['Medication']:
                    st.info("May take 4-6 weeks for full effect. Monitor mood changes.")
    
