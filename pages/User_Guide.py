from nbformat import write
import streamlit as st

st.title("User Guide")

st.write("In this User Guide we specify how to use the ICS Vulnerability Risk Assessment Model (ICS VURAM).")

st.header("Industrial Control Systems")

st.write('''
Industrial Control Systems require continuous, uninterrupted and unmodified functioning of the involved components. 
The main goal of ICSs is to monitor or control a physical process in an industrial setting. 
This is done by reading from and/or writing data to sensors and actuators (Hahn, 2016). 
The control systems collect from sensors and devices within the process and act when set thresholds are met. 
An ICS consists of numerous control loops, human in-the-loop involvement via a Human Machine Interface (HMI), using specifically designed protocols. 
The image below shows a simple architecture of a single ICS in Figure 4 (Bhamare et al., 2020).
''')

st.image("images/ICS architecture.png")

st.markdown('''
When discussing ICSs in this model, we focus on the systems in level 0-2 of Purdue Enterprise Reference Architecture, which are also the levels describes in the architecture sketch provided in Figure 4. On these levels, we encounter several types of ICS:
-   RTU: The function of a remote terminal unit is to collect controlled variables from field devices connected to sensors and send manipulated variables to process actuators. It also sends information control systems. The RTU is generally the one of the most basic process control devices within an architecture. It uses a microprocessor to conduct the logic within the system. 
-   PLC: A programmable logic controller is similar to an RTU but more complex. Its main function is also to collect and digitalize data gathered from the sensors and actuators and send it to the control systems and control the state of the machines. PLC’s have generally more processing power than an RTU.
-   SIS: Safety Instrumented System contains the same processing power and exterior as a PLC or RTU. However, the main function of a SIS is to control the various safety states of a process. The system directs a process to go in fail-safe mode when certain thresholds are met that indicate a disturbance such as loss of control or malfunctioning. The SIS is often more hardened than other ICSs due to its importance for process safety. 
-   HMI: A Human Machine interface is a system that uses a touch screen panel that allows operators to read data and control systems such as RTUs and PLCs. It presents the information to operators through visualizations such as diagrams, charts and allows control through digital buttons and dials.
-   SCADA: Supervisory Control and Data Acquisition are centralized systems that support the coordination of processes. SCADA is the central point of process data collection and process control within an infrastructure.  As with the HMI’s, SCADA provides operators with information through diagrams and charts. 
-   DCS: The Distributed Control System is strongly related to SCADA systems and the terms are often used interchangeably. One distinction is that generally SCADA are event driven, focusing on scheduled and unscheduled events created by monitoring a process, whereas DCS focuses on the state a process is in. However, such distinctions are not definitive to separate a DCS from a SCADA.
'''
)

st.header("Analytical Hierarchy Process")

st.write('''
The ICS-VURAM Model uses Anaytical Hierachy Process (AHP) to rank the various factors used to
determine the risk of a vulnerability of an Industrial Control System. AHP is a multi criteria decision making approach that 
allows users to select the most siutable option based on a number of criteria that influence the decision. 
AHP ranks the various factors in a hierarchical order and attaches weights to the various factors selected in the model. 
Below is the hierrachy of the factors used in this model. The AHP scores for the model were calculated with AHP OS: https://bpmsg.com/ahp/.
'''
)

st.image("images/AHP_scores.png")

st.header("Using the Model")

st.write('''
Step 1: Getting information
The Model starts at the Home Page where the user can insert an CVE number to gather the CVSS score of the vulnerability and some background information.

Step 2: Determine the Risk
The user goes to the Assessment Page where per factor there are 4 risk scores that guide the user in estimating the correct risk level for that factor. Corresponding text for each risk level can be found at the 
Risk Levels page. There the user can find an explanation of each factors Risk Level and select the most appropiate one. 

Step 3: Gaining Advice
After entering the risk levels the model produces an advice for the user. There are 4 different advices that the model can produce, based on the appropiate risk level. Vulnerbailities that have high risk levels are adviced to remediate or resolve quickly, 
whereas vulnerabilities that are less important can be accepted or resolved during the next maintenance cycle. 

The ICS-VURAM Model also produces a diagram that shows the risk level score of each factor. 


Step 4: Download the Result
The results of the assessment can be downloaded on the bottom of the Assessment Page in JSON format. The user receives the CVE-number, the risk levels for each factor and the corresponding advice.

''')

st.subheader("Risk Factors")

st.write("The ICS-VURAM Model uses 8 factors that determine the risk of a vulnerability. The factors were selected after various interviews with ICS security experts. \
This model is not a exhaustive list of risk factors for each ICS but an manageable and easy to operate group of important criteria that infleucne the risk a vulnerability poses to the system and the organization")

st.write(
    {'Impact Metrics': ['Human and Environmental Safety Impact', 'Process Reliability', 'Process Availability']},
    {'System Security Metrics':['Security Posture', 'Visibility', 'Exposure']},
    {'Exploitability Metrics': ['Exploit Skill Level', 'Patch Status']})


st.subheader(" Vulnerability Advice")

st.write("Corresponding to the risk of the vulnerability, the model uses 4 different advices on how to best approach the assessed vulnerability. \
    The advices correspond with the patch risk levels of the IEC-62443 3-2, a well known standard for ICS security. Below are the 4 advices the model can produce.")

st.markdown(
"""
Vulnerability Advice:
-   Accept Vulnerability Risk
-   Resolve or mitigate vulnerability risk in 1 year, or during next scheduled
    maintenance cycle.
-   Resolve or mitigate vulnerability risk within 3 months.
-   Resolve or mitigate vulnerability risk immediately.
"""
)


