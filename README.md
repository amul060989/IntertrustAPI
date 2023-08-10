Deployement Notes:

1. Clone the repo locally. 
2. Navigate to the folder/repo which haven been pulled/cloned locally.
3. Run the follwing command to setup the enviornment:

    ```
    pip install -r requirements.txt
    ```

3. Once the environement setup is comnplete. There will be a feature file folder, which consists of all the feature file(Manual test cases). User need to navigate to the master folder:

    a. To run all the feature files:      

      ```
      behave %feature_file_folder%
      ```


    b. To run indivisual feature file
    
    
      ```
      behave %feature_file_folder%/%feature_file_name%
      ```

    c. To run test suites. Test suites are defined by adding the tags to the Scenarios in the feature file:

```
behave %feature_file_folder%/%feature_file_name% --tag=%tag name%
```

4. To generate allure report, this is a 2 step method

    a. Run the test suite by giving the behave allure command. PSB the command
    
    ```
    behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features
    ```

    b. Generate allure based HTML report
    
``` 
allure generate %allure_html_report_folder% --clean -o %%allure_result_folder%%
```
