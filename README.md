Mental Health in Tech Survey EDA Analysis

Prepared by: Manjula. M

Domain: DA/BA

Date: 19-09-2026

GitHub Link: https://github.com/Manjula1989/Mental-Health-in-Tech-Survey.git

# Project Summary

Mental health is an important aspect of employee well-being, especially in the technology workplace. This project performs Exploratory Data Analysis (EDA) on the 2014 Mental Health in Tech Survey dataset, which contains 1,259 responses and 27 variables related to demographics, employment, mental-health treatment and workplace support.

The analysis focuses on understanding patterns and associations between factors such as age, gender, family history, treatment, company size, remote work, mental-health benefits, care options and workplace attitudes.

Data cleaning and preprocessing are performed by handling missing values, correcting invalid age values, standardizing gender categories and creating age groups. Univariate, Bivariate and Multivariate visualizations are then used to explore the data.

The analysis also includes a categorical association heatmap and pair plot to examine relationships between important variables. The findings provide insights into mental-health treatment patterns and workplace experiences and can help organizations better understand employee mental-health support needs.

Overall, this project demonstrates how EDA can be used to clean, visualize and interpret survey data and identify meaningful patterns and associations in the technology workplace.

# Problem Statement

Mental health is an important concern in the technology workplace. Employees may experience different levels of mental-health awareness, support and willingness to seek treatment.

The objective of this project is to analyze the Mental Health in Tech Survey data and identify meaningful patterns and associations between employee demographics, workplace factors and reported mental-health treatment.

# Business Use Cases

Understand mental-health treatment patterns among technology workers.
Analyze how demographic factors such as age and gender relate to treatment responses.
Examine the relationship between family history and mental-health treatment.
Understand how workplace factors such as company size, remote work and technology-company status are represented.
Analyze the availability of mental-health benefits, care options and wellness programs.
Understand employee attitudes towards discussing mental-health issues with coworkers and supervisors.
Identify workplace factors that may require greater mental-health awareness and support.
# Business Objective

The objective of this project is to analyze the 2014 Mental Health in Tech Survey and identify meaningful patterns and associations related to mental-health treatment and workplace experiences.

The analysis focuses on:

Demographic characteristics of respondents.
Mental-health treatment and family history.
Workplace factors such as company size and remote work.
Mental-health benefits, care options and wellness programs.
Work interference and workplace attitudes.
Associations among important categorical variables.
Patterns that can help organizations better understand workplace mental-health experiences.

[ ]

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Display all columns while exploring the dataset
pd.set_option('display.max_columns', None)

# Display floating-point values with two decimal places
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# Set a consistent visualization style
sns.set_style("whitegrid")

print("Libraries imported successfully.")
Libraries imported successfully.

[ ]
# ============================================================
# DATASET LOADING
# ============================================================

from google.colab import files

uploaded = files.upload()

# Load the uploaded CSV file
df = pd.read_csv('survey.csv')

print("Dataset loaded successfully.")
print("Shape of the dataset:", df.shape)


[ ]
# Display the first five records of the dataset

df.head()


[ ]
# Display the last five records of the dataset

df.tail()


[ ]
# ============================================================
# DATASET ROWS AND COLUMNS
# ============================================================

rows, columns = df.shape

print("Number of rows:", rows)
print("Number of columns:", columns)
Number of rows: 1259
Number of columns: 27

[ ]
# Display basic information about the dataset

df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1259 entries, 0 to 1258
Data columns (total 27 columns):
 #   Column                     Non-Null Count  Dtype 
---  ------                     --------------  ----- 
 0   Timestamp                  1259 non-null   object
 1   Age                        1259 non-null   int64 
 2   Gender                     1259 non-null   object
 3   Country                    1259 non-null   object
 4   state                      744 non-null    object
 5   self_employed              1241 non-null   object
 6   family_history             1259 non-null   object
 7   treatment                  1259 non-null   object
 8   work_interfere             995 non-null    object
 9   no_employees               1259 non-null   object
 10  remote_work                1259 non-null   object
 11  tech_company               1259 non-null   object
 12  benefits                   1259 non-null   object
 13  care_options               1259 non-null   object
 14  wellness_program           1259 non-null   object
 15  seek_help                  1259 non-null   object
 16  anonymity                  1259 non-null   object
 17  leave                      1259 non-null   object
 18  mental_health_consequence  1259 non-null   object
 19  phys_health_consequence    1259 non-null   object
 20  coworkers                  1259 non-null   object
 21  supervisor                 1259 non-null   object
 22  mental_health_interview    1259 non-null   object
 23  phys_health_interview      1259 non-null   object
 24  mental_vs_physical         1259 non-null   object
 25  obs_consequence            1259 non-null   object
 26  comments                   164 non-null    object
dtypes: int64(1), object(26)
memory usage: 265.7+ KB

[ ]
# Display the data types of all variables

df.dtypes


[ ]
# Display the number of unique values in each column

df.nunique()


[ ]
# Display the basic statistical summary of numerical variables

df.describe()


[ ]
# ============================================================
# CHECK DUPLICATE RECORDS
# ============================================================

duplicate_count = df.duplicated().sum()

print("Number of duplicate rows:", duplicate_count)
Number of duplicate rows: 0

[ ]
# ============================================================
# CHECK MISSING VALUES
# ============================================================

missing_values = df.isnull().sum()

missing_summary = pd.DataFrame({
    'Missing Values': missing_values,
    'Missing Percentage': (missing_values / len(df)) * 100
})

missing_summary = missing_summary.sort_values(
    by='Missing Values',
    ascending=False
)

missing_summary


[ ]
# ============================================================
# VISUALIZE MISSING VALUES
# ============================================================

plt.figure(figsize=(14, 6))

missing_percent = (
    df.isnull().mean() * 100
).sort_values(ascending=False)

missing_percent = missing_percent[missing_percent > 0]

sns.barplot(
    x=missing_percent.values,
    y=missing_percent.index
)

plt.title("Percentage of Missing Values by Column")
plt.xlabel("Missing Values (%)")
plt.ylabel("Column")

plt.tight_layout()
plt.show()


[ ]
# Display all columns in the dataset

print("Number of columns:", len(df.columns))
print("\nColumn names:\n")

for i, column in enumerate(df.columns, start=1):
    print(f"{i}. {column}")
Number of columns: 27

Column names:

1. Timestamp
2. Age
3. Gender
4. Country
5. state
6. self_employed
7. family_history
8. treatment
9. work_interfere
10. no_employees
11. remote_work
12. tech_company
13. benefits
14. care_options
15. wellness_program
16. seek_help
17. anonymity
18. leave
19. mental_health_consequence
20. phys_health_consequence
21. coworkers
22. supervisor
23. mental_health_interview
24. phys_health_interview
25. mental_vs_physical
26. obs_consequence
27. comments

[ ]
# Statistical summary of numerical variables

df.describe().T


[ ]
# Statistical summary of categorical variables

df.describe(include='object').T

Variables Description

The dataset consists of demographic, employment and mental-health-related variables collected through the Mental Health in Tech Survey.

Age represents the respondent's age, while Gender, Country and state provide demographic and geographic information. Self_employed indicates whether the respondent is self-employed.

The variables family_history and treatment capture important mental-health-related information. Work_interfere describes the extent to which a mental-health condition interferes with work.

The dataset also contains workplace-related variables such as no_employees, remote_work and tech_company. Variables including benefits, care_options, wellness_program, seek_help and anonymity provide information about the mental-health support available in the workplace.

The variables mental_health_consequence, phys_health_consequence, coworkers, supervisor, mental_health_interview, phys_health_interview and mental_vs_physical capture attitudes and perceptions regarding mental and physical health in the workplace.

The obs_consequence variable indicates whether the respondent has observed negative consequences for coworkers with mental-health conditions. The comments variable contains optional additional comments.


[ ]
# Check the number of unique values and sample unique values
# for every variable

for column in df.columns:
    print("=" * 70)
    print("Column:", column)
    print("Number of unique values:", df[column].nunique())
    print("Unique values:")
    print(df[column].dropna().unique())
    print()
======================================================================
Column: Timestamp
Number of unique values: 1246
Unique values:
['2014-08-27 11:29:31' '2014-08-27 11:29:37' '2014-08-27 11:29:44' ...
 '2015-11-07 12:36:58' '2015-11-30 21:25:06' '2016-02-01 23:04:31']

======================================================================
Column: Age
Number of unique values: 53
Unique values:
[         37          44          32          31          33          35
          39          42          23          29          36          27
          46          41          34          30          40          38
          50          24          18          28          26          22
          19          25          45          21         -29          43
          56          60          54         329          55 99999999999
          48          20          57          58          47          62
          51          65          49       -1726           5          53
          61           8          11          -1          72]

