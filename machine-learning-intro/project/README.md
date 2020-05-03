## Identify Fraud from Enron Email

**project folder:**  
1. classifier_features_parameters.txt file captures the final features and parameters for the DecisionTreeClassifier and KNeighborsClassifier.  
2. enron_data.csv file is the output file created in data_exploration.py.  
3. enron61702insiderpay.pdf file is the finance dataset.  
4. final_project_dataset.pkl file is the final project dataset that was provided.  
5. Identify Fraud from Enron Email.pdf file is the project writeup for the required questions.  
6. my_classifier.pkl, my_dataset.pkl and my_feature_list.pkl files are the output from poi.py script for the tester.py script.  
7. poi_id.py is the final project script.  
    a. The clf_choice variable is the input used to set the final algorithm choice.  
    b. The perform_cv boolean was set to True to perform cross-validation but set to False for final analysis.  
8. poi_names.txt file is the list of POI names provided for the project.  
9. references.txt file is a list of all references used for the project.  
10. tester.py script is the evaluation script provided for the project.  


**tools folder:**  
1. feature_update.py script is used to import remove_outliers, calc_cash_received, calc_poi_message for feature update in poi_id.py script.  It must be in the tools folder for the poi_id.py to run successfully.  
2. feature_format.py script was provided to import featureFormat, targetFeatureSplit for formatting of the initial dataset and splitting the labels and features.  
3. data_exploration.py script was used to analyze the dataset to create a df and export to csv for offline review, check missing and valid values for each data point and allocation across classes.  
4. outlier_investigation.py script was used to check for outliers and identify the appropriate data points to be removed from the dataset.  
5. feature_selection.py script was used to perform the initial feature selection processing using the SelectKBest method and prints the best feature k scores.  