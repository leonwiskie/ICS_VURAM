import streamlit as st
import pandas as pd

dict_safety = {
"None": "Exploitation of process(es) leads to no environmental and/or physical damage.",
"Low": "Exploitation of process leads to possible minor environmental and/or physical damage.",
"Medium": "Exploitation of process(es) leads to possible major environmental and/or hospitalization.",
"High": "Exploitation of process leads to possible major environmental and/or possible loss of life."
}

dict_availability = {
"None": "Exploitation has no effect on continuation non-critical and critical process(es).",
"Low": "Exploitation leads to acceptable down-time of non-critical process(es).",
"Medium": "Exploitation leads to unacceptable down-time of critical process(es) and possible degradation of services.",
"High": "Exploitation leads to failing of critical process(es) and overall failing of services."
}

dict_reliability = {
"None": "Exploitation has no effect on process output of non-critical and critical process(es).",
"Low": "Exploitation leads to manageable errors in process output.",
"Medium": "Exploitation leads to loss of control of non-critical process(es) and unacceptable degradation of process output.",
"High": "Exploitation leads to loss of control of critical process(es) and causes process defects."
}

dict_posture = {
"None": "The vulnerability does not reduce the security posture of the system: The system lacks any form of authentication. The system uses insecure protocols. The system version is out of support. A publicly accessible exploit against the current system version exists.",
"Low": "The vulnerability marginally reduces the security posture of the system: The system lacks strong password requirements. The system uses insecure protocols. The system version is out of support. The current system version contains five or more vulnerabilities No exploits are publicly available for current system version.",
"Medium": "The vulnerability reduces the security posture of the system: The system uses strong password requirements. The system uses secure protocols. The current system version contains one vulnerability. No exploits are publicly available for current system version.",
"High": "The vulnerability critically reduces the security posture of the system: The system uses strong password requirements and MFA. The system uses secure protocols The current system version contains no vulnerabilities. No exploits are publicly available for current system version The system's security is audited every year."
}


dict_exposure = {
"None":"System is situated in segmented zone and has no connection to other systems.",
"Low": "System is in segmented zone but does have connection to other systems.",
"Medium": "System is directly connected to Perimeter System within its zone.",
"High": "System is a Perimeter System (connection to enterprise environment or external vendor system e.g. via modem)."
}

dict_exploit = {
"None": "No known exploits or details available.",
"Low": "Only proof of concept available.",
"Medium": "Exploit is publicly available, but requires modification and/or testing.",
"High": "Automated exploit or toolkit available."
}

dict_patch = {
"None": "Patch is available and tested locally.",
"Low": "Patch is available and is tested by trusted source.",
"Medium": "Patch is available but not tested.",
"High": "No patch available." 
}

series_safety = pd.Series(dict_safety)
series_avail = pd.Series(dict_availability)
series_relia = pd.Series(dict_reliability)
series_posture = pd.Series(dict_posture)
series_exposure = pd.Series(dict_exposure)
series_exploit = pd.Series(dict_exploit)
series_patch = pd.Series(dict_patch)

st.header("Risk Levels")

st.write("Below are the risk levels for each criterium used in the assessment. Each criterium has four risk levels with corresponding text.")

tab1, tab2, tab3 = st.tabs(["Impact", "System Security", "Exploitability"])

with tab1:
    col1, col2, col3  = st.columns(3, gap="small")

    with col1:
        st.header("Impact on Safety")
        st.table(series_safety)

    with col2:
        st.header("Impact on Availability")
        st.table(series_avail)
    
    with col3:
        st.header("Impact on Reliability")
        st.table(series_relia)


with tab2:
    col1, col2  = st.columns(2, gap="small")

    with col1:
        st.header("Security Posture")
        st.table(series_posture)

    with col2:
        st.header("Exposure")
        st.table(series_exposure)


with tab3:
    col1, col2  = st.columns(2, gap="small")

    with col1:
        st.header("Exploit")
        st.table(series_exploit)

    with col2:
        st.header("Patch Status")
        st.table(series_patch)


