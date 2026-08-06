import pandas as pd

# Load dataset
df = pd.read_csv("dataset/interview_questions.csv")

# Random question
random_question = df.sample(1).iloc[0]

print("Question:")
print(random_question["question"])
print("Role:", random_question["role"])
print("Category:", random_question["category"])
print("Difficulty:", random_question["difficulty"])

# User answer
answer = input("\nYour Answer: ")

print("\nYour Answer:")
print(answer)

if len(answer.strip()) < 10:
    print("\n⚠️ Answer is too short. Please give a detailed answer.")
else:
    print("\nYour Answer:")
    print(answer)
    
    
    import pandas as pd

df = pd.read_csv("dataset/interview_questions.csv")

print(df.info())
print()
print(df.isnull().sum())