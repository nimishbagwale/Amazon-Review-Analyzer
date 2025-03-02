import analyzer
import time

def main():
    
    print('''==========================================
   Amazon Review Classifier - CLI Tool
==========================================
1. Analyze dataset
2. Analyze a Specific Review
3. Filter Reviews on dataset 
4. Export Results
5. Exit
          ''')

    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            dataset_path = input("Enter the path to the dataset: ")
            model = input("Enter the model to use (vader/roberta): ")
            result = analyzer.analyze_database(dataset_path,model)
            print("Dataset analyzed successfully ......")
        elif choice == '2':
            review = input("Enter a review: ")
            model = input("Enter the model to use (vader/roberta): ")
            result = analyzer.analyze_review(review,model)
            print("Review analyzed successfully ......")
            print(result)
        elif choice == '3':
            analyzer.filter_reviews_on_dataset(result)
        elif choice == '4':
            analyzer.export_results(result)
        elif choice == '5':
            print("Exiting...")
            time.sleep(1)
            exit(0)
        else:
            print("Invalid choice. Exiting...")
            time.sleep(1)
            exit(1)

if __name__ == '__main__':
    main()