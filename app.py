import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from diabetes_model import DiabetesPredictor
from medicine_recommendations import MedicineRecommendations
from educational_content import EducationalContent
from meal_planner import MealPlanner
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="AI Diabetes Assessment Tool",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load FontAwesome
st.markdown("""
<link rel="stylesheet" 
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
""", unsafe_allow_html=True)

# CSS
st.markdown("""
<style>
.card{background:white;padding:1.5rem;border-radius:12px;
box-shadow:0 4px 6px rgba(0,0,0,0.1);margin-bottom:1.5rem;}
.metric-card{background:linear-gradient(135deg,#667eea,#764ba2);
color:white;padding:1.5rem;border-radius:12px;text-align:center;}
.section-header{color:#1f77b4;border-bottom:2px solid #1f77b4;}
.risk-factor{background:#e9ecef;padding:0.5rem;border-radius:10px;margin:0.2rem 0;}
.header{background:linear-gradient(135deg,#1f77b4,#ff7f0e);
padding:2rem;border-radius:12px;margin-bottom:2rem;color:white;}
.disclaimer{background:#fff3cd;border:1px solid #ffeaa7;
padding:1.2rem;border-radius:12px;margin-bottom:2rem;color:#856404;}
</style>
""", unsafe_allow_html=True)

# Load models
@st.cache_resource
def load_model(): return DiabetesPredictor()

@st.cache_resource
def load_medicine_system(): return MedicineRecommendations()

@st.cache_resource
def load_educational_content(): return EducationalContent()

@st.cache_resource
def load_meal_planner(): return MealPlanner()

diabetes_predictor = load_model()
medicine_system = load_medicine_system()
educational_content = load_educational_content()
meal_planner = load_meal_planner()


def main():

    st.markdown("""
    <div class="header">
    <h1><i class="fa-solid fa-heart-pulse"></i>  Diabetes Assessment Tool</h1>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="disclaimer">
    ⚠️ <strong>MEDICAL DISCLAIMER</strong>: This application is for educational and informational purposes only. 
    It is NOT a substitute for professional medical advice, diagnosis, or treatment. 
    Always consult with qualified healthcare professionals for medical decisions.
    </div>
    """, unsafe_allow_html=True)

    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Choose a section:",
        ["Assessment","Meal Planner","Educational Content","About Diabetes"]
    )

    if page=="Assessment":
        assessment_page()
    elif page=="Meal Planner":
        meal_planner_page()
    elif page=="Educational Content":
        educational_page()
    else:
        diabetes_types_page()


# ================= ASSESSMENT =================

