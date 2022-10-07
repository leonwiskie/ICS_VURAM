import streamlit as st
import json
import nvdlib
from streamlit_echarts import st_echarts

advices = ['Accept Vulnerability Risk',
            'Resolve or mitigate vulnerability risk in 1 year, or during next scheduled maintenance cycle',
            'Resolve or mitigate vulnerability risk within 3 months',
            'Resolve or mitigate vulnerability risk immediately.'
            ]

results = {"S":1, "A":1, "R":1, "Po":1, "Sg":1, "V":1, "E":1, "P":1}

scores = {"S":1, "A":1, "R":1, "Po":1, "Sg":1, "V":1, "E":1, "P":1}

mapping = {1:"None", 2:"Low", 3:"Medium", 4:"High"}

cve_number = "None"

#https://discuss.streamlit.io/t/unique-key-for-every-items-in-radio-button/20654/3


### CVE Information

st.title("Industrial Vulnerability Risk Assessment Tool")

start_option = st.radio("Do you have a CVE Number?", ("Yes", "No"))

if start_option == "Yes":

    user_input = st.text_input(label="Please enter your CVE number here :", placeholder=f"use CVE-XXXX-XXXX")

    if not user_input:
        st.stop()

    cve_number = user_input.upper()

    try:
        len(cve_number) <= 12 and cve_number.startswith('CVE')

        with st.spinner(text="In progress..."):

            request = nvdlib.getCVE(cve_number)
            st.write("CVSSv3 : " + request.v3severity + ' - ' + str(request.v3score))
            st.write(request.cve.description.description_data[0].value)
            
            st.success("Thank you! Go to the Assessment.")

    except:
        st.error("CVE not found. Please enter the CVE correctly.") 
        cve_number = "None"

else:
    st.success("Thank you! Go to the Assessment.")
    results.update({"cve":cve_number})


### Assessment

def show_options(option, result):
    choice = st.radio(option, (mapping), index=1, format_func=lambda x: mapping[x], horizontal=True)
    results[result] = choice
    return choice
    


with st.form('Assessing Vulnerabilities in ICSs'):

    st.header("Impact Criteria")

    st.write("You Selected : ", show_options('Select Impact on Safety', 'S'))

    st.write("You Selected : ", show_options('Select Impact on Availability', 'A'))

    st.write("You Selected : ", show_options('Select Impact on Reliability', 'R'))

    st.header('System Security Criteria')

    st.write("You Selected : ", show_options('Select Security Posture', 'Po'))

    st.write("You Selected : ", show_options('Select Exposure', 'Sg'))

    st.write("You Selected : ", show_options('Select Visibility', 'V'))

    st.header('Exploitability Criteria')

    st.write("You Selected : ", show_options('Exploit Skill Level', 'E'))

    st.write("You Selected : ", show_options('Patch Status', 'P'))

    submitted = st.form_submit_button("Submit")

### Print Nightingale Rose Graph to the webpage

if submitted:

    with st.container():

        st.header("Graph of Results")

        option = {
            "legend": {"top": "bottom"},
            "toolbox": {
                "show": True,
                "feature": {
                    "mark": {"show": True},
                    "dataView": {"show": True, "readOnly": False},
                    "restore": {"show": True},
                    "saveAsImage": {"show": True},
                },
            },
            "series": [
                {
                    "name": "Risk Scores",
                    "type": "pie",
                    "radius": [25, 125],
                    "center": ["50%", "50%"],
                    "roseType": "area",
                    "itemStyle": {"borderRadius": 8},
                    "data": [
                        {"value": results['S'], "name": "Impact on Safety"},
                        {"value": results['A'], "name": "Impact on Availability"},
                        {"value": results['R'], "name": "Impact on Reliability"},
                        {"value": results['Po'], "name": "Security Posture"},
                        {"value": results['Sg'], "name": "Exposure"},
                        {"value": results['V'], "name": "Visibility"},
                        {"value": results['E'], "name": "Exploit Skill Level"},
                        {"value": results['P'], "name": "Patch Status"},
                        '''
                        {"value": 30, "name": "rose 4"},
                        {"value": 28, "name": "rose 5"},
                        {"value": 26, "name": "rose 6"},
                        {"value": 22, "name": "rose 7"},
                        {"value": 18, "name": "rose 8"},
                        '''
                    ],
                }
            ],
        }
        st_echarts(
            options=option, height="400px",
        )

    ### Match Results with AHP scores

    scores['S']= results['S'] * 0.409
    scores['A'] = results['A'] * 0.062
    scores['R'] = results['R'] * 0.062
    scores['Po'] = results['Po'] * 0.019
    scores['Sg'] = results['Sg'] * 0.073
    scores['V'] = results['V'] * 0.08
    scores['E'] = results['E'] * 0.408
    scores['P'] = results['P'] * 0.058

    score = sum(scores.values())

    ### Match advice with produced score of the risk levels

    if score <= 1.5:
        advice = advices[0]
    elif score <= 2.5:
        advice = advices[1]
    elif score <= 3.5:
        advice = advices[2]
    else:
        advice = advices[3]


    ### Print Advice to the webpage

    st.header("ICS VURAM Advice")

    st.success("Advice : " + advice)

    ### Add the CVE number and advice to the JSON file

    results.update({"advice":advice})

### Download File

st.header("Download Result")

json_file = json.dumps(results, indent = 4) 

st.download_button(
label='Download JSON', 
file_name='result_vucram.json',
mime="application/json",
data=json_file
)
