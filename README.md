# ICS_VURAM
Assessment Tool for ICS vulnerabilities

The ICS-VURAM Model uses Anaytical Hierachy Process (AHP) to rank the various factors used to
determine the risk of a vulnerability of an Industrial Control System. AHP is a multi criteria decision making approach that 
allows users to select the most siutable option based on a number of criteria that influence the decision. 
AHP ranks the various factors in a hierarchical order and attaches weights to the various factors selected in the model. 
Below is the hierrachy of the factors used in this model. The AHP scores for the model were calculated with AHP OS: https://bpmsg.com/ahp/.

# Using the Model

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

The ICS-VURAM Model uses 8 factors that determine the risk of a vulnerability. The factors were selected after various interviews with ICS security experts. This model is not a exhaustive list of risk factors for each ICS but a manageable and easy to operate group of important criteria that infleucne the risk a vulnerability poses to the system and the organization.

Impact Metrics - Human and Environmental Safety Impact, Process Reliability, Process Availability
System Security Metrics - Security Posture, Visibility, Exposure
Exploitability Metrics - Exploit Skill Level, Patch Status


# Vulnerability Advice

Corresponding to the risk of the vulnerability, the model uses 4 different advices on how to best approach the assessed vulnerability. 
The advices correspond with the patch risk levels of the IEC-62443 3-2, a well known standard for ICS security. Below are the 4 advices the model can produce.

Vulnerability Advice:
-   Accept Vulnerability Risk
-   Resolve or mitigate vulnerability risk in 1 year, or during next scheduled
    maintenance cycle.
-   Resolve or mitigate vulnerability risk within 3 months.
-   Resolve or mitigate vulnerability risk immediately.

# Using docker for development
build the container image:  
docker build -t ics_vuram:latest .

and starting the app container:
docker run -dp 8501:8501 ics_vuram:latest