======================================================================
Column: Gender
Number of unique values: 49
Unique values:
['Female' 'M' 'Male' 'male' 'female' 'm' 'Male-ish' 'maile' 'Trans-female'
 'Cis Female' 'F' 'something kinda male?' 'Cis Male' 'Woman' 'f' 'Mal'
 'Male (CIS)' 'queer/she/they' 'non-binary' 'Femake' 'woman' 'Make' 'Nah'
 'All' 'Enby' 'fluid' 'Genderqueer' 'Female ' 'Androgyne' 'Agender'
 'cis-female/femme' 'Guy (-ish) ^_^' 'male leaning androgynous' 'Male '
 'Man' 'Trans woman' 'msle' 'Neuter' 'Female (trans)' 'queer'
 'Female (cis)' 'Mail' 'cis male' 'A little about you' 'Malr' 'p' 'femail'
 'Cis Man' 'ostensibly male, unsure what that really means']

======================================================================
Column: Country
Number of unique values: 48
Unique values:
['United States' 'Canada' 'United Kingdom' 'Bulgaria' 'France' 'Portugal'
 'Netherlands' 'Switzerland' 'Poland' 'Australia' 'Germany' 'Russia'
 'Mexico' 'Brazil' 'Slovenia' 'Costa Rica' 'Austria' 'Ireland' 'India'
 'South Africa' 'Italy' 'Sweden' 'Colombia' 'Latvia' 'Romania' 'Belgium'
 'New Zealand' 'Zimbabwe' 'Spain' 'Finland' 'Uruguay' 'Israel'
 'Bosnia and Herzegovina' 'Hungary' 'Singapore' 'Japan' 'Nigeria'
 'Croatia' 'Norway' 'Thailand' 'Denmark' 'Bahamas, The' 'Greece' 'Moldova'
 'Georgia' 'China' 'Czech Republic' 'Philippines']

======================================================================
Column: state
Number of unique values: 45
Unique values:
['IL' 'IN' 'TX' 'TN' 'MI' 'OH' 'CA' 'CT' 'MD' 'NY' 'NC' 'MA' 'IA' 'PA'
 'WA' 'WI' 'UT' 'NM' 'OR' 'FL' 'MN' 'MO' 'AZ' 'CO' 'GA' 'DC' 'NE' 'WV'
 'OK' 'KS' 'VA' 'NH' 'KY' 'AL' 'NV' 'NJ' 'SC' 'VT' 'SD' 'ID' 'MS' 'RI'
 'WY' 'LA' 'ME']

======================================================================
Column: self_employed
Number of unique values: 2
Unique values:
['Yes' 'No']

======================================================================
Column: family_history
Number of unique values: 2
Unique values:
['No' 'Yes']

======================================================================
Column: treatment
Number of unique values: 2
Unique values:
['Yes' 'No']

======================================================================
Column: work_interfere
Number of unique values: 4
Unique values:
['Often' 'Rarely' 'Never' 'Sometimes']

======================================================================
Column: no_employees
Number of unique values: 6
Unique values:
['6-25' 'More than 1000' '26-100' '100-500' '1-5' '500-1000']

======================================================================
Column: remote_work
Number of unique values: 2
Unique values:
['No' 'Yes']

======================================================================
Column: tech_company
Number of unique values: 2
Unique values:
['Yes' 'No']

======================================================================
Column: benefits
Number of unique values: 3
Unique values:
['Yes' "Don't know" 'No']

======================================================================
Column: care_options
Number of unique values: 3
Unique values:
['Not sure' 'No' 'Yes']

======================================================================
Column: wellness_program
Number of unique values: 3
Unique values:
['No' "Don't know" 'Yes']

======================================================================
Column: seek_help
Number of unique values: 3
Unique values:
['Yes' "Don't know" 'No']

======================================================================
Column: anonymity
Number of unique values: 3
Unique values:
['Yes' "Don't know" 'No']

======================================================================
Column: leave
Number of unique values: 5
Unique values:
['Somewhat easy' "Don't know" 'Somewhat difficult' 'Very difficult'
 'Very easy']

======================================================================
Column: mental_health_consequence
Number of unique values: 3
Unique values:
['No' 'Maybe' 'Yes']

======================================================================
Column: phys_health_consequence
Number of unique values: 3
Unique values:
['No' 'Yes' 'Maybe']

======================================================================
Column: coworkers
Number of unique values: 3
Unique values:
['Some of them' 'No' 'Yes']

======================================================================
Column: supervisor
Number of unique values: 3
Unique values:
['Yes' 'No' 'Some of them']

======================================================================
Column: mental_health_interview
Number of unique values: 3
Unique values:
['No' 'Yes' 'Maybe']

======================================================================
Column: phys_health_interview
Number of unique values: 3
Unique values:
['Maybe' 'No' 'Yes']

======================================================================
Column: mental_vs_physical
Number of unique values: 3
Unique values:
['Yes' "Don't know" 'No']

======================================================================
Column: obs_consequence
Number of unique values: 2
Unique values:
['No' 'Yes']

