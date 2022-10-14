from gettext import find
from requests import session
import streamlit as st
import json
from streamlit_echarts import st_echarts

advices = ['Accept Vulnerability Risk',
            'Resolve or mitigate vulnerability risk in 1 year, or during next scheduled maintenance cycle',
            'Resolve or mitigate vulnerability risk within 3 months',
            'Resolve or mitigate vulnerability risk immediately.'
            ]


risk_levels = {
"dict_safety":{
"None": "Exploitation of process(es) leads to no environmental and/or physical damage.",
"Low": "Exploitation of process leads to possible minor environmental and/or physical damage.",
"Medium": "Exploitation of process(es) leads to possible major environmental and/or hospitalization.",
"High": "Exploitation of process leads to possible major environmental and/or possible loss of life."
},
"dict_availability":{
"None": "Exploitation has no effect on continuation non-critical and cdict_safetyritical process(es).",
"Low": "Exploitation leads to acceptable down-time of non-critical process(es).",
"Medium": "Exploitation leads to unacceptable down-time of critical process(es) and possible degradation of services.",
"High": "Exploitation leads to failing of critical process(es) and overall failing of services."
},
"dict_reliability":{
"None": "Exploitation has no effect on process output of non-critical and critical process(es).",
"Low": "Exploitation leads to manageable errors in process output.",
"Medium": "Exploitation leads to loss of control of non-critical process(es) and unacceptable degradation of process output.",
"High": "Exploitation leads to loss of control of critical process(es) and causes process defects."
},
"dict_posture":{
"None": "The vulnerability does not reduce the security posture of the system: The system lacks any form of authentication. The system uses insecure protocols. The system version is out of support. A publicly accessible exploit against the current system version exists.",
"Low": "The vulnerability marginally reduces the security posture of the system: The system lacks strong password requirements. The system uses insecure protocols. The system version is out of support. The current system version contains five or more vulnerabilities No exploits are publicly available for current system version.",
"Medium": "The vulnerability reduces the security posture of the system: The system uses strong password requirements. The system uses secure protocols. The current system version contains one vulnerability. No exploits are publicly available for current system version.",
"High": "The vulnerability critically reduces the security posture of the system: The system uses strong password requirements and MFA. The system uses secure protocols The current system version contains no vulnerabilities. No exploits are publicly available for current system version The system's security is audited every year."
},
"dict_exposure":{
"None":"System is situated in segmented zone and has no connection to other systems.",
"Low": "System is in segmented zone but does have connection to other systems.",
"Medium": "System is directly connected to Perimeter System within its zone.",
"High": "System is a Perimeter System (connection to enterprise environment or external vendor system e.g. via modem)."
},
"dict_exploit":{
"None": "No known exploits or details available.",
"Low": "Only proof of concept exploit code available.",
"Medium": "Exploit code is publicly available, but requires modification and/or testing.",
"High": "Automated exploit or toolkit available."
},
"dict_patch":{
"None": "Patch is available and tested locally.",
"Low": "Patch is available and is tested by trusted source.",
"Medium": "Patch is available but not tested.",
"High": "No patch available." 
}
}


results = {"S":1, "A":1, "R":1, "Po":1, "Sg":1, "E":1, "P":1}

scores = {"S":1, "A":1, "R":1, "Po":1, "Sg":1, "V":1, "E":1, "P":1}

mapping = {1:"None", 2:"Low", 3:"Medium", 4:"High"}

#https://discuss.streamlit.io/t/unique-key-for-every-items-in-radio-button/20654/3

### Session State 

#st.write(st.session_state['cve'])

### Assessment

def show_options(option, result):
    choice = st.radio(option, (mapping), index=1, format_func=lambda x: mapping[x], horizontal=True)
    results[result] = choice
    return choice

def show_expander(dict, criterion):
    with st.expander("Risk Levels" + " " + criterion):
        st.write(dict)


with st.form('Assessing Vulnerabilities in ICSs'):

    st.header('Impact Criteria')

    show_expander(risk_levels['dict_safety'], 'Impact on Process Safety')

    st.write('You Selected : ', show_options('Select Impact on Process Safety', 'S'))

    show_expander(risk_levels['dict_availability'], 'Impact on Process Availability')

    st.write('You Selected : ', show_options('Select Impact on Process Availability', 'A'))

    show_expander(risk_levels['dict_reliability'], 'Impact on Process Reliability')

    st.write('You Selected : ', show_options('Select Impact on Process Reliability', 'R'))

    st.header('System Security Criteria')

    show_expander(risk_levels['dict_posture'], 'Security Posture')

    st.write('You Selected : ', show_options('Select Security Posture', 'Po'))

    show_expander(risk_levels['dict_exposure'], 'Exposure')

    st.write('You Selected : ', show_options('Select Exposure', 'Sg'))

    st.header('Exploitability Criteria')

    show_expander(risk_levels['dict_exploit'], 'Exploit Skill Level')

    st.write('You Selected : ', show_options('Exploit Skill Level', 'E'))

    show_expander(risk_levels['dict_patch'], 'Patch Status')

    st.write('You Selected : ', show_options('Patch Status', 'P'))

    submitted = st.form_submit_button('Submit')


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
                        {"value": results['E'], "name": "Exploit Skill Level"},
                        {"value": results['P'], "name": "Patch Status"},
                    ],
                }
            ],
        }
        st_echarts(
            options=option, height="400px",
        )

    ### Match Results with AHP scores

    scores['S'] = results['S'] * 0.336
    scores['A'] = results['A'] * 0.107
    scores['R'] = results['R'] * 0.09
    scores['Po'] = results['Po'] * 0.05
    scores['Sg'] = results['Sg'] * 0.261
    scores['E'] = results['E'] * 0.131
    scores['P'] = results['P'] * 0.025

    score = sum(scores.values())

    ### Match advice with produced score of the risk levels

    if score <= 2.0:
        advice = advices[0]
    elif score <= 3.0:
        advice = advices[1]
    elif score <= 4.0:
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

cve_number = st.session_state['cve']

st.download_button(
label='Download JSON',
file_name= 'ics_vucram-'+ cve_number + '.json',
mime="application/json",
data=json_file
)
