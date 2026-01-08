import streamlit as st 

st.subheader('Calculate BMI(Body Mass Index) \n\n')
st.write("Have a look at the chart displaying the different BMI ranges according to their respective weight categories.\n\n")
st.image('ranges.png')

height = st.number_input("Enter your height in(cms): ", min_value=100)
weight = st.number_input("Enter your weight in kgs: ", min_value=1)
def bmi(height, weight):
      value = weight/((height/100)**2)
      return value*(1.0)
def category(person_bmi):
    if person_bmi<16:
        return ("Severe Thinness")
    elif person_bmi>=16 and person_bmi<17:
        return ("Moderate Thinness")
    elif person_bmi>=17 and person_bmi<18.5:
        return ("Mild Thinness")

    elif person_bmi>=18.5 and person_bmi<25:
        return ("Normal")


    elif person_bmi>=25 and person_bmi<30:
        return ("Overweight")


    elif person_bmi>=30 and person_bmi<35:
        return ("Obese Class I")

    elif person_bmi>=35 and person_bmi<40:
        return ("Obese Class II")

    else:
        return ("Obese Class III")
    

person_bmi = bmi(height, weight)
st.write("Your BMI is "+str(person_bmi)+' kg/m2')
st.write("You lies under the category of " + category(person_bmi))


st.subheader('\n\nCalculate BMR(Basal Metabolic Rate)\n\n')
age = st.number_input("Enter your age: ")
gender = st.text_input("Enter your gender Either('M' or 'F'): ")
if gender == 'M':
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
else:
    bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

lifestyle = st.selectbox('Choose the lifestyle', options=['sedentary (little or no exercise)', 'lightly active (light exercise or sports 1-3 days/week)', 'moderately active (moderate exercise 3-5 days/week)', 'very active (hard exercise 6-7 days/week)','super active (very hard exercise and a physical job)'])

if lifestyle == 'sedentary (little or no exercise)':
    bmr = bmr*1.2
elif lifestyle == 'lightly active (light exercise or sports 1-3 days/week)':
    bmr = bmr*1.375
elif lifestyle == 'moderately active (moderate exercise 3-5 days/week)':
    bmr  = bmr*1.55
elif lifestyle == 'very active (hard exercise 6-7 days/week)':
    bmr = bmr*1.725
else:
    bmr =bmr*1.9

st.text(f'Your daily calories consumption is {bmr} kcal per day')