======================================================================
Column: comments
Number of unique values: 160
Unique values:
["I'm not on my company's health insurance which could be part of the reason I answered Don't know to so many questions."
 'I have chronic low-level neurological issues that have mental health side effects. One of my supervisors has also experienced similar neurological problems so I feel more comfortable being open about my issues than I would with someone without that experience. '
 "My company does provide healthcare but not to me as I'm on a fixed-term contract. The mental healthcare I use is provided entirely outside of my work."
 'Relatively new job. Ask again later'
 'Sometimes I think  about using drugs for my mental health issues. If i use drugs I feel better'
 'I selected my current employer based on its policies about self care and the quality of their overall health and wellness benefits. I still have residual caution from previous employers who ranged from ambivalent to indifferent to actively hostile regarding mental health concerns.'
 "Our health plan has covered my psychotherapy and my antidepressant medication. My manager has been aware but discreet throughout. I did get negative reviews when my depression was trashing my delivery but y'know I wasn't delivering."
 "I just started a new job last week hence a lot of don't know's"
 "In addition to my own mental health issues I've known several coworkers that may be suffering and I don't know how to tell them I empathize and that I want to help."
 'Thanks for doing this research.'
 "In Russia we have mandatory medical insurance. Every employer must pay 3.6% of every employee's salary to the insurance fund like a tax. Everyone gets free healthcare at public clinics and hospitals. Some types of healthcare including mental health are still funded from the government budget but that doesn't matter it's still FREE!However this is Russia :D I don't know much about what actually happens in mental hospitals here except that a lot of young people with male in their passports use these to avoid military draft and doctors seem to help them."
 "In my previous workplace which had mental health protections policies and access to counsellors my Director went so far as to say to me in somewhat casual conversation A woman was murdered across the street. At best though she was bipolar and at worst - who knowsI have bipolar disorder. I have zero faith that an organization with policies in place could appropriately handle mental health. I have even less faith that a workplace without the policies in place could appropriately handle mental health. I can only imagine it's worse in full tech environments."
 "I've seen negative consequences towards mental health conditions in previous workplaces.Working remote is empowering in this way."
 "I'm not a permanent employee so do not get they benefits they get.My client is extremely supportive of permanent staff with mental health issues."
 "I'd be more worried about coworkers and workplace culture than the employer--they're probably legally obligated to do some things but reputation among people I work with is something else. For instance I've heard people make snide remarks about men taking paternity leave I don't want to know what they'd say about mental health leave."
 "Had a co-worker disappear from work for a few weeks and then come back to let everyone know he was bipolar. His responsibilities and schedule were adjusted to accommodate but he got worse didn't show up didn't work etc and was eventually let go.It was tough because on the one hand he was struggling with some mental health issues but on the other hand he went through a period of months where he wasn't performing."
 "Family history of depression.  Currently dealing with depression and anxiety as well as drug addition.Employer provides & pays premiums on insurance which covers therapy and prescriptions.  Employer allows work-from-home and unlimited PTO which makes episodes easier to control.I don't speak of my problems to anyone at work except for the people that I consider friends and even then I don't go into great detail.I would never bring up a mental health issue during an interview for fear of discrimination and rejection (and therefore greater depression).  One co-worker had serious anxiety problems and would not inform his team of episodes and was eventually let go for being unresponsive."
 'I feel that my employer and colleagues have created my mental health issue. Additionally I have contributed to this by staying in the same job with the same employer for 10+ years.'
 "Many of these questions become irrelevant once 'Yes' is selected for 'Are you self-employed'.  It would be preferable for there to be a 'Not Relevant' option on these."
 "as a UK-based company we don't have any medical provisions as it's all provided on the National Health Service (for now!) However if we do need to take days off for any kind of health problems everyone is understanding :)"
 'My employer employs 17k people worldwide and my previous employer only 140 globally both have been very supportive and accommodating with my moderate depression and intense anxiety.'
 "I am not sure about my company's healthcare because I've opted out of it and I'm covered under another policy.I currently work at a great company though in past jobs I don't think I would have felt comfortable talking about mental health at all."
 'In small startups it is very hard to keep mental health issues truly private no matter what management does.'
 'A close family member of mine struggles with mental health so I try not to stigmatize it. My employers/coworkers also seem compassionate toward any kind of health or family needs.'
 "Too many people even especially IT considered mental health issues as a choice or something people can freely act about. You are depressed: take vacation. You feel weird: admit it is physical (otherwise it is not serious) go and see a doctor (and if you are on sick leave too many days you will get fired). You don't feel good today: take a holiday but don't work from home. In startup there is what I call the tyranny of happiness: you have to look happy to be accepted and to be worked with. At some point playing a role can definitely make the mental health issue worse and it is also a threat to diversity :(I don't like to call mental health issues an issue but actually when it comes to company field it too often becomes an issue and this is sad because working is sometimes better than medication. It is a vicious circle: people are scared of speaking about it so they don't inform their coworkers about what mental health is for real and so coworkers are so scared on a regular basis that the people with mental health issues keep it for themselves. "
 "My seniority at the company and rapport with the owners has helped me gain support for seeking help regarding my mental health as well as being able to take time off or work from home when an episode starts.However I don't feel that the company's stance on mental health is as clear as say something like vision or dental.  There's very much a stigma."
 "When you are an introvert people don't notice if you are depressed. Its a vicious cycle of sorts."
 "I've answered 'Yes' on remote working but 50% is the maximum time we're allowed.The branch of the company I work for doesn't offer any medical benefits. It's not as common in the UK as we have the NHS for the moment. There are international branches that may so I've answered 'Don't know'."
 'Many of these questions were difficult to answer as a self-employed person; I did my best with the available options.'
 "I tried to answer as good as possible but I am CEO of a company so many questions don't fit very well.Also many of the questions are very US-centric in most systems healthcare is not your employers business."
 "One of my coworkers has mental health issues and she's open about them (eg: my enjoyment of this project may be due to my recent change in meds). I believe the response has been generally supportive. We're a very small tight-knit company."
 'A strong mind goes a long way. Stay strong. Take some time off to help. Its all in your head. '
 'Would you bring up a mental health issue with a potential employer in an interview?Poignant.'
 'I found it difficult to answer all of the questions effectively as many of them would depend on the nature of the mental health issues as some seem more socially accepted than others. For some people telling your current supervisor that you have a history of bi-polar disorder might be easier than telling a potential employer that you have a history of compulsive gambling. They might both be bits of irrelevant information (past behavior and not indicators of future behavior). However western culture pushes us to appear as capable as possible to our supervisors in pursuit of excellence in our work. Providing information that could create a negative bias seems like a more genuine and yet more risky approach to the discussion.'
 'I have only discussed my mental illness with close family members. I feel completely uncomfortable discussing with anyone at my place of employment as I am concerned it would have negative consequences.'
 'No benefits at this organization but my employer/direct supervisor has had positive and constructive conversations with me about physical and mental health. Supervisor offered solutions advice time/energy to get help if I ever felt that needed it. (though it would have to be at my own expense). I feel safe sharing personal info with this particular person/company but this environment is the exception rather than the norm in my 15+ years as a tech worker. I would never feel safe enough to reveal info about any mental health concerns with any previous employers in the tech industry for fear of  negative perceptions job loss performance dings etc. '
 'I think I am very lucky in my workplace. Our CEO has a degree in psychology.'
 "Some of these questions were difficult to answer as being self-employed they didn't all apply to me."
 "It's a small startup in a small city in a small country."
 "Hi Ed it's Paul Dragoonis. I have Aspergers/High Functioning Autism :-)"
 'The form of mental health problem that I suffer is anxiety.'
 'The thought of going through my employer directly to get help is fucking scary.Getting help is the hardest part of getting help.'
 "Don't know because I haven't checked not because it's difficult to find out. If you didn't have the don't know option I would've looked up the answer."
 "I think there might be some bugs in my thought but I haven't sought treatment because they're not worse than annoying and I worry about having the label."
 "I think a lot of our policy is based on a situation that occurred in the past 5 years. A very public mental illness happened with a coworker that unfortunately ended negatively. It was definitely a catalyst to talking about our options but the overall sentiment of it being OK to take time off talk with your supervisors etc. has always been there. It's a great company."
 "Regardless of a stated lack of negative consequences for discussing mental health issues with coworkers/superiors unconscious bias is a very real thing - as long as I don't *need* to inform my co-workers my mental health issues do not need to be public knowledge."
 'YOU MAY WANT TO THROW OUT MY ENTRY.I answered all of these questions with the assumption that Attention Deficit Disorder is considered a mental illness and with ADD in mind.'
 'In Belgium we have all medical care so perhaps some question are not relevant'
 "A co-worker recently had mental health issues and my employer was very reasonable with them I don't know the full story but I do know that he was given ample time off and eased back in to the work place."
 'My refer to the mental health issue of depression.  I might answer differently if I was talking about a more serious issue like schizophrenia'
 'My employer does what they can providing a wellness program and pointing it out after particularly stressful times. But the interaction between the wellness program and the medical insurance is unpleasant and finding a long-term therapist / psychiatrist covered by insurance is amazingly difficult. My current lack of active treatment is due to insurance friction more than workplace friction.'
 'I work for a university.'
 "Being in Canada there are several health options that are available to Canadian citizens/perm residents for free so employers may not provide resources because they are available elsewhere. Otherwise good quiz. I hope this benefits everyone who's dealt with mental health issues in the past!"
 "I'm troubled by the way that our hiring process tends to filter out non-neurotypicals of all stripes. Competent people who act a little funny can be hard to hire."
 "In Germany your employer doesn't really provide mental health benefits. There's a standard and I get that but I would get the same at any other company in Germany."
 "fwiw I am a co founder of this company and the would you X in an interview questions shouldn't reflect how I would treat anyone addressing their own phys/mental health issue to me in such a situation. "
 "I talked to a psychiatrist once about taking medical leave for mental health issues with his referral. He was willing to help but warned me that I may not want to as he's seen that sort of thing follow people throughout their tech careers (word gets out even if it's confidential at work). I've been terrified of bringing mental health up anywhere that coworkers or potential employers could see ever since."
 'So much depends upon the organization. '
 "Now at starutp.  Previously worked at big tech company which was actually quite good at supporting mental health issues.  Still wouldn't share with bosses/other employees though as there remains a strong negative stigma."
 'Nice job on the text field for gender :-)'
 "I currently have the best managers I've ever worked with. I don't have any issues but one of my coworkers recently did and it was handled extremely well. "
 'you rock for doing this!' "I don't have a job :D"
 "Israel has public health insurance for everyone. Everyone has free mental health coverage and it's quite good. So that explains some of my answers."
 "Stigma is the worst. People first language is a small step but we can't get that right."
 '-'
 'I work for an extremely supportive company and we are amazingly open about mental health issues. Employees often share their struggles with the whole team and receive a high level of support in return.'
 'I bring up my depression in interviews solely because I have a large gap on my CV due to mental health issues which could be mistaken for a gap taken to say have children which I feel would harm my chances much more. I have other MH issues I would never bring up with employers or peers.'
 "I'm not aware of anyone with mental health issues at work it's definitely not something that's discussed publicly. There's also a lot of other personal info I don't know about my coworkers so it may just be that we tend not to talk about personal issues."
 'I suffer from mild depression and anxiety.'
 "The family history question needs a don't know option."
 "I'm afraid I haven't seen mental health issues arise at work yet. They are very accommodating with maternity leave but I don't know how that translates to anything else."
 'Mental health issue I have dealt with: acute depression'
 'Thanks for doing this. It will help end the stigma!'
 'For clarity I work at a casino.'
 'Most employers / coworkers and even immediate family is not all the time supportive to discuss depression and other problems. ie. My wife thinks she should be able to make sure that I am not depressed  which is funny because sometimes depression state has nothing to do with her. '
 'It has come to interfere with work as life progresses.Between burn out and enduring more of the work and balancing a family. Changes in my mental health have a larger pond to make ripples in.'
 'The supposed divide between mental and physical health needs to done away with and probably will be as our knowledge of the brain increases. That said we are often employed for our ability to provide value. If any issue prevents is from providing value that creates a very real challenge for the employer who is responsible to shareholders and other team members who are providing value. There are no easy answers here.'
 "Because I'm self-employed and the only person in my organization I would have liked a not applicable option. I don't want my answers to be misleading."
 "I work for a very small firm that doesn't really have a dedicated H/R person. Also for the question:If you have a mental health condition do you feel that it interferes with your work?...I don't have a diagnosed mental health condition but I suspect I might have some slight depression issues. Definitely have Imposter Syndrome."
 "I went through a divorce and was pretty depressed I went to therapy and my boss (one of the owners) was extremely supportive. I'm not sure I would have got through that rough time with out my co-workers and boss."
 "I'm diagnosed with Bipolar Disorder. My benefits for mental health exist but are terrible. The deductible is $800. I see a therapist once or twice a month at the cost of $150. The insurance company only values it at $40. My psychiatrist is $180 for 15 minutes. The insurance company values it at $80. It is IMPOSSIBLE to hit my deductible. I don't even bother making the claims."
 "We don't fucking talk about it ever."
 "thanks for what you're doing. FYI these questions dont quite work for entrepreneurs where employer == cofounders / sr mgmt / me"
 'Majority of qs on survey not relevant if you are self employed'
 "I mostly suffer from social anxiety which keeps me from attending conferences. In my small dev group a big problem is a supervisor who's a workaholic and will never say no when asked to do something so he's doing the job of at least two ppl (poorly) and working crazy hours setting the tone for the test of us that work/life balance isn't important."
 "I don't have any mental health issues but for a number of years I had to care for a family member who did and I felt that I was not able to discuss or get support from friends or colleagues in the same way that I might have if they had suffered from a physical condition."
 'I am a contractor so my lack of knowledge of workplace wellness stems directly from my lack of access to that material since I am not covered by it. I am aware that mental health services are available and am aware of a colleague who has taken a leave of absence to deal with mental health issues but am otherwise uninformed.'
 'Fully remote developer'
 "We had a developer suffer from depression and pretty hard burnout but he refused treatment even when the company said we'd foot the bill. Eventually he had to be asked to resign which was a shame. I don't know if we have any specific programs for mental health but we're definitely on the lookout for those types of issues."
 "I am a 15 year vet of the industry and I get 2 weeks of combined sick and vacation time a year and I have children to fit into that too. I've had heart problems from the stress. Fuck everything about startup culture. "
 'Italians are somewhat behind for what concerns mental health care in the workplace.  Physical health care is very much accepted with a doctor that certifies your ailment.  Mental health is treated quite differently I believe because most people are willing to admit that physical ailments should be covered while mental ailments are almost considered non-existent in most respects.  '
 "Since I am the CEO of my startup some of the would you feel comfortable and do you know the policy questions are interesting.  Of course I feel comfortable since no one can fire me and I know the policies because I chose them!However now I am curious if my employees know just how supportive the company would be of their mental health needs and this survey is making me realize that we probably haven't done a great job communicating that to everyone.  Thanks for doing this."
 "I work for the state so the health plan is large and cumbersome.  I believe it covers most medical as a state benefit but I haven't seen any promotion of it.  And it's not really the same as a tech company where I am.  We are an IT department but hardly run like any tech company around."
 'I have Narcolepsy and have been fired from a job before for falling asleep standing up during a meeting. I was standing up in the back of the room so that i could pace and try to prevent myself from falling asleep. I still managed to fall asleep while standing and fell over against the wall. I was fired the next day. The worst part is this is a condition i had given months of notice about to my boss and i reminded her of it before the meeting. I worked at a hospital at the time. I would have thought that they would be more accommodating.'
 "I feel like most of my answers were useless due to answering that I am self-employed early on. Since my employer is me... my employer does/doesn't offer mental health benefits or would I be comfortable bring it up with 'them' doesn't make sense..."
 "My current work situation was constructed in part because of my mental health issues. One of the reasons I'm self employed is to give me the most flexibility for coping with my mental health issues.I have been removed from a client project in the past because of a mental health condition. This was while I was an employee for a large consulting company. "
 'Some of these questions are not really suitable for non US people.'
 "I work for the state government. While things are slowly changing regarding covering mental health with state employees it's just not something that is acceptable in this kind of strict environment so I have to be careful about what I say and how I say it. I often take mental health days but have to call in with a physical illness because mental health problems are not acceptable excuses for using sick leave."
 'Thank you for your work what you do is important!'
 "It might be safe to talk about it where I am now but I don't know for sure and I err on the side of being over cautious. Struggle with depression and anxiety which sometimes affects my productivity but I try to make up / cover up for it instead of being open about it."
 "I'm comfortable talking about mental health with my current supervisor & my immediate at my current job but this is a first for me!"
 'None of us who are already in marginal groups in tech--the non-young the non-male the non-white--will risk our careers to admit another source of stigma: poor health.'
 "I have been incredibly public about my own struggle in my own conversations and in social media insofar as how I can use my depression to raise awareness or help others. Because of that my employer - or any future employer - kind of knows by default. It's not a secret. That said the downside of that openness is that I have no faith that I wouldn't be discriminated against at a future job simply because the information is public. Likewise I worry I'm seen as less-than by my employer in some circumstances. Regerdless I don't regret being public and raising awareness. My point is that even those of us who do publicly discuss the issue fear systemic retribution. "
 'At a previous employer I witness a bad thing happen to a coworker with mental health issues get swept under the rug... :('
 'While not personally affected I do have immediate family with mental health illness and my employer has been very supportive. Thanks for doing this survey.'
 "The company I work for was started by engineers and so anything other then the engineering department has always lacked a bit. Now that we've grown things are better but I feel that overall our total benefits package (including healthcare) isn't well communicated. This reflects negatively on the mental health questions above but would also reflect negatively on any other sort of survey about the benefits. That is I don't think the company is purposefully doing less for mental health. They just aren't doing enough across the board and that includes mental health."
 'Thank you for all you are doing to study this topic and raise awareness in our communities. '
 "The main reason for the openness answers are because of an experience with my last employer. I felt I could trust my direct supervisor so I divulged information. It ended up spreading to more supervisors and eventually my coworkers. Supers highly suggested treatment but rushed things that shouldn't have been rushed and I ended up being incorrectly treated in a psych ward and mentally scarred from the issue. I lost most of my desire to program due to the experience not to mention thousands of dollars I lost - lost work time vacation time they used for treatment time doctors expenses etc. I have major depressive disorder high anxiety and mild agoraphobia. After seeing what treatment has to offer I will likely not seek it again and continue as is. (Long story short.)"
 '(yes but the situation was unusual and involved a change in leadership at a very high level in the organization as well as an extended leave of absence)'
 "I would add that while there were negative consequences for coworkers with mental health they were given a HUGE amount of leeway.  I think the team at large tried their best to be kind but that's how the person suffered.  The company actually gave this person a lot of help.  Which was cool.  But the team still discriminated."
 'Bipolar spectrum is tricky.'
 'To be self employed helps but also brings you in touch with lots of new people that you might have to explain yourself to.'
 "A lot of these answers aren't really applicable since I'm self employed as a sole proprietor."
 'While I have not seen any direct retaliation against people with known mental illness many people do freely use insults commonly associated with mental illness (r****d for example) and criticize people behind their back for taking extra leave for doctor appointments (Oh I bet they are just hung over or other comments about how lazy they are.)'
 "My employer gives access to basic counseling and referrals but I don't know (and it's not obvious) what might be covered in the way of expenses for therapy medication etc."
 '* Small family business - YMMV.'
 "I have an exceptional employer. I haven't run into problems with any employer I've had but consider myself lucky."
 'Some of these should not be required.'
 "Though I'm in the Netherlands and chose that country from the list quite some questions are strongly geared towards the US. Over here people don't need benefits from their employer because we pay enough taxes for the government to pay for treatment of any physical or mental condition. We don't need employer approval for medical leave; that's something a qualified medical professional decides (and while on leave we still get paid our salaries something the employer can get insurance for). I answered yes to questions about these things meaning it's covered not it's covered by my employer."
 "I am a Trans woman and suffer from depression relating to that. I'm a contractor so I've answered the questions as relating to my current contract."
 'Thank you for shining a light on this topic.' ' '
 'While mental health is a part of our insurance program the UCR is 50% of 140% of medicare which means a solo mental health practitioner who will charge in my area $150-$180 a session will only result in a $45-$60 reimbursement and thus a very high out of pocket expense. This usage of a different schedule for UCR and often the lower rate is very hard to determine before purchasing insurance even in the new health insurance exchanges.'
 'My work is using my brain. I do it incredibly well.I make an effort to avoid diagnosis of anything mental health related because I am convinced it would only affect me negatively.'
 "My employer is extremely easy to work with and e.g. I have enormous leeway with flex time so I could take care of myself under that umbrella but I don't know and don't have a history of bring up mental health at the workplace so I am cautious in that area."
 "The questions related to employer-provided health benefits are largely irrelevant to where I live Australia so I'd discount them."
 'I suffered of panic attacks and agoraphobia for about 10 years.'
 "These result may be a tad confusing so a summary follows.* Currently self-employed so employer is me :)* Last place of employment was amazing when I first discovered I was bi-polar and helped me as long as I was there up to and including a mental health course for the whole team (although no mention why to others which was great).* I've never had a negative reaction yet but I know others who have.* I've been very lucky with company I keep which is why my experience is largely good."
 'I should note one of the places my employer fails with regards to mental health is that the company-paid health insurance policy does not cover trans healthcare needs.'
 'Thank you this is very important.'
 "I've never heard of a workplace that would actually allow you to call off for mental health reasons. So many places require a doctor's note for calling off sick. It's all set up to make you feel worse if you can't just suck it up. Thanks for working to change this!!!"
 'This survey was tough as a self-employed individual. You may wish to discard responses from self employed people for much of your analysis.'
 "I answered based on previous job at large technical company where I was pushed out of my role within 3 months of disclosing diagnosis.I had been struggling for 3 months prior to disclosure and was incredibly relieved when finally diagnosed. Growing up in a family open about mental health and also at the end of my rope I immediately shared with management what was going on. I requested a temporary reduced workload so I could reduce anxiety. (At time I didn't know it was anxiety as took me a year to accept that the (to me) deserved stress was anxiety caused by my core diagnosis.) When disclosing I didn't deeply understand details of the state of my mental health; I simply knew I was so stressed out by having been unable to get myself to do work in three months that I couldn't juggle all that was currently on my plate.It was at this point my direct manager and I began an almost daily struggle. After working on a single project and making progress (compared to 3 months before diagnosis when management didn't even know how bad I was doing) I requested increasing my workload. This was never granted; boss said I hadn't proved myself and implied I could not be trusted.Two huge issues stick out to me from that experience:1) Company assumes things would be better and back to 100% within months. They did not understand what one goes through when figuring out meds: things at times got worse. They did not understand how long it takes until meds are figured out: mine took two years. They most certainly would not truly understand why to this day four years later despite being stable I'm in counseling every other week in addition to being on meds. Rather than supporting that it would be seen as oh I'm sorry. I was a problem to my manager because he didn't see improvements each week.2) Accomodations.- There was no option for me to reduce work temporarily to part-time (too complicated). Instead they pushed me to take disability leave. I told them that wouldn't help; they told me to double-check with care providers. That required me to see a psychologist unnecessarily as psychologist said I didn't qualify for leave. (Expensive unnecessary appointment).- The assistance I needed the most at work was understanding: I was open but my manager told me to not tell my co-worker assigned to support me. That was disasterous for colleague's stress/frustration levels. He knew something was up but was barred from asking and I was implied it was better to keep my mouth shut.- Accommodations weren't understood by even Benefits as they're not trained in mental health nor do they have people come in to assess how they're doing in supporting those with mental health issues. Should be no different than people coming in to assess for physical accessibility of the workplace. When in a meeting with my manager supervised by HR I shouldn't feel like I'm asking too much of manager when requesting he put the negative critiques on the back burner and help me figure out whether I'm doing anything right. That this didn't stop him from coming into my office that same day and putting on my dick hat to yell at me for something that wasn't even my fault (he had brought in co-worker for this yelling and turned to finish yelling at this person): FUCKING UNACCEPTABLE.While I will never return to that company and as such took the severance package I will NEVER agree with their legal reason for being unable to do the job: me being medically disqualified from this role. I was too expensive in the short term for them; I'm not worth the cost."
 'If a man in tech is afraid of speaking up about these things it is even worse for women in tech who are already fearful of and fighting against the stigma of incompetence.  On the other hand if a female in tech does not commiserate with her male coworkers on mental health problems she will no longer be seen as a team player. It is really a catch-22 for women in STEM.'
 "Autism is a bitch for those living with it and living it. For the past years I've really been working hard to get myself (known) in the community. The people in the community that know can be counted on one hand. In general I'm not telling anyway unless it really matters and it would be a gain in some way or the other. Not because I don't trust the community members close to me but because I don't want to be that guy. And IMHO it doesn't and shouldn't matter but sadly some people are funky about that. Yet sometimes I wan't to tell everyone what I've been through and share my lessons learned."
 'This issue for me is very real at the moment. I have missed several days of work recently because of a bad reaction to a depression/anxiety drug and I hate not being able to discuss it with my boss without worrying that I will be labeled a liability. '
 'Really manager dependent. I have had managers who work with my strengths and others who want my to work on my weaknesses which are directly tied to my mental issues. '
 "Though it doesn't affect me (male) good job for making the Gender field a text input instead of a drop down of only two options."
 "I was (wrongly) diagnosed clinically depressed at 12 then bipolar I at 15 and medicated for a decade until decided myself to go drug free. Since then I've never been happier. Insomnia and my insatiablility for learning and programming have always had a symbiotic  relationship.It might also bear mentioning that I'm self-employed in addition to my more traditional day job."
 'My employer currently does not offer any health insurance I have to get that on my own.  However at past positions I have had health insurance but no one ever mentioned mental health issues nor would I wish to discuss those with my co-workers bosses etc for fear of negative reception.'
 'Mental health at work is not an issue if you leave work problems at work that may be easier for those of us not in a support role.'
 'password: testered' 'suffer from CR-PTSD so all answered based on that'
 "Since being advised by Occupational Health that the tempo and spontenaity of the office environment was likely to have a negative effect on my mental health (I'm schizoaffective) I've been moved to 100% remote (home) working. The company have furnished a home office for me and I am only required to attend the office once a month to keep in touch"
 "Despite the impression that several 'no' responses might give my employer has been very supportive. But then I work in health care."
 "When I've had a depression I was lucky to have an awesome manager who was very understanding and found a budget to pay for my therapy sessions."
 'People have often felt uncomfortable with my story while most of it happened a decade ago. I used to be quite open about it and have since kept it quietly tucked away. While I sometimes have waves of depression I have learned to cope with the affects.'
 "I burnt out this year. I worked too much had too much pressure on myself from being the sole developer on a delayed project that seemed to grow in size with each week it was delayed by and worried about money a lot.I became depressed and anxious and had trouble eating sleeping and generally being myself. As my depression worsened I was regularly late for work couldn't perform as well as I should and became irritable with my colleagues.My employers response after a while was to send me private messages complaining about my lateness which only worsened the situation. I was prescribed 3 weeks off work by my doctor which my employer agreed to only to come back after to find I had been on 'statutory pay' which was roughly half of what I was expecting and was not enough to cover my rent bills AND food. This made me worse and sent me into another depression until I eventually admitted defeat gave up working and left the company. It took me months to recover and I'm now left (over 6 months after this all started) recovering from the fallout I created leaving employment with hardly any money to my name.I had previously been told by my employer that I was too young to burn out and (stupidly) trusted them. I did not feel comfortable discussing my problems with my employer because each time I was met with an attitude that I had to get myself together and ultimately given the amount of employees before me who had left the company by being fired after an altercation with the employer left me with no option but to hide it from them so I too wouldn't be fired."
 "I'm self-employed on contract with small start-up. Covered through spouse's insurance."
 "My mental health issues were the direct result of the trauma from childhood abuse. Most (all?) of the Prompt-sponsored/related presentations I've seen have been about congenital mental health issues that are treatable with continued medication. For me medication only provided temporary assistance. I needed years of (continuing) therapy to deal with PTSD and related disorders (depression anxiety suicidal tendencies others). I haven't seen many in our community discussing trauma-related mental health issues but they are just as real and just as debilitating."
 'it is my opinion that bad mental health is a red flag for employers and i would never bring it up.'
 "I openly discuss my mental health struggles. I have found that doing so encourages people who also struggle to seek treatment. I'm willing to risk losing the support of people who don't understand if it helps those who understand all too well."
 "Just starting a new job hence the numerous I don't know selections."
 "The data will be skewed for self-employed people as the questions contain some bias.Having said that: being self-employed I *choose* to work for companies which want to employ *me* not just my skills but including my opinions my life-experience etc. If a potential contract/job doesn't *feel* right I prefer to not take it (and be poor) than to compromise myself."
 'Although my employer does everything they can to accommodate employees with mental health problems when those individuals cannot carry out any work assigned to them (even over the course of months) they appear to have no alternative but to terminate their employment. However I believe this would be the same for a physical health problem. '
 'I work at a large university with a track record of health and wellbeing support'
 "i'm in a country with social health care so my options are not dependant on my employer. this makes a few of the early questions less relevant than they would be for a resident of the US."
 "In australia all organisations of a certain size have to provide free access to a 'employee assistance program' to discuss work and personal issues.EAPs are an external provider totally confidential and anonymous (ring up andsay the name of who you work for - so they know to bill your work)  and they offer phone and face to face consults."
 'Bipolar disorder ']