def assessment_page():

    st.markdown('<h2 class="section-header"><i class="fa-solid fa-chart-column"></i> Diabetes Risk Assessment</h2>',unsafe_allow_html=True)

    if "step" not in st.session_state:
        st.session_state.step=1

    # STEP 1
    if st.session_state.step==1:

        l,r=st.columns(2)

        with l:
            st.markdown('<div class="card"><h3><i class="fa-solid fa-user"></i> Personal Info</h3>',unsafe_allow_html=True)
            age=st.slider("Age",1,120,35)
            gender=st.selectbox("Gender",["Male","Female"])
            weight=st.number_input("Weight (kg)",30.0,300.0,90.0)
            height=st.number_input("Height (cm)",100.0,250.0,170.0)
            bmi=weight/((height/100)**2)
            st.info(f"BMI : {bmi:.2f}")
            st.markdown("</div>",unsafe_allow_html=True)

        with r:
            st.markdown('<div class="card"><h3><i class="fa-solid fa-notes-medical"></i> Medical History</h3>',unsafe_allow_html=True)
            family_history=st.selectbox("Family History",["No","Yes"])
            hypertension=st.selectbox("Hypertension",["No","Yes"])
            heart_disease=st.selectbox("Heart Disease",["No","Yes"])
            st.markdown("</div>",unsafe_allow_html=True)

        if st.button("Continue"):
            st.session_state.basic_data={
                'age':age,
                'gender':1 if gender=="Male" else 0,
                'weight':weight,
                'height':height,
                'bmi':bmi,
                'family_history':1 if family_history=="Yes" else 0,
                'hypertension':1 if hypertension=="Yes" else 0,
                'heart_disease':1 if heart_disease=="Yes" else 0
            }
            st.session_state.step=2
            st.rerun()

    # STEP 2
    elif st.session_state.step==2:

        choice=st.radio("Do you have Glucose & HbA1c reports?",["Yes","No"])

        c1,c2=st.columns(2)
        with c1:
            if st.button("Back"):
                st.session_state.step=1
                st.rerun()
        with c2:
            if st.button("Next"):
                st.session_state.step=3 if choice=="Yes" else 4
                st.rerun()

    # STEP 3
    elif st.session_state.step==3:

        l,r=st.columns(2)

        with l:
            st.markdown('<div class="card"><h3><i class="fa-solid fa-vial"></i> Laboratory Values</h3>',unsafe_allow_html=True)
            glucose=st.number_input("Fasting Glucose",50.0,400.0,210.0)
            hba1c=st.number_input("HbA1c",3.0,15.0,9.5)
            systolic_bp=st.number_input("Systolic BP",80.0,250.0,175.0)
            diastolic_bp=st.number_input("Diastolic BP",50.0,150.0,100.0)
            cholesterol=st.number_input("Cholesterol",100.0,400.0,285.0)
            st.markdown("</div>",unsafe_allow_html=True)

        with r:
            st.markdown('<div class="card"><h3><i class="fa-solid fa-person-running"></i> Lifestyle</h3>',unsafe_allow_html=True)
            smoking=st.selectbox("Smoking",["Never","Former","Current"])
            physical_activity=st.selectbox("Activity",["Low","Moderate","High"])
            alcohol=st.selectbox("Alcohol",["None","Light","Moderate","Heavy"])
            st.markdown("</div>",unsafe_allow_html=True)

        c1,c2,c3=st.columns([2,3,2])
        with c2:
            if st.button("Access Results",use_container_width=True):

                final=st.session_state.basic_data
                final.update({
                    'glucose':glucose,'hba1c':hba1c,
                    'systolic_bp':systolic_bp,'diastolic_bp':diastolic_bp,
                    'cholesterol':cholesterol,
                    'smoking':{"Never":0,"Former":1,"Current":2}[smoking],
                    'physical_activity':{"Low":0,"Moderate":1,"High":2}[physical_activity],
                    'alcohol':{"None":0,"Light":1,"Moderate":2,"Heavy":3}[alcohol]
                })

                st.session_state.results=diabetes_predictor.predict(final)
                st.session_state.final_input=final
                st.session_state.step=5
                st.rerun()

        if st.button("Back"):
            st.session_state.step=2
            st.rerun()

    # STEP 4
    elif st.session_state.step==4:
        st.warning("Please get your lab tests done.")
        if st.button("Back"):
            st.session_state.step=2
            st.rerun()

    # STEP 5 – FULL REPORT PAGE
    elif st.session_state.step==5:
        display_results(st.session_state.results,st.session_state.final_input)

        if st.button("View Detailed Report"):
            st.session_state.step=6
            st.rerun()

    # STEP 6 – GRAPHS + MEDICINE + RECOMMENDATIONS
    elif st.session_state.step==6:
        detailed_report(st.session_state.results,st.session_state.final_input)

        if st.button("Back to Results"):
            st.session_state.step=5
            st.rerun()


# ================= RESULT CARDS =================

def display_results(results,data):

    st.subheader("Results")

    c1,c2,c3=st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="metric-card">
        <h3>Risk %</h3>
        <h1>{results['risk_percentage']:.1f}%</h1>
        <p>{results['classification']}</p>
        </div>""",unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="metric-card">
        <h3>Stage</h3>
        <h1>{results['stage']}</h1>
        <p>{results['severity']}</p>
        </div>""",unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="card"><h3>Risk Factors</h3>',unsafe_allow_html=True)
        for f in analyze_risk_factors(data):
            st.markdown(f'<div class="risk-factor">• {f}</div>',unsafe_allow_html=True)
        st.markdown("</div>",unsafe_allow_html=True)


