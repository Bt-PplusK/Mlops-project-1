import streamlit as st
import pickle
import re
import nltk

nltk.download('stopwords')

#loading models
model = pickle.load(open('model_with_lr.pkl', 'rb'))
tfidf = pickle.load(open('tfidf (1).pkl','rb'))

def cleanResume(txt):
  cleanTxt = re.sub('http\S+\s',' ',txt)
  cleanTxt = re.sub('@\S+',' ',cleanTxt)
  cleanTxt = re.sub('#\S+',' ',cleanTxt)
  cleanTxt = re.sub('RT|cc',' ',cleanTxt)
  cleanTxt = re.sub('[%s]'%re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_{|}~"""),' ',cleanTxt)
  cleanTxt = re.sub(r'[^\x00-\x7f]',' ',cleanTxt)
  cleanTxt = re.sub('\s+',' ',cleanTxt)

  return cleanTxt

my_resume = 'D:\Resume_screening\electrical-engineering-resume-template.pdf'


# Clean the input resume
cleaned_resume = cleanResume(my_resume)

# Transform the cleaned resume using the trained TfidfVectorizer
input_features = tfidf.transform([cleaned_resume])

# Make the prediction using the loaded classifier
prediction_id = model.predict(input_features)[0]
category_mapping = {
            15: "Java Developer",
            23: "Testing",
            8: "DevOps Engineer",
            20: "Python Developer",
            24: "Web Designing",
            12: "HR",
            13: "Hadoop",
            3: "Blockchain",
            10: "ETL Developer",
            18: "Operations Manager",
            6: "Data Science",
            22: "Sales",
            16: "Mechanical Engineer",
            1: "Arts",
            7: "Database",
            11: "Electrical Engineering",
            14: "Health and fitness",
            19: "PMO",
            4: "Business Analyst",
            9: "DotNet Developer",
            2: "Automation Testing",
            17: "Network Security Engineer",
            21: "SAP Developer",
            5: "Civil Engineer",
            0: "Advocate",
        }

category_name = category_mapping.get(prediction_id, "Unknown")


print("Predicted Category:", category_name)
print(prediction_id)