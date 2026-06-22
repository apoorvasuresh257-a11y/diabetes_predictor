class MedicineRecommendations:
    def __init__(self):
        self.medicine_database = self._initialize_medicine_database()
    
    def _initialize_medicine_database(self):
        """Initialize comprehensive medicine database"""
        return {
            'prediabetes': {
                'lifestyle_medications': [
                    {
                        'name': 'Metformin',
                        'type': 'Biguanide',
                        'dosage': '500-850mg twice daily with meals',
                        'description': 'Reduces glucose production by liver and improves insulin sensitivity',
                        'usage': 'Prevention of Type 2 diabetes in high-risk individuals',
                        'side_effects': ['Nausea', 'Diarrhea', 'Metallic taste', 'Vitamin B12 deficiency']
                    }
                ],
                'supplements': [
                    {
                        'name': 'Alpha-Lipoic Acid',
                        'type': 'Antioxidant Supplement',
                        'dosage': '300-600mg daily',
                        'description': 'May improve insulin sensitivity and glucose uptake',
                        'usage': 'Supplementary therapy for glucose control',
                        'side_effects': ['Skin rash', 'Stomach upset']
                    },
                    {
                        'name': 'Chromium Picolinate',
                        'type': 'Mineral Supplement',
                        'dosage': '200-400mcg daily',
                        'description': 'May enhance insulin action and glucose metabolism',
                        'usage': 'May help with glucose control',
                        'side_effects': ['Headache', 'Sleep disturbances']
                    }
                ]
            },
            'type2_early': {
                'first_line': [
                    {
                        'name': 'Metformin',
                        'type': 'Biguanide',
                        'dosage': '500mg twice daily, may increase to 1000mg twice daily',
                        'description': 'First-line treatment for Type 2 diabetes',
                        'usage': 'Reduces hepatic glucose production and improves insulin sensitivity',
                        'side_effects': ['GI upset', 'Lactic acidosis (rare)', 'B12 deficiency']
                    }
                ],
                'second_line': [
                    {
                        'name': 'Glipizide',
                        'type': 'Sulfonylurea',
                        'dosage': '5-10mg daily before breakfast',
                        'description': 'Stimulates pancreatic insulin release',
                        'usage': 'When metformin alone is insufficient',
                        'side_effects': ['Hypoglycemia', 'Weight gain', 'Skin reactions']
                    },
                    {
                        'name': 'Sitagliptin',
                        'type': 'DPP-4 Inhibitor',
                        'dosage': '100mg once daily',
                        'description': 'Increases insulin and decreases glucagon in glucose-dependent manner',
                        'usage': 'Add-on therapy with good safety profile',
                        'side_effects': ['Upper respiratory infections', 'Headache', 'Joint pain']
                    }
                ]
            },
            'type2_moderate': {
                'combination_therapy': [
                    {
                        'name': 'Metformin + Glipizide',
                        'type': 'Combination Therapy',
                        'dosage': 'Metformin 1000mg + Glipizide 5mg twice daily',
                        'description': 'Combines insulin sensitivity improvement with insulin stimulation',
                        'usage': 'For patients not achieving target with monotherapy',
                        'side_effects': ['Combined side effects of both medications']
                    },
                    {
                        'name': 'Empagliflozin',
                        'type': 'SGLT2 Inhibitor',
                        'dosage': '10-25mg once daily in the morning',
                        'description': 'Blocks glucose reabsorption in kidneys',
                        'usage': 'Provides cardiovascular and renal protection',
                        'side_effects': ['UTI', 'Genital infections', 'Dehydration', 'DKA (rare)']
                    }
                ],
                'injectable': [
                    {
                        'name': 'Liraglutide',
                        'type': 'GLP-1 Receptor Agonist',
                        'dosage': '0.6mg daily, may increase to 1.8mg daily',
                        'description': 'Incretin mimetic that stimulates insulin and suppresses glucagon',
                        'usage': 'For weight loss and cardiovascular benefits',
                        'side_effects': ['Nausea', 'Vomiting', 'Diarrhea', 'Pancreatitis risk']
                    }
                ]
            },
            'type2_advanced': {
                'insulin_therapy': [
                    {
                        'name': 'Insulin Glargine (Lantus)',
                        'type': 'Long-acting Insulin',
                        'dosage': '10-20 units daily at bedtime, adjust based on fasting glucose',
                        'description': 'Provides 24-hour basal insulin coverage',
                        'usage': 'When oral medications are insufficient',
                        'side_effects': ['Hypoglycemia', 'Weight gain', 'Injection site reactions']
                    },
                    {
                        'name': 'Insulin Aspart (NovoLog)',
                        'type': 'Rapid-acting Insulin',
                        'dosage': 'Individualized based on carbohydrate intake and blood glucose',
                        'description': 'Covers mealtime glucose spikes',
                        'usage': 'Intensive insulin therapy',
                        'side_effects': ['Hypoglycemia', 'Weight gain', 'Lipodystrophy']
                    }
                ],
                'intensive_care': [
                    {
                        'name': 'Metformin + Insulin',
                        'type': 'Combination Therapy',
                        'dosage': 'Continue metformin with insulin as tolerated',
                        'description': 'Maintains insulin sensitivity while providing insulin replacement',
                        'usage': 'Comprehensive diabetes management',
                        'side_effects': ['Combined medication effects']
                    }
                ]
            },
            'type1': {
                'basal_insulin': [
                    {
                        'name': 'Insulin Detemir (Levemir)',
                        'type': 'Long-acting Insulin',
                        'dosage': '0.1-0.2 units/kg twice daily, adjust based on glucose monitoring',
                        'description': 'Provides basal insulin replacement',
                        'usage': 'Essential for Type 1 diabetes management',
                        'side_effects': ['Hypoglycemia', 'Weight changes', 'Allergic reactions']
                    }
                ],
                'bolus_insulin': [
                    {
                        'name': 'Insulin Lispro (Humalog)',
                        'type': 'Rapid-acting Insulin',
                        'dosage': 'Carb ratio typically 1:10-15, correction factor individualized',
                        'description': 'Covers meals and corrects high glucose',
                        'usage': 'Mealtime and correction dosing',
                        'side_effects': ['Hypoglycemia', 'Injection site reactions']
                    }
                ],
                'continuous_therapy': [
                    {
                        'name': 'Insulin Pump Therapy',
                        'type': 'Device-based Treatment',
                        'dosage': 'Continuous basal rates with bolus for meals',
                        'description': 'Provides precise insulin delivery',
                        'usage': 'For intensive management and lifestyle flexibility',
                        'side_effects': ['Device-related complications', 'DKA risk if pump fails']
                    }
                ]
            },
            'complications': {
                'hypertension': [
                    {
                        'name': 'Lisinopril',
                        'type': 'ACE Inhibitor',
                        'dosage': '10-40mg once daily',
                        'description': 'Provides cardiovascular and renal protection',
                        'usage': 'First-line for diabetic hypertension',
                        'side_effects': ['Cough', 'Hyperkalemia', 'Angioedema (rare)']
                    }
                ],
                'dyslipidemia': [
                    {
                        'name': 'Atorvastatin',
                        'type': 'HMG-CoA Reductase Inhibitor',
                        'dosage': '20-80mg daily in the evening',
                        'description': 'Reduces cardiovascular risk in diabetes',
                        'usage': 'For cholesterol management and CV protection',
                        'side_effects': ['Muscle pain', 'Liver enzyme elevation', 'Memory issues']
                    }
                ]
            }
        }
    
    def get_recommendations(self, prediction_results, patient_data):
        """Get personalized medicine recommendations"""
        recommendations = {}
        
        classification = prediction_results['classification']
        stage = prediction_results['stage']
        severity = prediction_results['severity']
        
        if classification == "Pre-diabetes":
            recommendations.update(self._get_prediabetes_recommendations(patient_data))
        
        elif classification == "Type 2 Diabetes":
            recommendations.update(self._get_type2_recommendations(severity, patient_data))
        
        elif classification == "Type 1 Diabetes":
            recommendations.update(self._get_type1_recommendations(patient_data))
        
        # Add complication management
        recommendations.update(self._get_complication_management(patient_data))
        
        return recommendations
    
    def _get_prediabetes_recommendations(self, patient_data):
        """Get recommendations for pre-diabetes"""
        recommendations = {}
        
        # Lifestyle medications
        if patient_data['bmi'] > 30 or patient_data['family_history'] == 1:
            recommendations['Preventive Medications'] = self.medicine_database['prediabetes']['lifestyle_medications']
        
        # Supplements
        recommendations['Nutritional Supplements'] = self.medicine_database['prediabetes']['supplements']
        
        return recommendations
    
    def _get_type2_recommendations(self, severity, patient_data):
        """Get recommendations for Type 2 diabetes based on severity"""
        recommendations = {}
        
        if severity == "Mild":
            # Early stage Type 2
            recommendations['First-line Treatment'] = self.medicine_database['type2_early']['first_line']
            if patient_data['hba1c'] > 7.0:
                recommendations['Additional Options'] = self.medicine_database['type2_early']['second_line']
        
        elif severity == "Moderate":
            # Moderate Type 2
            recommendations['Combination Therapy'] = self.medicine_database['type2_moderate']['combination_therapy']
            if patient_data['bmi'] > 30:
                recommendations['Weight Management'] = self.medicine_database['type2_moderate']['injectable']
        
        else:  # Severe
            # Advanced Type 2
            recommendations['Insulin Therapy'] = self.medicine_database['type2_advanced']['insulin_therapy']
            recommendations['Intensive Management'] = self.medicine_database['type2_advanced']['intensive_care']
        
        return recommendations
    
    def _get_type1_recommendations(self, patient_data):
        """Get recommendations for Type 1 diabetes"""
        recommendations = {}
        
        recommendations['Basal Insulin'] = self.medicine_database['type1']['basal_insulin']
        recommendations['Bolus Insulin'] = self.medicine_database['type1']['bolus_insulin']
        
        # Advanced options for intensive management
        if patient_data['age'] > 12:  # Appropriate age for pump therapy
            recommendations['Advanced Therapy'] = self.medicine_database['type1']['continuous_therapy']
        
        return recommendations
    
    def _get_complication_management(self, patient_data):
        """Get recommendations for managing diabetes complications"""
        recommendations = {}
        
        # Hypertension management
        if patient_data['hypertension'] == 1 or patient_data['systolic_bp'] > 130:
            recommendations['Blood Pressure Management'] = self.medicine_database['complications']['hypertension']
        
        # Dyslipidemia management
        if patient_data['cholesterol'] > 200 or patient_data['age'] > 40:
            recommendations['Cholesterol Management'] = self.medicine_database['complications']['dyslipidemia']
        
        return recommendations
    
    def get_medication_interactions(self, medications):
        """Check for potential medication interactions"""
        interactions = []
        
        # Common diabetes medication interactions
        interaction_database = {
            ('Metformin', 'Insulin'): 'Generally safe combination, may reduce insulin requirements',
            ('Metformin', 'Lisinopril'): 'Monitor kidney function more frequently',
            ('Insulin', 'Atorvastatin'): 'May need insulin dose adjustment',
            ('Glipizide', 'Atorvastatin'): 'Increased risk of muscle problems'
        }
        
        for med1, med2 in interaction_database.keys():
            if med1 in medications and med2 in medications:
                interactions.append({
                    'medications': f"{med1} + {med2}",
                    'interaction': interaction_database[(med1, med2)]
                })
        
        return interactions