[ ]
# Create a copy of the original dataset
# so that the original data remains unchanged.

df_clean = df.copy()

print("Original dataset shape:", df.shape)
print("Working dataset shape:", df_clean.shape)
Original dataset shape: (1259, 27)
Working dataset shape: (1259, 27)

[ ]
# Convert Timestamp into datetime format

df_clean['Timestamp'] = pd.to_datetime(
    df_clean['Timestamp'],
    errors='coerce'
)

print("Timestamp data type:", df_clean['Timestamp'].dtype)
Timestamp data type: datetime64[ns]

[ ]
# Check the minimum, maximum and unusual age values

print("Minimum Age:", df_clean['Age'].min())
print("Maximum Age:", df_clean['Age'].max())

print("\nAge values below 18:")
print(df_clean[df_clean['Age'] < 18]['Age'].value_counts())

print("\nAge values above 70:")
print(df_clean[df_clean['Age'] > 70]['Age'].value_counts())
Minimum Age: -1726
Maximum Age: 99999999999

Age values below 18:
Age
-29      1
-1726    1
 5       1
 8       1
 11      1
-1       1
Name: count, dtype: int64

Age values above 70:
Age
329            1
99999999999    1
72             1
Name: count, dtype: int64

[ ]
# Replace unrealistic age values with NaN

