
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Mental Health in Tech",
    page_icon="🧠",
    layout="wide"
)

# Load dataset
df = pd.read_csv("survey.csv")

# Title
st.title("🧠 Mental Health in Tech Survey")
st.subheader("Exploratory Data Analysis Dashboard")

st.write(
    "This dashboard presents an interactive analysis of the "
    "2014 Mental Health in Tech Survey."
)

# Dataset overview
st.header("Dataset Overview")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Respondents", df.shape[0])

with col2:
    st.metric("Total Variables", df.shape[1])

# Age distribution
st.header("Age Distribution")

fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(df["Age"], bins=20, kde=True, ax=ax)
ax.set_xlabel("Age")
ax.set_ylabel("Number of Respondents")
st.pyplot(fig)

# Gender distribution
st.header("Gender Distribution")

gender_counts = df["Gender"].value_counts()

fig, ax = plt.subplots(figsize=(10, 5))
gender_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Gender")
ax.set_ylabel("Number of Respondents")
plt.xticks(rotation=45)
st.pyplot(fig)

# Treatment distribution
st.header("Mental Health Treatment")

treatment_counts = df["treatment"].value_counts()

fig, ax = plt.subplots(figsize=(7, 5))
treatment_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Sought Treatment")
ax.set_ylabel("Number of Respondents")
plt.xticks(rotation=0)
st.pyplot(fig)

# Remote work
st.header("Remote Work Distribution")

remote_counts = df["remote_work"].value_counts()

fig, ax = plt.subplots(figsize=(7, 5))
remote_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Remote Work")
ax.set_ylabel("Number of Respondents")
plt.xticks(rotation=0)
st.pyplot(fig)

# Key findings
st.header("Key Findings")

st.write("""
- The dataset contains 1,259 survey responses.
- Respondents represent different age and gender groups.
- The survey includes information about mental-health treatment and workplace support.
- Workplace factors such as remote work, company size, benefits and wellness programs can be explored.
- The analysis identifies patterns and associations rather than cause-and-effect relationships.
""")
