from data_prep import pre_processing
import pandas as pd

def main():
    print("Reding Input data\n")
    input_data = pd.read_csv("DiamondsPrices.csv")
    print("Data pre-process starts\n")
    preprocess_data = pre_processing(input_data)
    
    
if __name__ == "__main__":
    main()  