df_clean.loc[
    (df_clean['Age'] < 18) | (df_clean['Age'] > 70),
    'Age'
] = np.nan

print("Missing Age values after validation:",
      df_clean['Age'].isnull().sum())
Missing Age values after validation: 9

[ ]
# Impute invalid/missing ages using the median age

median_age = df_clean['Age'].median()

df_clean['Age'] = df_clean['Age'].fillna(median_age)

print("Median age used:", median_age)
Median age used: 31.0

[ ]
# Create age groups for easier demographic analysis

bins = [17, 24, 34, 44, 54, 70]

labels = [
    '18-24',
    '25-34',
    '35-44',
    '45-54',
    '55-70'
]

df_clean['Age_Group'] = pd.cut(
    df_clean['Age'],
    bins=bins,
    labels=labels
)

print(df_clean['Age_Group'].value_counts().sort_index())
Age_Group
18-24    156
25-34    716
35-44    320
45-54     51
55-70     16
Name: count, dtype: int64

[ ]
# ============================================================
# HANDLE MISSING VALUES
# ============================================================

# comments has approximately 87% missing values and is
# an optional free-text field, so it is removed.
df_clean = df_clean.drop(columns=['comments'])

# State is not applicable to many respondents outside the US.
# Therefore, missing values are retained as a separate category.
df_clean['state'] = df_clean['state'].fillna('Not Available')

