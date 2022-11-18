import streamlit as st
import nvdlib


st.set_page_config(
    page_title = "ICS-VuRAM"
)

st.title("ICS VuRAM: Industrial Vulnerability Risk Assessment Tool")

def get_cve_number():
    cve_number = st.text_input(label="Please enter your CVE number here :", key=st.session_state["cve"], placeholder=f"use CVE-XXXX-XXXX", )
    if not cve_number:
        st.stop()
    cve_number = cve_number.upper()
    return cve_number

def find_cve_number(cve_number):
    try:
        len(cve_number) <= 15 and cve_number.startswith('CVE')
        with st.spinner(text="In progress..."):
            request = nvdlib.getCVE(cve_number)
            st.write("CVSSv3 : " + request.v3severity + ' - ' + str(request.v3score))
            st.write(request.cve.description.description_data[0].value)
            st.success("Thank you! Go to the Assessment.")
        st.session_state["cve"] = cve_number
        #st.write(st.session_state["cve"])

    except:
        st.error("CVE not found. Please enter the CVE correctly.") 


### CVE Information
start_option = st.radio("Do you have a CVE Number?", ("Yes", "No"))

if 'cve' not in st.session_state:
    st.session_state['cve'] = ""

if start_option == "Yes":
    cve = get_cve_number()
    find_cve_number(cve)
   
    
else:
    st.success("Thank you! Go to the Assessment.")
    #st.write(st.session_state)
