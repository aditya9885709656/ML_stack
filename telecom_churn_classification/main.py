from data_prep import pre_processing
import pandas as pd

def main():
    print("Reding Input data\n")
    input_data = pd.read_csv("churn.csv")
    print("Data pre-process starts\n")
    preprocess_data = pre_processing(input_data, "churn")
    
    
if __name__ == "__main__":
    main()    