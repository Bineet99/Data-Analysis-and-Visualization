import pandas as pd
import matplotlib.pyplot as plt

#Created a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [85, 78, 92, 88, 76],
    'Physics': [90, 82, 88, 94, 79],
    'Chemistry': [88, 85, 91, 89, 80]
}
df = pd.DataFrame(data)

#Calculate average marks per student
df['Average'] = df[['Math', 'Physics', 'Chemistry']].mean(axis=1)
print("Student Marks:\n", df)

#Find highest average
top_student = df.loc[df['Average'].idxmax()]
print(top_student[['Name', 'Average']].to_dict())

#Plot Graph
plt.bar(df['Name'], df['Average'], color='blue')
plt.xlabel('<---Students--->')
plt.ylabel('<---Average Marks--->')
plt.title('Average Marks Per Student')
plt.show()
