# Amazon-Review-Analyzer

This project is a command-line tool for analyzing the sentiment of Amazon product reviews using either the VADER or RoBERTa model. It allows you to analyze a dataset of reviews, filter reviews based on sentiment, and export the results.

-------------------------
**Table of Contents**
-------------------------
1. How to Use the Project
2. Downloading the Dataset
3. Dataset Format Requirements
4. Features
5. Dependencies
6. Running the Project
7. Troubleshooting

-------------------------
**1. How to Use the Project**
-------------------------
The tool provides a simple command-line interface (CLI) with the following options:

1. **Analyze Dataset**:
   - Provide the path to a CSV file containing Amazon reviews.
   - Choose the sentiment analysis model (VADER or RoBERTa).
   - The tool will analyze the reviews and store the results.

2. **Analyze a Specific Review**:
   - Enter a review text manually.
   - Choose the sentiment analysis model (VADER or RoBERTa).
   - The tool will analyze the review and display the sentiment scores.

3. **Filter Reviews on Dataset**:
   - After analyzing a dataset, you can filter reviews by sentiment (Positive, Negative, Neutral).
   - The tool will display the top 10 reviews for the selected sentiment.

4. **Export Results**:
   - Export the analyzed results to a CSV file named `exportedResults.csv`.

5. **Exit**:
   - Exit the program.

-------------------------
**2. Downloading the Dataset**
-------------------------
To analyze a dataset, you need to download the Amazon Fine Food Reviews dataset from Kaggle:

1. Visit the dataset page: [Amazon Fine Food Reviews on Kaggle](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews/data).
2. Download the dataset (you may need to create a Kaggle account if you don’t have one).
3. Extract the downloaded file and locate the `Reviews.csv` file.
4. Place the `Reviews.csv` file in the project directory.

Alternatively, you can use the following command to download the dataset using the Kaggle API (if installed):
kaggle datasets download -d snap/amazon-fine-food-reviews
unzip amazon-fine-food-reviews.zip

-------------------------
**3. Dataset Format Requirements**
-------------------------
To analyze a dataset, the CSV file must have the following columns in the exact order:

- **Id**: Unique identifier for each review.
- **ProductId**: Identifier for the product being reviewed.
- **UserId**: Identifier for the user who wrote the review.
- **ProfileName**: Name of the user profile.
- **HelpfulnessNumerator**: Number of users who found the review helpful.
- **HelpfulnessDenominator**: Total number of users who rated the review's helpfulness.
- **Score**: Rating given by the user (e.g., 1 to 5 stars).
- **Time**: Timestamp of the review.
- **Summary**: Brief summary of the review.
- **Text**: Full text of the review.

Example CSV format:
Id,ProductId,UserId,ProfileName,HelpfulnessNumerator,HelpfulnessDenominator,Score,Time,Summary,Text
1,B00012345,USER123,John,10,15,5,1372638000,Great product!,This product is amazing and works perfectly.
2,B00012345,USER456,Jane,5,10,1,1372639000,Terrible product!,This product stopped working after a week.

-------------------------
**4. Features**
-------------------------
- **Sentiment Analysis**:
  - Use the VADER model for rule-based sentiment analysis.
  - Use the RoBERTa model for deep learning-based sentiment analysis.
- **Filter Reviews**:
  - Filter reviews by sentiment (Positive, Negative, Neutral).
- **Export Results**:
  - Export analyzed results to a CSV file for further analysis.
- **Visualization**:
  - View a bar chart showing the distribution of sentiments in the dataset.

-------------------------
**5. Dependencies**
-------------------------
To run this project, you need the following Python libraries:
- pandas
- numpy
- matplotlib
- seaborn
- nltk
- transformers
- scipy
- tqdm

Install the dependencies using:
pip install pandas numpy matplotlib seaborn nltk transformers scipy tqdm

-------------------------
**6. Running the Project**
-------------------------
1. Clone the repository or download the project files.
2. Install the required dependencies (see above).
3. Run the `main.py` file: python main.py
4. Follow the on-screen instructions to analyze reviews.

-------------------------
**7. Troubleshooting**
-------------------------
- **Error: File not found**:
- Ensure the dataset path is correct and the file exists.
- **Error: Missing columns in dataset**:
- Ensure the dataset has the required columns in the correct order.
- **Error: Model not loading**:
- Ensure you have an active internet connection to download the RoBERTa model.

-------------------------
**Contact**
-------------------------
For questions or feedback, please contact Nimish Bagwale at nimishbagwale@gmail.com