# ================= DETAILED PAGE =================

def detailed_report(results,input_data):

    st.markdown("## Health Metrics Visualization")

    metrics={
        'Metric':['BMI','Glucose','HbA1c','Systolic BP','Diastolic BP'],
        'Your Value':[input_data['bmi'],input_data['glucose'],
                      input_data['hba1c'],input_data['systolic_bp'],
                      input_data['diastolic_bp']],
        'Normal':[24.9,100,5.6,120,80],
        'Diabetes':[30,126,6.5,140,90]
    }

    df=pd.DataFrame(metrics)
    fig=go.Figure()

    fig.add_bar(name='Your Values',x=df['Metric'],y=df['Your Value'])

    fig.add_scatter(name='Normal Range (Upper)',
        x=df['Metric'],y=df['Normal'],
        mode='markers',
        marker=dict(color='green', size=10, symbol='line-ew'),
        line=dict(width=3))

    fig.add_scatter(name='Diabetes Range (Lower)',
        x=df['Metric'],y=df['Diabetes'],
        mode='markers',
        marker=dict(color='red', size=10, symbol='line-ew'),
        line=dict(width=3))

    fig.update_layout(
        title='Your Health Metrics vs Normal/Diabetes Ranges',
        xaxis_title='Health Metrics',
        yaxis_title='Values',
        barmode='group',
        height=500,
        template='plotly_white'
    )

    st.plotly_chart(fig,use_container_width=True)

    # PIE
    rf=analyze_risk_factors(input_data)
    if rf:
        fig_pie=px.pie(
            values=[1]*len(rf),
            names=rf,
            title="Your Risk Factor Distribution",
            color_discrete_sequence=px.colors.sequential.Plasma_r
        )
        st.plotly_chart(fig_pie,use_container_width=True)

    # MEDICINE
    st.markdown("## Medicine Recommendations")
    display_medicine_recommendations(
        medicine_system.get_recommendations(results,input_data))

    # HEALTH
    st.markdown("## Personalized Health Recommendations")
    display_health_recommendations(
        get_health_recommendations(results,input_data))


# ================= SUPPORT FUNCTIONS =================

def analyze_risk_factors(d):
    r=[]
    if d['bmi']>30:r.append("High BMI")
    if d['glucose']>126:r.append("High Glucose")
    if d['hba1c']>6.5:r.append("High HbA1c")
    if d['physical_activity']==0:r.append("Low Physical Activity")
    return r


def display_medicine_recommendations(recommendations):

    st.warning("Educational only. Consult doctor.")

    for cat,meds in recommendations.items():
        st.markdown(f"### {cat}")
        for m in meds:
            with st.expander(m['name']):
                st.write("Type:",m['type'])
                st.write("Dosage:",m['dosage'])
                st.write("Description:",m['description'])
                st.write("Usage:",m['usage'])
                st.write("Side effects:",",".join(m['side_effects']))


def get_health_recommendations(results,input_data):

    rec={'Diet':[],'Exercise':[],'Lifestyle':[],'Monitoring':[]}

    rec['Diet']+=["Increase fiber","Limit sugar","Lean protein"]
    rec['Exercise']+=["Walk daily","150 mins/week"]
    rec['Lifestyle']+=["Good sleep","Stress control"]
    rec['Monitoring']+=["Glucose monitoring","HbA1c test"]

    return rec


def display_health_recommendations(r):

    for cat,items in r.items():
        st.markdown(f"### {cat}")
        for i in items:
            st.success(i)


def educational_page():
    educational_content.display_content()

def meal_planner_page():
    meal_planner.display_meal_planner_interface()

def diabetes_types_page():
    educational_content.display_diabetes_types()


if __name__=="__main__":
    main()
