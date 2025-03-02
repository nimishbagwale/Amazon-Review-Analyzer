import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk 
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm import tqdm
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax
import os
import warnings
from transformers import logging

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
warnings.filterwarnings("ignore")
logging.set_verbosity_error()

def export_results(result):
    try:
        result.to_csv("exportedResults.csv", index=False)
        print("Results exported successfully to exportedResults.csv.")
    except Exception as e:
        print(f"Error exporting results: {e}")
        
def filter_reviews_on_dataset(result):
    if result is None or result.empty:
        print("No results available. Please analyze a dataset first.")
        return
    
    print("Data Filtered ....")
    positive_reviews = result.loc[result.iloc[:, 3] >= 0.5, :]
    negative_reviews = result.loc[result.iloc[:, 1] >= 0.5, :]
    neutral_reviews = result.loc[result.iloc[:, 2] >= 0.5, :]
    
    values = ["Positive", "Negative", "Neutral"]
    count = [positive_reviews.shape[0],negative_reviews.shape[0],neutral_reviews.shape[0]]
    plt.bar(values,count,color="skyblue")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.title("Sentiment Distribution")
    plt.show()
            
    
    print("Which reviews would you like to see?\n1. Positive\n2. Negative\n3. Neutral\n4. None")
    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if(choice == "1"):
            print(positive_reviews.sort_values(by="roberta_pos", ascending=False).head(10))
        elif(choice == "2"):
            print(negative_reviews.sort_values(by="roberta_neg", ascending=False).head(10))
        elif(choice == "3" ):
            print(neutral_reviews.sort_values(by="roberta_neu", ascending=False).head(10))
        elif(choice == "4"):
            break
        else:
            print("Invalid choice")
            continue
        cont = input("Want to check more results ? (y/n)")
        if cont.lower() == "n":
            break
    
def polarity_scores_roberta(example):
    MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    tokens = tokenizer(example,return_tensors="pt")
    output = model(**tokens)
    score = output[0][0].detach().numpy()
    scores = softmax(score)
    scores_dict = {
        "roberta_neg": scores[0],
        "roberta_neu": scores[1],
        "roberta_pos": scores[2]
    }
    return scores_dict

def polarity_scores_vader(example):
    sia = SentimentIntensityAnalyzer()
    vader_result = sia.polarity_scores(example)
    vader_result_rename = {}
    for key, value in vader_result.items():
        vader_result_rename[f"vader_{key}"] = value
    return vader_result_rename
    
def apply_model(dataset,model):
    res = {}
    for i, row in tqdm(dataset.iterrows(), total=len(dataset)):
        try :
            text = row["Text"]
            myid = row["Id"]
            if(model.lower()=="vader"):
                result = polarity_scores_vader(text)
            else:
                result = polarity_scores_roberta(text)
            res[myid] = result
        except RuntimeError:
            print(f"\n---------------------------------------\nBroke for id {myid}\n---------------------------------------\n")
    return res

def analyze_review(review,model):
    if(model.lower()=="vader"):
        result = polarity_scores_vader(review)
    else:
        result = polarity_scores_roberta(review)
    return result

def analyze_database(dataset_path,model):
    dataset = pd.read_csv(dataset_path)

    res = apply_model(dataset,model)
        
    results_df = pd.DataFrame(res).T
    results_df = results_df.reset_index().rename(columns={"index": "Id"})
    results_df = results_df.merge(dataset, how="left")
    
    return results_df