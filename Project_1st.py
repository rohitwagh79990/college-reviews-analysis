# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:45:13 202

@author: JS COMPUTERS
"""

###############################################################################
#------------------------------------------------------------------------------


#############################################################################

import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Explanation:
# We imported the required libraries.
# Regex is used for text extraction, Pandas for data analysis,
# and Matplotlib and Seaborn for data visualization.


# ============================================================
# 1. KESHAV MAHAVIDYALAYA
# ============================================================

review1 = """
College: Keshav Mahavidyalaya
Course: B.Sc Computer Science Hons
Infrastructure: Good
Placements: Average
Academics: Good
Value for Money: Good
Campus Life: Good
Faculty: Teachers are very good and supportive
Lab Resources: Computer labs are average and some systems are outdated
Skill Development: Placement cell helps students in building their resume and skills
"""

# Explanation:
# We stored the raw review data of Keshav Mahavidyalaya
# in a string variable.


with open("keshav.txt", "w") as file:
    file.write(review1)

# Explanation:
# We created a text file and stored the Keshav Mahavidyalaya
# review data using write mode.


# ============================================================
# 2. MGM UNIVERSITY
# ============================================================

review2 = """
College: MGM University
Course: B.Tech Computer Science and Engineering
Infrastructure: Good
Placements: Good
Academics: Good
Value for Money: Average
Campus Life: Good
Faculty: Faculty members are knowledgeable and supportive
Lab Resources: Computer labs have good resources and equipment
Skill Development: Students get opportunities for projects, internships and technical activities
"""

# Explanation:
# We stored the raw review data of MGM University
# in a string variable.


with open("mgm.txt", "w") as file:
    file.write(review2)

# Explanation:
# We created a separate text file and stored the MGM
# University review data in it.


# ============================================================
# 3. COEP TECHNOLOGICAL UNIVERSITY
# ============================================================

review3 = """
College: COEP Technological University
Course: B.Tech Electronics and Telecommunication Engineering
Infrastructure: Good
Placements: Excellent
Academics: Excellent
Value for Money: Good
Campus Life: Good
Faculty: Faculty members are experienced and supportive
Lab Resources: Laboratories have good equipment and technical resources
Skill Development: Students get good opportunities for projects, competitions and internships
"""

# Explanation:
# We stored the raw review data of COEP Technological University
# in a string variable.


with open("coep.txt", "w") as file:
    file.write(review3)

# Explanation:
# We created a separate text file and stored the COEP
# review data in it.


# ============================================================
# 4. MIT WORLD PEACE UNIVERSITY
# ============================================================

review4 = """
College: MIT World Peace University
Course: B.Tech Computer Science and Engineering
Infrastructure: Excellent
Placements: Good
Academics: Good
Value for Money: Average
Campus Life: Excellent
Faculty: Faculty members are supportive and knowledgeable
Lab Resources: Labs have modern computers and good technical facilities
Skill Development: Students get opportunities for internships, projects and industry interaction
"""

# Explanation:
# We stored the raw review data of MIT World Peace University
# in a string variable.


with open("mit_wpu.txt", "w") as file:
    file.write(review4)

# Explanation:
# We created a separate text file and stored the MIT WPU
# review data in it.


# ============================================================
# 5. CSMS COLLEGE
# ============================================================

review5 = """
College: CSMS College
Course: B.Sc Computer Science
Infrastructure: Average
Placements: Average
Academics: Good
Value for Money: Good
Campus Life: Average
Faculty: Teachers are helpful and supportive
Lab Resources: Computer labs have basic facilities and some systems need improvement
Skill Development: Students get basic opportunities for projects and technical skill development
"""

# Explanation:
# We stored the raw review data of CSMS College
# in a string variable.


with open("csms.txt", "w") as file:
    file.write(review5)

# Explanation:
# We created a separate text file and stored the CSMS
# College review data in it.


# ============================================================
# READ ALL FILES
# ============================================================

with open("keshav.txt", "r") as file:
    keshav = file.read()

with open("mgm.txt", "r") as file:
    mgm = file.read()

with open("coep.txt", "r") as file:
    coep = file.read()

with open("mit_wpu.txt", "r") as file:
    mit_wpu = file.read()

with open("csms.txt", "r") as file:
    csms = file.read()

# Explanation:
# We opened all five text files in read mode and loaded
# their contents into Python variables.


# ============================================================
# STORE ALL REVIEWS
# ============================================================

reviews = [keshav, mgm, coep, mit_wpu, csms]

# Explanation:
# We combined all five college reviews into one list
# so that we can process them together.


# ============================================================
# REGEX EXTRACTION
# ============================================================

colleges = []
courses = []
infrastructure = []
placements = []
academics = []
value_for_money = []
campus_life = []
faculty = []
lab_resources = []
skill_development = []

# Explanation:
# We created empty lists to store the information
# extracted from each college review.


for review in reviews:

    colleges.append(
        re.findall(r'College:\s*(.*)', review)[0]
    )

    courses.append(
        re.findall(r'Course:\s*(.*)', review)[0]
    )

    infrastructure.append(
        re.findall(r'Infrastructure:\s*(.*)', review)[0]
    )

    placements.append(
        re.findall(r'Placements:\s*(.*)', review)[0]
    )

    academics.append(
        re.findall(r'Academics:\s*(.*)', review)[0]
    )

    value_for_money.append(
        re.findall(r'Value for Money:\s*(.*)', review)[0]
    )

    campus_life.append(
        re.findall(r'Campus Life:\s*(.*)', review)[0]
    )

    faculty.append(
        re.findall(r'Faculty:\s*(.*)', review)[0]
    )

    lab_resources.append(
        re.findall(r'Lab Resources:\s*(.*)', review)[0]
    )

    skill_development.append(
        re.findall(r'Skill Development:\s*(.*)', review)[0]
    )

# Explanation:
# We used a for loop and Regular Expressions to extract
# useful information such as college name, course,
# infrastructure, placements and other parameters.


# ============================================================
# CREATE DATAFRAME
# ============================================================

df = pd.DataFrame({
    "College": colleges,
    "Course": courses,
    "Infrastructure": infrastructure,
    "Placements": placements,
    "Academics": academics,
    "Value_for_Money": value_for_money,
    "Campus_Life": campus_life,
    "Faculty": faculty,
    "Lab_Resources": lab_resources,
    "Skill_Development": skill_development
})

# Explanation:
# We created a Pandas DataFrame to organize the extracted
# information into rows and columns.


print(df)

# Explanation:
# We displayed the DataFrame to check our extracted data.


# ============================================================
# BASIC DATA CHECK
# ============================================================

print(df.head())

# Explanation:
# head() displays the first five rows of the DataFrame.


print(df.shape)

# Explanation:
# shape tells us the number of rows and columns.


print(df.dtypes)

# Explanation:
# dtypes shows the data type of each column.


print(df.describe())

# Explanation:
# describe() gives a statistical summary of numerical data.


# ============================================================
# SAVE DATAFRAME AS CSV
# ============================================================

df.to_csv("college_reviews.csv", index=False)

# Explanation:
# We saved the processed DataFrame into a CSV file.


print("CSV file created successfully")


# ============================================================
# CONVERT RATINGS INTO NUMBERS
# ============================================================

rating_map = {
    "Average": 2,
    "Good": 3,
    "Excellent": 5
}

# Explanation:
# We created a rating map to convert text-based ratings
# into numerical values for calculations.


df["Infrastructure_Rating"] = df["Infrastructure"].map(rating_map)
df["Placement_Rating"] = df["Placements"].map(rating_map)
df["Academics_Rating"] = df["Academics"].map(rating_map)
df["Value_Rating"] = df["Value_for_Money"].map(rating_map)
df["Campus_Rating"] = df["Campus_Life"].map(rating_map)

# Explanation:
# We used map() to convert the text ratings into numerical
# ratings for each parameter.


# ============================================================
# OVERALL RATING
# ============================================================

df["Overall_Rating"] = (
    df["Infrastructure_Rating"]
    + df["Placement_Rating"]
    + df["Academics_Rating"]
    + df["Value_Rating"]
    + df["Campus_Rating"]
) / 5

# Explanation:
# We calculated the overall rating by taking the average
# of five parameters.


print(df[["College", "Overall_Rating"]])

# Explanation:
# We displayed each college along with its overall rating.


# ============================================================
# OVERALL COLLEGE COMPARISON
# ============================================================

plt.figure(figsize=(12, 6))

sns.barplot(
    data=df,
    x="College",
    y="Overall_Rating"
)

plt.title("Overall College Comparison")
plt.xlabel("College")
plt.ylabel("Overall Rating")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# Explanation:
# We created a bar chart to compare the overall ratings
# of all five colleges.
# figsize makes the chart larger, rotation makes long
# college names easier to read, and tight_layout prevents
# labels from getting cut off.

# INFERENCE:
# Based on our ratings, COEP has the highest overall rating,
# while CSMS has the lowest overall rating among the five colleges.


# ============================================================
# INFRASTRUCTURE COMPARISON
# ============================================================

plt.figure(figsize=(12, 6))

sns.barplot(
    data=df,
    x="College",
    y="Infrastructure_Rating"
)

plt.title("College Infrastructure Comparison")
plt.xlabel("College")
plt.ylabel("Infrastructure Rating")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# Explanation:
# This bar chart compares the infrastructure ratings
# of the five colleges.

# INFERENCE:
# MIT WPU has the highest infrastructure rating.
# Keshav, MGM and COEP have good infrastructure ratings,
# while CSMS has the lowest infrastructure rating.


# ============================================================
# PLACEMENT COMPARISON
# ============================================================

plt.figure(figsize=(12, 6))

sns.barplot(
    data=df,
    x="College",
    y="Placement_Rating"
)

plt.title("College Placement Comparison")
plt.xlabel("College")
plt.ylabel("Placement Rating")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# Explanation:
# This chart compares the placement ratings of all
# five colleges.

# INFERENCE:
# COEP has the highest placement rating because it is
# rated Excellent. MGM and MIT WPU have Good placement
# ratings, while Keshav and CSMS have Average ratings.


# ============================================================
# ACADEMICS COMPARISON
# ============================================================

plt.figure(figsize=(12, 6))

sns.barplot(
    data=df,
    x="College",
    y="Academics_Rating"
)

plt.title("College Academics Comparison")
plt.xlabel("College")
plt.ylabel("Academics Rating")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# Explanation:
# This chart compares the academic ratings of all five colleges.

# INFERENCE:
# COEP has the highest academic rating because it is rated
# Excellent. The other four colleges have Good academic ratings.