# Missing work_interfere responses should not be assumed
# to mean "Never".
df_clean['work_interfere'] = df_clean['work_interfere'].fillna(
    'Not Available'
)

# Retain missing self-employment responses as Unknown.
df_clean['self_employed'] = df_clean['self_employed'].fillna(
    'Unknown'
)

print("Missing-value handling completed.")
Missing-value handling completed.

[ ]
# ============================================================
# STANDARDIZE GENDER
# ============================================================

def standardize_gender(value):

    if pd.isna(value):
        return 'Unknown'

    value = str(value).strip().lower()

    if value in ['male', 'm', 'man', 'cis male',
                 'male (cis)', 'mal', 'maile', 'msle', 'mail']:
        return 'Male'

    elif value in ['female', 'f', 'woman', 'cis female',
                   'female (cis)', 'female (trans)',
                   'femake', 'femail']:
        return 'Female'

    elif value in ['non-binary', 'enby', 'genderqueer',
                   'agender', 'androgyne', 'neuter']:
        return 'Non-binary/Other'

    else:
        return 'Other'


df_clean['Gender_Clean'] = df_clean['Gender'].apply(
    standardize_gender
)

print(df_clean['Gender_Clean'].value_counts())
Gender_Clean
Male                984
Female              248
Other                21
Non-binary/Other      6
Name: count, dtype: int64

[ ]
# Final missing-value check

missing_after = df_clean.isnull().sum()

print("Missing values remaining:")
print(missing_after[missing_after > 0])
Missing values remaining:
Series([], dtype: int64)

[ ]
# Check the cleaned dataset

print("Original dataset shape:", df.shape)
print("Cleaned dataset shape:", df_clean.shape)

display(df_clean.head())


[ ]
# ============================================================
# CHART 1: AGE DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df_clean,
    x='Age',
    bins=20,
    kde=True
)

plt.title('Distribution of Respondent Age')
plt.xlabel('Age')
plt.ylabel('Number of Respondents')

plt.tight_layout()
plt.show()

A histogram is used to see how the respondents' ages are distributed.

This helps organizations understand which employee age groups are mainly represented and plan suitable mental-health support accordingly.


[ ]
# ============================================================
# CHART 2: GENDER DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df_clean,
    x='Gender_Clean',
    order=df_clean['Gender_Clean'].value_counts().index
)

plt.title('Gender Distribution of Respondents')
plt.xlabel('Gender')
plt.ylabel('Number of Respondents')

plt.tight_layout()
plt.show()

A count plot helps us see how the respondents are divided across gender groups.

This helps understand the demographic mix of the survey and supports more inclusive workplace planning.


[ ]
# ============================================================
# CHART 3: MENTAL HEALTH TREATMENT DISTRIBUTION
# ============================================================

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df_clean,
    x='treatment',
    order=df_clean['treatment'].value_counts().index
)

plt.title('Mental Health Treatment Distribution')
plt.xlabel('Sought Treatment')
plt.ylabel('Number of Respondents')

plt.tight_layout()
plt.show()

A count plot shows how many respondents have and have not sought mental-health treatment.

This helps organizations understand the level of mental-health treatment usage among respondents.


[ ]
# ============================================================
# CHART 4: FAMILY HISTORY OF MENTAL ILLNESS
# ============================================================

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df_clean,
    x='family_history',
    order=df_clean['family_history'].value_counts().index
)

plt.title('Family History of Mental Illness')
plt.xlabel('Family History')
plt.ylabel('Number of Respondents')

plt.tight_layout()
plt.show()

A count plot shows how respondents are divided based on family history of mental illness.

This information helps organizations understand the background factors that may be relevant to workplace mental-health support.


[ ]
# ============================================================
# CHART 5: COMPANY SIZE DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 5))

order = df_clean['no_employees'].value_counts().index

sns.countplot(
    data=df_clean,
    x='no_employees',
    order=order
)

plt.title('Distribution of Respondents by Company Size')
plt.xlabel('Number of Employees')
plt.ylabel('Number of Respondents')
plt.xticks(rotation=30)

plt.tight_layout()
plt.show()

A count plot helps compare the number of respondents across different company sizes.

This helps organizations understand which company-size groups are represented most in the survey.


[ ]
# ============================================================
# CHART 6: REMOTE WORK DISTRIBUTION
# ============================================================

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df_clean,
    x='remote_work',
    order=df_clean['remote_work'].value_counts().index
)

plt.title('Remote Work Distribution')
plt.xlabel('Remote Work')
plt.ylabel('Number of Respondents')

plt.tight_layout()
plt.show()

A count plot shows how many respondents work remotely and how many work mainly from an office.

This helps organizations understand the working arrangement represented in the survey.


[ ]
# ============================================================
# CHART 7: MENTAL HEALTH TREATMENT BY GENDER
# ============================================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df_clean,
    x='Gender_Clean',
    hue='treatment'
)

plt.title('Mental Health Treatment by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Respondents')
plt.legend(title='Treatment')

plt.tight_layout()
plt.show()

This chart compares treatment responses across gender groups.

This comparison can help organizations consider whether mental-health support is reaching different employee groups.


[ ]
# ============================================================
# CHART 8: TREATMENT VS FAMILY HISTORY
# ============================================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df_clean,
    x='family_history',
    hue='treatment'
)

plt.title('Mental Health Treatment by Family History')
plt.xlabel('Family History of Mental Illness')
plt.ylabel('Number of Respondents')
plt.legend(title='Treatment')

plt.tight_layout()
plt.show()

