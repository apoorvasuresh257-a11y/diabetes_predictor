import streamlit as st
import pandas as pd


class EducationalContent:

    def __init__(self):
        pass

    # ================= MAIN PAGE =================
    def display_content(self):

        tabs = st.tabs([
            "Risk Factors",
            "Prevention",
            "Complications",
            "Management"
        ])

        with tabs[0]:
            self.display_risk_factors()

        with tabs[1]:
            self.display_prevention()

        with tabs[2]:
            self.display_complications()

        with tabs[3]:
            self.display_management()


    # ================= RISK FACTORS =================
    def display_risk_factors(self):

        st.markdown("""
        <h3><i class="fa-solid fa-triangle-exclamation"></i> Diabetes Risk Factors</h3>
        """, unsafe_allow_html=True)

        st.markdown("""
        **Modifiable**
        - Overweight  
        - Physical inactivity  
        - Poor diet  
        - Smoking  
        - High BP  
        
        **Non-modifiable**
        - Age > 45  
        - Family history  
        - PCOS  
        """)

        st.divider()

        st.subheader("Check factors that apply to you")

        factors = {
            "Age > 45": 1,
            "BMI > 25": 2,
            "Family history": 3,
            "High BP": 2,
            "Inactive lifestyle": 2,
            "Smoking": 1,
            "High cholesterol": 1,
            "Gestational diabetes": 3,
            "PCOS": 2
        }

        score = 0
        for f, w in factors.items():
            if st.checkbox(f):
                score += w

        if st.button("Calculate Risk"):
            if score <= 2:
                st.success("Low Risk")
            elif score <= 6:
                st.warning("Moderate Risk")
            elif score <= 10:
                st.error("High Risk")
            else:
                st.error("Very High Risk – consult doctor")


    # ================= PREVENTION =================
    def display_prevention(self):

        st.markdown("""
        <h3><i class="fa-solid fa-shield-heart"></i> Diabetes Prevention</h3>
        """, unsafe_allow_html=True)

        st.divider()
        st.subheader("Personal Action Plan")

        diet = st.multiselect(
            "Diet Goals",
            [
                "Eat more vegetables",
                "Reduce portions",
                "Whole grains",
                "Limit sugar",
                "Home cooking",
                "High fiber foods"
            ]
        )

        exercise = st.selectbox(
            "Exercise Plan",
            [
                "30 min - 3x/week",
                "30 min - 5x/week",
                "45 min - 5x/week",
                "60 min - 5x/week"
            ]
        )

        lifestyle = st.multiselect(
            "Lifestyle Goals",
            [
                "Better sleep",
                "Stress control",
                "Quit smoking",
                "Limit alcohol",
                "Daily steps",
                "Meditation"
            ]
        )

        if st.button("Generate Action Plan", type="primary"):

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("### Diet")
                for d in diet:
                    self.card(d, "Improves glucose control")

            with col2:
                st.markdown("### Exercise")
                self.card(exercise, "Boosts insulin sensitivity")

            with col3:
                st.markdown("### Lifestyle")
                for l in lifestyle:
                    self.card(l, "Supports mental & physical health")


    # ================= COMPLICATIONS =================
    def display_complications(self):

        st.markdown("""
        <h3><i class="fa-solid fa-heart-pulse"></i> Diabetes Complications</h3>
        """, unsafe_allow_html=True)

        st.markdown("""
        **Short Term**
        - Hypoglycemia  
        - Ketoacidosis  

        **Long Term**
        - Heart disease  
        - Kidney failure  
        - Eye damage  
        - Nerve damage  
        - Foot ulcers  
        """)

        st.divider()

        checks = [
            "Eye exam",
            "Foot exam",
            "Kidney test",
            "Cholesterol test",
            "BP monitoring"
        ]

        for c in checks:
            st.checkbox(c)


    # ================= MANAGEMENT =================
    def display_management(self):

        st.markdown("""
        <h3><i class="fa-solid fa-gear"></i> Diabetes Management</h3>
        """, unsafe_allow_html=True)

        st.markdown("""
        **ABC Rule**
        A – A1C  
        B – Blood Pressure  
        C – Cholesterol  
        """)

        a1c = st.number_input("Current HbA1c", 4.0, 15.0, 7.0)
        bp = st.number_input("Systolic BP", 80, 200, 130)
        ldl = st.number_input("LDL", 50, 300, 100)

        adherence = st.slider("Medication adherence (%)", 0, 100, 90)

        if adherence >= 90:
            st.success("Excellent adherence")
        elif adherence >= 80:
            st.info("Good adherence")
        else:
            st.warning("Needs improvement")


    # ================= ABOUT DIABETES =================
    def display_diabetes_types(self):

        st.markdown("""
        <h2><i class="fa-solid fa-microscope"></i> Types of Diabetes</h2>
        """, unsafe_allow_html=True)

        with st.expander("Type 1 Diabetes"):
            st.markdown("""
            **Cause:** Autoimmune destruction  
            - Children & young adults  
            - Needs insulin for life  
            - 5–10% cases  
            """)

        with st.expander("Type 2 Diabetes"):
            st.markdown("""
            **Cause:** Insulin resistance  
            - 90% cases  
            - Lifestyle related  
            - Preventable  
            """)

        with st.expander("Gestational Diabetes"):
            st.markdown("""
            - During pregnancy  
            - Resolves after birth  
            - Risk later in life  
            """)

        with st.expander("Prediabetes"):
            st.markdown("""
            - HbA1c 5.7–6.4%  
            - Reversible stage  
            """)

        st.divider()

        st.markdown("""
        <h2><i class="fa-solid fa-timeline"></i> Disease Progression Timeline</h2>
        """, unsafe_allow_html=True)

        stages = [
            ("Normal", "Glucose < 100"),
            ("Prediabetes", "100–125"),
            ("Early Diabetes", "HbA1c 6.5–7.5"),
            ("Established", "7.5–9"),
            ("Advanced", "> 9")
        ]

        for s, desc in stages:
            self.timeline_card(s, desc)

        st.divider()

        st.markdown("""
        <h3><i class="fa-solid fa-stethoscope"></i> Diagnostic Criteria</h3>
        """, unsafe_allow_html=True)

        data = {
            "Condition": ["Normal", "Prediabetes", "Diabetes"],
            "Fasting Glucose": ["<100", "100–125", "≥126"],
            "HbA1c (%)": ["<5.7", "5.7–6.4", "≥6.5"]
        }

        df = pd.DataFrame(data)
        st.table(df)


    # ================= UI COMPONENTS =================
    def card(self, title, desc):

        st.markdown(f"""
        <div style="
        padding:14px;
        border-radius:12px;
        background:#F1F8E9;
        margin-bottom:10px;
        box-shadow:0 4px 6px rgba(0,0,0,0.1)">
        <b>{title}</b><br>
        <small>{desc}</small>
        </div>
        """, unsafe_allow_html=True)


    def timeline_card(self, title, desc):

        st.markdown(f"""
        <div style="
        padding:12px;
        border-left:5px solid #1976D2;
        background:#E3F2FD;
        margin-bottom:12px">
        <b>{title}</b><br>
        <small>{desc}</small>
        </div>
        """, unsafe_allow_html=True)
