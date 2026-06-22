import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import random


class MealPlanner:
    def __init__(self):
        self.food_database = self._initialize_food_database()
        self.meal_templates = self._initialize_meal_templates()
        self.allergy_substitutes = self._initialize_allergy_substitutes()

    # ---------------------------------------------------
    # DATABASE
    # ---------------------------------------------------

    def _initialize_food_database(self):
        # Indian-centric food database with veg / non-veg categories
        return {
            'grains': [
                {'name': 'Oats', 'calories_per_100g': 389, 'protein': 17, 'carbs': 66, 'fat': 7, 'fiber': 10, 'glycemic_index': 55, 'category': 'veg'},
                {'name': 'Brown Rice', 'calories_per_100g': 123, 'protein': 2.7, 'carbs': 25.6, 'fat': 1, 'fiber': 1.8, 'glycemic_index': 50, 'category': 'veg'},
                {'name': 'Roti (Whole Wheat)', 'calories_per_100g': 250, 'protein': 9, 'carbs': 45, 'fat': 3.5, 'fiber': 6, 'glycemic_index': 50, 'category': 'veg'},
                {'name': 'Quinoa', 'calories_per_100g': 120, 'protein': 4.4, 'carbs': 21.3, 'fat': 1.9, 'fiber': 2.8, 'glycemic_index': 53, 'category': 'veg'}
            ],
            'dals_legumes': [
                {'name': 'Moong Dal', 'calories_per_100g': 347, 'protein': 24, 'carbs': 59, 'fat': 1.2, 'fiber': 16, 'glycemic_index': 30, 'category': 'veg'},
                {'name': 'Masoor Dal', 'calories_per_100g': 358, 'protein': 25, 'carbs': 60, 'fat': 1.1, 'fiber': 11, 'glycemic_index': 29, 'category': 'veg'},
                {'name': 'Chickpeas', 'calories_per_100g': 164, 'protein': 8, 'carbs': 27, 'fat': 2.6, 'fiber': 8, 'glycemic_index': 28, 'category': 'veg'}
            ],
            'vegetables': [
                {'name': 'Spinach', 'calories_per_100g': 23, 'protein': 2.9, 'carbs': 3.6, 'fat': 0.4, 'fiber': 2.2, 'glycemic_index': 15, 'category': 'veg'},
                {'name': 'Cauliflower', 'calories_per_100g': 25, 'protein': 1.9, 'carbs': 5, 'fat': 0.3, 'fiber': 2, 'glycemic_index': 15, 'category': 'veg'},
                {'name': 'Mixed Vegetables', 'calories_per_100g': 50, 'protein': 2, 'carbs': 10, 'fat': 0.5, 'fiber': 3, 'glycemic_index': 30, 'category': 'veg'}
            ],
            'dairy': [
                {'name': 'Paneer', 'calories_per_100g': 265, 'protein': 18, 'carbs': 1.2, 'fat': 20, 'fiber': 0, 'glycemic_index': 27, 'category': 'veg'},
                {'name': 'Curd', 'calories_per_100g': 98, 'protein': 3.5, 'carbs': 4.7, 'fat': 7.7, 'fiber': 0, 'glycemic_index': 35, 'category': 'veg'}
            ],
            'eggs_fish_chicken': [
                {'name': 'Eggs', 'calories_per_100g': 155, 'protein': 13, 'carbs': 1.1, 'fat': 11, 'fiber': 0, 'glycemic_index': 0, 'category': 'non-veg'},
                {'name': 'Chicken Breast', 'calories_per_100g': 165, 'protein': 31, 'carbs': 0, 'fat': 3.6, 'fiber': 0, 'glycemic_index': 0, 'category': 'non-veg'},
                {'name': 'Fish (Rohu)', 'calories_per_100g': 120, 'protein': 20, 'carbs': 0, 'fat': 4, 'fiber': 0, 'glycemic_index': 0, 'category': 'non-veg'}
            ],
            'healthy_snacks': [
                {'name': 'Roasted Chana', 'calories_per_100g': 164, 'protein': 9, 'carbs': 27, 'fat': 2.6, 'fiber': 8, 'glycemic_index': 28, 'category': 'veg'},
                {'name': 'Mixed Nuts (small portion)', 'calories_per_100g': 607, 'protein': 20, 'carbs': 21, 'fat': 54, 'fiber': 7, 'glycemic_index': 15, 'category': 'veg'}
            ]
        }

    def _initialize_meal_templates(self):
        # Indian meal templates with veg and non-veg friendly options
        return {
            'diabetes_management': {
                'breakfast': [
                    {'name': 'Masala Oats', 'ingredients': ['Oats','Mixed Vegetables'], 'prep_time': 10, 'category': 'veg'},
                    {'name': 'Moong Dal Cheela (savory pancake)', 'ingredients': ['Moong Dal','Mixed Vegetables'], 'prep_time': 15, 'category': 'veg'},
                    {'name': 'Paneer Bhurji', 'ingredients': ['Paneer','Mixed Vegetables'], 'prep_time': 12, 'category': 'veg'}
                ],
                'lunch': [
                    {'name': 'Dal Tadka with Brown Rice', 'ingredients': ['Masoor Dal','Brown Rice'], 'prep_time': 25, 'category': 'veg'},
                    {'name': 'Chole with Roti', 'ingredients': ['Chickpeas','Roti (Whole Wheat)'], 'prep_time': 30, 'category': 'veg'},
                    {'name': 'Grilled Tandoori Chicken Salad', 'ingredients': ['Chicken Breast','Mixed Vegetables'], 'prep_time': 25, 'category': 'non-veg'}
                ],
                'dinner': [
                    {'name': 'Palak Paneer with Roti', 'ingredients': ['Spinach','Paneer','Roti (Whole Wheat)'], 'prep_time': 30, 'category': 'veg'},
                    {'name': 'Grilled Fish with Vegetables', 'ingredients': ['Fish (Rohu)','Mixed Vegetables'], 'prep_time': 25, 'category': 'non-veg'},
                    {'name': 'Mixed Veg & Dal Khichdi', 'ingredients': ['Moong Dal','Brown Rice','Mixed Vegetables'], 'prep_time': 35, 'category': 'veg'}
                ]
            },

            'weight_loss': {
                'breakfast': [
                    {'name': 'Ragi Porridge', 'ingredients': ['Roti (Whole Wheat)'], 'prep_time': 10, 'category': 'veg'},
                    {'name': 'Poha with Peas', 'ingredients': ['Brown Rice','Mixed Vegetables'], 'prep_time': 12, 'category': 'veg'}
                ],
                'lunch': [
                    {'name': 'Grilled Chicken with Salad', 'ingredients': ['Chicken Breast','Mixed Vegetables'], 'prep_time': 20, 'category': 'non-veg'},
                    {'name': 'Lentil Salad', 'ingredients': ['Moong Dal','Mixed Vegetables'], 'prep_time': 15, 'category': 'veg'}
                ],
                'dinner': [
                    {'name': 'Light Vegetable Curry with Roti', 'ingredients': ['Mixed Vegetables','Roti (Whole Wheat)'], 'prep_time': 20, 'category': 'veg'},
                    {'name': 'Tandoori Fish with Greens', 'ingredients': ['Fish (Rohu)','Spinach'], 'prep_time': 22, 'category': 'non-veg'}
                ]
            },

            'muscle_gain': {
                'breakfast': [
                    {'name': 'Egg Bhurji with Roti', 'ingredients': ['Eggs','Roti (Whole Wheat)'], 'prep_time': 15, 'category': 'non-veg'},
                    {'name': 'Paneer & Oats Bowl', 'ingredients': ['Paneer','Oats'], 'prep_time': 12, 'category': 'veg'}
                ],
                'lunch': [
                    {'name': 'Chicken Power Bowl with Quinoa', 'ingredients': ['Chicken Breast','Quinoa','Mixed Vegetables'], 'prep_time': 25, 'category': 'non-veg'},
                    {'name': 'Protein Lentil Curry', 'ingredients': ['Masoor Dal','Brown Rice'], 'prep_time': 20, 'category': 'veg'}
                ],
                'dinner': [
                    {'name': 'Grilled Chicken Plate with Veg', 'ingredients': ['Chicken Breast','Mixed Vegetables'], 'prep_time': 25, 'category': 'non-veg'},
                    {'name': 'Paneer Tikka with Salad', 'ingredients': ['Paneer','Mixed Vegetables'], 'prep_time': 22, 'category': 'veg'}
                ]
            }
        }

    def _initialize_allergy_substitutes(self):
        return {
            'gluten': {
                'avoid': ['wheat', 'barley'],
                'substitutes': {'Bread': 'Rice'}
            },
            'dairy': {
                'avoid': ['milk', 'cheese'],
                'substitutes': {'Milk': 'Almond Milk'}
            },
            'nuts': {
                'avoid': ['almonds', 'walnuts'],
                'substitutes': {'Almonds': 'Seeds'}
            },
            'shellfish': {
                'avoid': ['shrimp'],
                'substitutes': {'Shrimp': 'Chicken'}
            },
            'eggs': {
                'avoid': ['eggs'],
                'substitutes': {'Eggs': 'Tofu'}
            },
            'soy': {
                'avoid': ['tofu'],
                'substitutes': {'Tofu': 'Chicken'}
            }
        }

    # ---------------------------------------------------
    # CORE LOGIC
    # ---------------------------------------------------

    def calculate_daily_needs(self, gender, weight, height, age, activity_level, goals):

        if gender == 'Male':
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161

        activity = {
            'Sedentary': 1.2,
            'Lightly Active': 1.375,
            'Moderately Active': 1.55,
            'Very Active': 1.725
        }

        calories = int(bmr * activity.get(activity_level, 1.375))

        return {
            'calories': calories,
            'protein_g': int(calories * 0.3 / 4),
            'carbs_g': int(calories * 0.4 / 4),
            'fat_g': int(calories * 0.3 / 9),
            'fiber_g': 30
        }

    def filter_foods_by_allergies(self, allergies, diet_pref='Any'):

        # Flatten the database (each top-level value is a list of foods)
        all_foods = []
        for cat_list in self.food_database.values():
            all_foods.extend(cat_list)

        safe = []
        for food in all_foods:
            safe_flag = True
            name = food['name'].lower()

            for allergy in allergies:
                avoid_list = self.allergy_substitutes.get(allergy, {}).get('avoid', [])
                if any(a in name for a in avoid_list):
                    safe_flag = False

            # Diet preference filter
            cat = food.get('category', 'veg')
            if diet_pref == 'Vegetarian' and cat == 'non-veg':
                safe_flag = False
            if diet_pref == 'Non-Vegetarian' and cat == 'veg':
                safe_flag = False

            if safe_flag:
                safe.append(food)

        return safe

    def generate_meal_plan(self, needs, safe_foods, goals, days=7, diet_pref='Any'):

        if "Muscle Gain" in goals:
            templates = self.meal_templates['muscle_gain']
        elif "Weight Loss" in goals:
            templates = self.meal_templates['weight_loss']
        else:
            templates = self.meal_templates['diabetes_management']

        food_lookup = {f['name']: f for f in safe_foods}

        plan = {}

        for d in range(1, days + 1):

            daily_meals = {}
            used = set()

            for meal_type in ['breakfast', 'lunch', 'dinner']:

                options = templates[meal_type]
                # Filter template options by diet preference when possible
                if diet_pref in ['Vegetarian', 'Non-Vegetarian']:
                    req_cat = 'veg' if diet_pref == 'Vegetarian' else 'non-veg'
                    filtered = [o for o in options if o.get('category') == req_cat]
                    if filtered:
                        options = filtered
                random.shuffle(options)

                for opt in options:
                    if opt['name'] not in used:
                        selected = opt
                        used.add(opt['name'])
                        break

                nutrition = {'calories': 0, 'protein': 0, 'carbs': 0, 'fat': 0, 'fiber': 0}
                ingredients = []

                for ing in selected['ingredients']:
                    if ing in food_lookup:
                        info = food_lookup[ing]
                        ingredients.append(ing)
                        nutrition['calories'] += info['calories_per_100g']
                        nutrition['protein'] += info['protein']
                        nutrition['carbs'] += info['carbs']
                        nutrition['fat'] += info['fat']
                        nutrition['fiber'] += info['fiber']

                daily_meals[meal_type] = {
                    'name': selected['name'],
                    'ingredients': ingredients,
                    'prep_time': selected['prep_time'],
                    'nutrition': nutrition
                }

            plan[f"Day {d}"] = daily_meals

        return plan

    # ---------------------------------------------------
    # UI
    # ---------------------------------------------------

    def display_meal_planner_interface(self):

        st.markdown("""
        <h2><i class="fa-solid fa-utensils"></i> Personalized Meal Planner</h2>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<h4><i class='fa-solid fa-user'></i> Personal Information</h4>", unsafe_allow_html=True)
            gender = st.selectbox("Gender", ["Male", "Female"])
            age = st.slider("Age", 1, 120, 30)
            weight = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
            height = st.number_input("Height (cm)", 120.0, 220.0, 170.0)
            activity = st.selectbox(
                "Activity Level",
                ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"]
            )

        with col2:
            st.markdown("<h4><i class='fa-solid fa-bullseye'></i> Health Goals & Conditions</h4>", unsafe_allow_html=True)

            goals = st.multiselect(
                "Health Goals",
                ["Weight Loss", "Muscle Gain", "Weight Maintenance",
                 "Blood Sugar Control", "Diabetes Management", "Heart Health"]
            )

            diet_pref = st.selectbox("Diet Preference", ["Any", "Vegetarian", "Non-Vegetarian"])

            allergies = st.multiselect(
                "Food Allergies",
                ["gluten", "dairy", "nuts", "shellfish", "eggs", "soy"]
            )

        if st.button("Generate Meal Plan", type="primary"):

            needs = self.calculate_daily_needs(
                gender, weight, height, age, activity, goals
            )

            safe_foods = self.filter_foods_by_allergies(allergies, diet_pref=diet_pref)

            plan = self.generate_meal_plan(needs, safe_foods, goals, diet_pref=diet_pref)

            self._display_results(needs, plan)

    def _display_results(self, needs, plan):

        st.success("Meal plan generated successfully")

        st.markdown("<h4><i class='fa-solid fa-chart-column'></i> Daily Targets</h4>", unsafe_allow_html=True)

        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("Calories", needs['calories'])
        c2.metric("Protein", f"{needs['protein_g']} g")
        c3.metric("Carbs", f"{needs['carbs_g']} g")
        c4.metric("Fat", f"{needs['fat_g']} g")
        c5.metric("Fiber", f"{needs['fiber_g']} g")

        st.markdown("<h4><i class='fa-solid fa-calendar-days'></i> Weekly Plan</h4>", unsafe_allow_html=True)

        tabs = st.tabs(list(plan.keys()))

        for i, (day, meals) in enumerate(plan.items()):
            with tabs[i]:
                for meal, info in meals.items():
                    with st.expander(f"{meal.title()} - {info['name']}"):
                        st.write("Ingredients:", ", ".join(info['ingredients']))
                        st.write("Prep time:", info['prep_time'], "min")