This chart compares treatment responses based on family history.

This can help organizations understand the importance of accessible mental-health support for employees with different backgrounds.


[ ]
# ============================================================
# CHART 9: TREATMENT BY AGE GROUP
# ============================================================

plt.figure(figsize=(9, 5))

sns.countplot(
    data=df_clean,
    x='Age_Group',
    hue='treatment'
)

plt.title('Mental Health Treatment by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Respondents')
plt.legend(title='Treatment')

plt.tight_layout()
plt.show()

This chart compares treatment responses across different age groups.

This may help organizations plan mental-health awareness and support programs for different age groups.


[ ]
# ============================================================
# CHART 10: TREATMENT BY REMOTE WORK
# ============================================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df_clean,
    x='remote_work',
    hue='treatment'
)

plt.title('Mental Health Treatment by Remote Work')
plt.xlabel('Remote Work')
plt.ylabel('Number of Respondents')
plt.legend(title='Treatment')

plt.tight_layout()
plt.show()

This chart compares treatment responses between remote and non-remote workers.

This can help organizations understand whether working arrangements are associated with different treatment patterns.


[ ]
# ============================================================
# CHART 11: TREATMENT BY COMPANY SIZE
# ============================================================

plt.figure(figsize=(10, 6))

sns.countplot(
    data=df_clean,
    x='no_employees',
    hue='treatment',
    order=df_clean['no_employees'].value_counts().index
)

plt.title('Mental Health Treatment by Company Size')
plt.xlabel('Company Size')
plt.ylabel('Number of Respondents')
plt.xticks(rotation=30)
plt.legend(title='Treatment')

plt.tight_layout()
plt.show()

This chart compares treatment responses across different company sizes.

This can help organizations understand whether workplace size is associated with different mental-health treatment patterns.


[ ]
# ============================================================
# CHART 12: TREATMENT BY TECH COMPANY
# ============================================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df_clean,
    x='tech_company',
    hue='treatment'
)

plt.title('Mental Health Treatment by Tech Company')
plt.xlabel('Employer is Primarily a Tech Company')
plt.ylabel('Number of Respondents')
plt.legend(title='Treatment')

plt.tight_layout()
plt.show()

This chart compares treatment responses between tech and non-tech companies.

This comparison helps organizations understand mental-health treatment patterns across different workplace types.


[ ]
# ============================================================
# CHART 13: TREATMENT BY MENTAL HEALTH BENEFITS
# ============================================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df_clean,
    x='benefits',
    hue='treatment'
)

plt.title('Mental Health Treatment by Workplace Benefits')
plt.xlabel('Mental Health Benefits')
plt.ylabel('Number of Respondents')
plt.legend(title='Treatment')

plt.tight_layout()
plt.show()

This chart compares treatment responses based on the mental-health benefits provided by employers.

This can help employers understand the importance of making mental-health support available to employees.


[ ]
# ============================================================
# CHART 14: TREATMENT BY AWARENESS OF CARE OPTIONS
# ============================================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df_clean,
    x='care_options',
    hue='treatment'
)

plt.title('Mental Health Treatment by Awareness of Care Options')
plt.xlabel('Awareness of Care Options')
plt.ylabel('Number of Respondents')
plt.legend(title='Treatment')

plt.tight_layout()
plt.show()

This chart compares treatment responses based on awareness of available care options.

Better awareness of available care options may help employees make informed decisions about seeking support.


[ ]
# ============================================================
# CHART 15: TREATMENT BY WELLNESS PROGRAM
# ============================================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df_clean,
    x='wellness_program',
    hue='treatment'
)

plt.title('Mental Health Treatment by Wellness Program')
plt.xlabel('Mental Health Discussed in Wellness Program')
plt.ylabel('Number of Respondents')
plt.legend(title='Treatment')

plt.tight_layout()
plt.show()

This chart compares treatment responses based on whether mental health was discussed in a workplace wellness program.

This helps organizations understand whether workplace wellness initiatives are reaching employees who may need support.


[ ]
# ============================================================
# CHART 16: TREATMENT BY WORK INTERFERENCE
# ============================================================

plt.figure(figsize=(9, 5))

order = ['Never', 'Rarely', 'Sometimes', 'Often', 'Not Available']

sns.countplot(
    data=df_clean,
    x='work_interfere',
    hue='treatment',
    order=[x for x in order if x in df_clean['work_interfere'].unique()]
)

plt.title('Mental Health Treatment by Work Interference')
plt.xlabel('Work Interference')
plt.ylabel('Number of Respondents')
plt.legend(title='Treatment')

plt.tight_layout()
plt.show()

This chart compares treatment responses with the level of work interference.

This can help employers identify the need for accessible support when mental health affects work.


[ ]
# ============================================================
# CHART 17: TREATMENT BY MENTAL HEALTH CONSEQUENCE
# ============================================================

plt.figure(figsize=(9, 5))

sns.countplot(
    data=df_clean,
    x='mental_health_consequence',
    hue='treatment'
)

plt.title('Mental Health Treatment by Perceived Workplace Consequences')
plt.xlabel('Mental Health Consequence')
plt.ylabel('Number of Respondents')
plt.legend(title='Treatment')

plt.tight_layout()
plt.show()

This chart compares treatment responses with perceived workplace consequences of discussing mental health.

This can help employers understand whether concerns about workplace consequences are linked with different treatment patterns.


[ ]
# ============================================================
# CHART 18: TREATMENT BY SUPERVISOR DISCUSSION
# ============================================================

plt.figure(figsize=(9, 5))

sns.countplot(
    data=df_clean,
    x='supervisor',
    hue='treatment'
)

plt.title('Mental Health Treatment by Willingness to Discuss with Supervisor')
plt.xlabel('Discuss Mental Health with Supervisor')
plt.ylabel('Number of Respondents')
plt.legend(title='Treatment')

plt.tight_layout()
plt.show()

This chart compares treatment responses with employees' willingness to discuss mental health with supervisors.

This may help organizations understand the importance of creating a comfortable environment for mental-health discussions.


[ ]
# ============================================================
# CHART 19: MENTAL HEALTH VS PHYSICAL HEALTH
# ============================================================

plt.figure(figsize=(9, 5))

sns.countplot(
    data=df_clean,
    x='mental_vs_physical',
    hue='treatment'
)

plt.title('Mental Health vs Physical Health by Treatment')
plt.xlabel('Employer Takes Mental Health as Seriously as Physical Health')
plt.ylabel('Number of Respondents')
plt.legend(title='Treatment')

plt.tight_layout()
plt.show()

This chart compares treatment responses with employees' views on how mental health is treated compared with physical health.

This can help organizations understand employees' perceptions of mental-health support in the workplace.


[ ]
# ============================================================
# CHART 20: GENDER + FAMILY HISTORY + TREATMENT
# ============================================================

g = sns.catplot(
    data=df_clean,
    x='Gender_Clean',
    hue='treatment',
    col='family_history',
    kind='count',
    height=5,
    aspect=1.1
)

g.set_axis_labels(
    'Gender',
    'Number of Respondents'
)

g.set_titles(
    'Family History: {col_name}'
)

g.fig.suptitle(
    'Mental Health Treatment by Gender and Family History',
    y=1.05
)

plt.show()


[ ]
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

sns.set_style("whitegrid")

[ ]
from google.colab import files

uploaded = files.upload()

df = pd.read_csv('survey.csv')

print("Dataset loaded successfully.")
print("Shape of the dataset:", df.shape)


[ ]
# Create a copy
df_clean = df.copy()

# Convert Timestamp
df_clean['Timestamp'] = pd.to_datetime(
    df_clean['Timestamp'],
    errors='coerce'
)

# Clean Age
df_clean.loc[
    (df_clean['Age'] < 18) | (df_clean['Age'] > 70),
    'Age'
] = np.nan

# Fill invalid ages with median
median_age = df_clean['Age'].median()
df_clean['Age'] = df_clean['Age'].fillna(median_age)

# Create Age Groups
bins = [17, 24, 34, 44, 54, 70]
labels = ['18-24', '25-34', '35-44', '45-54', '55-70']

df_clean['Age_Group'] = pd.cut(
    df_clean['Age'],
    bins=bins,
    labels=labels
)

# Handle missing values
df_clean = df_clean.drop(columns=['comments'])

df_clean['state'] = df_clean['state'].fillna('Not Available')
df_clean['work_interfere'] = df_clean['work_interfere'].fillna('Not Available')
df_clean['self_employed'] = df_clean['self_employed'].fillna('Unknown')

# Standardize Gender
def standardize_gender(value):
    if pd.isna(value):
        return 'Unknown'

    value = str(value).strip().lower()

    male_values = [
        'male', 'm', 'man', 'cis male',
        'male (cis)', 'mal', 'maile',
        'msle', 'mail'
    ]

    female_values = [
        'female', 'f', 'woman', 'cis female',
        'female (cis)', 'female (trans)',
        'femake', 'femail'
    ]

    non_binary_values = [
        'non-binary', 'enby', 'genderqueer',
        'agender', 'androgyne', 'neuter'
    ]

    if value in male_values:
        return 'Male'
    elif value in female_values:
        return 'Female'
    elif value in non_binary_values:
        return 'Non-binary/Other'
    else:
        return 'Other'

df_clean['Gender_Clean'] = df_clean['Gender'].apply(
    standardize_gender
)

print("Cleaning completed successfully.")
print("Shape:", df_clean.shape)
print("Missing values:", df_clean.isnull().sum().sum())
Cleaning completed successfully.
Shape: (1259, 28)
Missing values: 0

[ ]
# ============================================================
# CHART 21: AGE GROUP + REMOTE WORK + TREATMENT
# ============================================================

g = sns.catplot(
    data=df_clean,
    x='Age_Group',
    hue='treatment',
    col='remote_work',
    kind='count',
    height=5,
    aspect=1.1
)

g.set_axis_labels(
    'Age Group',
    'Number of Respondents'
)

g.set_titles(
    'Remote Work: {col_name}'
)

g.fig.suptitle(
    'Mental Health Treatment by Age Group and Remote Work',
    y=1.05
)

plt.show()

This chart compares treatment patterns across age groups and remote-work arrangements.

This can help organizations understand different mental-health support needs across employee groups.


[ ]
# ============================================================
# CHART 22: COMPANY SIZE + BENEFITS + TREATMENT
# ============================================================

g = sns.catplot(
    data=df_clean,
    x='no_employees',
    hue='treatment',
    col='benefits',
    kind='count',
    height=5,
    aspect=1.1
)

g.set_axis_labels(
    'Company Size',
    'Number of Respondents'
)

g.set_titles(
    'Mental Health Benefits: {col_name}'
)

g.fig.suptitle(
    'Mental Health Treatment by Company Size and Benefits',
    y=1.05
)

plt.xticks(rotation=30)
plt.show()

This chart compares treatment patterns across company sizes and mental-health benefit categories.

This can help organizations understand how workplace benefits and company size relate to reported treatment patterns.


[ ]
# ============================================================
# CHART 23: WORK INTERFERENCE + FAMILY HISTORY + TREATMENT
# ============================================================

g = sns.catplot(
    data=df_clean,
    x='work_interfere',
    hue='treatment',
    col='family_history',
    kind='count',
    height=5,
    aspect=1.1
)

g.set_axis_labels(
    'Work Interference',
    'Number of Respondents'
)

g.set_titles(
    'Family History: {col_name}'
)

g.fig.suptitle(
    'Mental Health Treatment by Work Interference and Family History',
    y=1.05
)

plt.show()

This chart compares treatment patterns across work interference levels and family history.

This can help organizations identify employee groups that may require accessible mental-health support.


[ ]
# ============================================================
# CHART 24: CATEGORICAL ASSOCIATION HEATMAP
# ============================================================

from scipy.stats import chi2_contingency

def cramers_v(x, y):
    table = pd.crosstab(x, y)

    chi2 = chi2_contingency(table)[0]
    n = table.sum().sum()
    r, k = table.shape

    phi2 = chi2 / n
    phi2corr = max(
        0,
        phi2 - ((k - 1) * (r - 1)) / (n - 1)
    )

    rcorr = r - ((r - 1) ** 2) / (n - 1)
    kcorr = k - ((k - 1) ** 2) / (n - 1)

    return np.sqrt(
        phi2corr / min(kcorr - 1, rcorr - 1)
    )

# Select important categorical variables
columns = [
    'Gender_Clean',
    'family_history',
    'treatment',
    'work_interfere',
    'remote_work',
    'tech_company',
    'benefits',
    'care_options',
    'wellness_program',
    'mental_health_consequence',
    'supervisor'
]

association_matrix = pd.DataFrame(
    index=columns,
    columns=columns,
    dtype=float
)

for col1 in columns:
    for col2 in columns:
        association_matrix.loc[col1, col2] = cramers_v(
            df_clean[col1],
            df_clean[col2]
        )

plt.figure(figsize=(12, 9))

sns.heatmap(
    association_matrix,
    annot=True,
    fmt='.2f',
    cmap='Blues',
    vmin=0,
    vmax=1
)

plt.title('Categorical Association Heatmap')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

This heatmap shows the strength of association between important categorical variables.

This helps organizations identify relationships between workplace factors and mental-health responses for further analysis.


[ ]
# ============================================================
# CHART 25: PAIR PLOT
# ============================================================

pair_df = df_clean[
    ['Age', 'treatment', 'family_history', 'remote_work', 'tech_company']
].copy()

# Convert Yes/No variables to numeric values
binary_columns = [
    'treatment',
    'family_history',
    'remote_work',
    'tech_company'
]

for col in binary_columns:
    pair_df[col] = pair_df[col].map({
        'Yes': 1,
        'No': 0
    })

# Remove rows with missing values
pair_df = pair_df.dropna()

sns.pairplot(
    pair_df,
    hue='treatment',
    diag_kind='hist'
)

plt.suptitle(
    'Pair Plot of Age and Selected Workplace Factors',
    y=1.02
)

plt.show()

This pair plot helps examine relationships between age and selected workplace factors.

This provides an overall view of relationships that can be explored further when studying workplace mental-health patterns.

Solution to Business Objective

The analysis of the Mental Health in Tech Survey provides useful insights into factors related to mental-health treatment and workplace experiences. The analysis shows that treatment responses vary across different age groups, gender groups, family-history categories, company sizes and working arrangements. Workplace factors such as mental-health benefits, awareness of care options, wellness programs and willingness to discuss mental health with supervisors also show differences in treatment patterns.

The analysis of work interference and family history provides additional insight into the relationship between personal background, workplace experience and reported treatment. The categorical association analysis helps identify variables that have stronger relationships with each other and can be considered for further investigation.

Based on these findings, organizations can focus on improving awareness of mental-health resources, providing accessible support programs and creating a workplace environment where employees feel comfortable discussing mental-health concerns. The analysis can also help organizations understand that mental-health support may need to consider different employee and workplace characteristics rather than using a single approach for everyone.

Conclusion

The exploratory data analysis of the Mental Health in Tech Survey provided useful insights into mental-health treatment patterns and workplace experiences among respondents. The analysis examined demographic factors such as age and gender, along with workplace factors including company size, remote work, mental-health benefits, care options, wellness programs and supervisor support.

The visualizations showed differences in treatment responses across various employee and workplace groups. The analysis also highlighted the relationship between family history, work interference and mental-health treatment. The categorical association heatmap provided an overall view of relationships among the selected variables.

Overall, the analysis demonstrates that mental-health experiences in the workplace are influenced by a combination of personal and workplace-related factors. These findings can help organizations understand employee needs and consider more accessible mental-health resources, awareness programs and supportive workplace practices.

The analysis is based on patterns and associations observed in the survey data and does not establish cause-and-effect relationships.


[1]
0s
%%writefile app.py

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
Writing app.py

[3]
18s
from google.colab import files

uploaded = files.upload()


[4]
0s
import os
print(os.listdir())
['.config', 'app.py', 'survey.csv', 'sample_data']

[5]
1s
import pandas as pd

df_test = pd.read_csv("survey.csv")

print("Rows:", df_test.shape[0])
print("Columns:", df_test.shape[1])
Rows: 1259
Columns: 27

[6]
9s
!pip install -q streamlit
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.1/10.1 MB 39.6 MB/s eta 0:00:00
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.4/11.4 MB 64.0 MB/s eta 0:00:00

[7]
4s
!npm install -g localtunnel
⠙⠹⠸⠼⠴⠦⠧⠇⠏⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏⠋⠙⠹⠸⠼
added 22 packages in 4s
⠼
⠼3 packages are looking for funding
⠼  run `npm fund` for details
⠼

[8]
0s
!streamlit run app.py --server.port 8501 &>/content/logs.txt &

[9]
0s
!cat /content/logs.txt

Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.

2026-09-19 08:00:44.668 Uvicorn server started on :::8501

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://172.28.0.12:8501
  External URL: http://34.106.195.46:8501


[11]
0s
!lt --port 8501
^C

[12]
0s

Writing requirements.txt

[13]
0s



[14]
0s

True
['.config', 'logs.txt', 'requirements.txt', 'app.py', 'survey.csv', 'sample_data']

[15]
0s


