# EDS 220 - Assignment 1, tasks 2 and 3 - OTTER GRADER FILES

This respository contains materials to set up the otter grader for the first assignment for the course [EDS 220 - Working with Environmental Datasets](https://meds-eds-220.github.io/MEDS-eds-220-course/). This course is part of the [UCSB Masters in Environmental Data Science](https://bren.ucsb.edu/masters-programs/master-environmental-data-science).

## File description

## Repository contents
    └── data/                                      # contains all data needed to run the notebook, csvs that start with t2 or t3 are used in the otter tests to                                                                check if the student's solution matches the csv with the solution
        └── coral_data.csv                         # coral data used for task 2
        └── earthquake_data.csv                    # earthquake data used for task 3
        └── t2_q3d_df.csv                          # solution dataframe for task 2 question 3d
        └── t2_q10_df.csv                          # solution dataframe for task 2 question 10
        └── t2_q11_df.csv                          # solution dataframe for task 2 question 11
        └── t2_q14_df.csv                          # solution dataframe for task 2 question 14
        └── t2_q8_df.csv                           # solution dataframe for task 2 question 8
        └── t2_q9_df.csv                           # solution dataframe for task 2 question 9
        └── t3_q1c_df.csv                          # solution dataframe for task 3 question 1c
        └── t3_q4a_df.csv                          # solution dataframe for task 3 question 4a
        └── t3_q4b_df.csv                          # solution dataframe for task 3 question 4b
        └── t3_q7a_df.csv                          # solution dataframe for task 3 question 7a
        └── t3_q8_df.csv                           # solution dataframe for task 3 question 8
            
    └── dist-task2/                                        
        └── autograder/                                              
            └── data/                                      # contains all data needed to run the notebook, csvs that start with t2 or t3 are used in the otter tests 
                                                             to check if the student's solution matches the csv with the solution
                └── coral_data.csv                         # coral data used for task 2
                └── earthquake_data.csv                    # earthquake data used for task 3
                └── t2_q3d_df.csv                          # solution dataframe for task 2 question 3d
                └── t2_q10_df.csv                          # solution dataframe for task 2 question 10
                └── t2_q11_df.csv                          # solution dataframe for task 2 question 11
                └── t2_q14_df.csv                          # solution dataframe for task 2 question 14
                └── t2_q8_df.csv                           # solution dataframe for task 2 question 8
                └── t2_q9_df.csv                           # solution dataframe for task 2 question 9
                └── t3_q1c_df.csv                          # solution dataframe for task 3 question 1c
                └── t3_q4a_df.csv                          # solution dataframe for task 3 question 4a
                └── t3_q4b_df.csv                          # solution dataframe for task 3 question 4b
                └── t3_q7a_df.csv                          # solution dataframe for task 3 question 7a
                └── t3_q8_df.csv                           # solution dataframe for task 3 question 8
            └── tests/                                     # this folder contains all the individual tests as .py files, this folder is automatically created when                                                                     running otter assign
                └── q3_a.py                                # .py test file for question 3a
                └── q3_b.py                                # .py test file for question 3b
                └── q3_c.py                                # .py test file for question 3c
                └── q3_d.py                                # .py test file for question 3d
                └── q6.py                                  # .py test file for question 6
                └── q8.py                                  # .py test file for question 8
                └── q9.py                                  # .py test file for question 9
                └── q10.py                                 # .py test file for question 10
                └── q11.py                                 # .py test file for question 11
                └── q14.py                                 # .py test file for question 14
                
            └── hwk1-task2-corals-autograder_2024_10_03T09_54_28_028866.zip   # this is the task 2 zip file for the gradescope autograder configuration, this file gets                                                                                  uploaded directly into gradescope
            └── hwk1-task2-corals.ipynb                    # this is the task 2 notebook with solutions (no tests), it is used to uploaded to gradescope as a test file                                                               to ensure all tests are properly working
        └── student/
            └── data/                                      # contains all data needed to run the notebook, csvs that start with t2 or t3 are used in the otter tests 
                                                             to check if the student's solution matches the csv with the solution
                └── coral_data.csv                         # coral data used for task 2
                └── earthquake_data.csv                    # earthquake data used for task 3
                └── t2_q3d_df.csv                          # solution dataframe for task 2 question 3d
                └── t2_q10_df.csv                          # solution dataframe for task 2 question 10
                └── t2_q11_df.csv                          # solution dataframe for task 2 question 11
                └── t2_q14_df.csv                          # solution dataframe for task 2 question 14
                └── t2_q8_df.csv                           # solution dataframe for task 2 question 8
                └── t2_q9_df.csv                           # solution dataframe for task 2 question 9
                └── t3_q1c_df.csv                          # solution dataframe for task 3 question 1c
                └── t3_q4a_df.csv                          # solution dataframe for task 3 question 4a
                └── t3_q4b_df.csv                          # solution dataframe for task 3 question 4b
                └── t3_q7a_df.csv                          # solution dataframe for task 3 question 7a
                └── t3_q8_df.csv                           # solution dataframe for task 3 question 8
           └── tests/                                     # this folder contains all the individual tests as .py files, this folder is automatically created when                                                                     running otter assign
                └── q3_a.py                                # .py test file for question 3a
                └── q3_b.py                                # .py test file for question 3b
                └── q3_c.py                                # .py test file for question 3c
                └── q3_d.py                                # .py test file for question 3d
                └── q6.py                                  # .py test file for question 6
                └── q8.py                                  # .py test file for question 8
                └── q9.py                                  # .py test file for question 9
                └── q10.py                                 # .py test file for question 10
                └── q11.py                                 # .py test file for question 11
                └── q14.py                                 # .py test file for question 14
            └── hwk1-task2-corals.ipynb                    # this is the notebook that should be distrubted to the students, all solutions are removed and all tests are      └── dist-task3/                                        
        └── autograder/                                              
            └── data/                                      # contains all data needed to run the notebook, csvs that start with t2 or t3 are used in the otter tests 
                                                             to check if the student's solution matches the csv with the solution
                └── coral_data.csv                         # coral data used for task 2
                └── earthquake_data.csv                    # earthquake data used for task 3
                └── t2_q3d_df.csv                          # solution dataframe for task 2 question 3d
                └── t2_q10_df.csv                          # solution dataframe for task 2 question 10
                └── t2_q11_df.csv                          # solution dataframe for task 2 question 11
                └── t2_q14_df.csv                          # solution dataframe for task 2 question 14
                └── t2_q8_df.csv                           # solution dataframe for task 2 question 8
                └── t2_q9_df.csv                           # solution dataframe for task 2 question 9
                └── t3_q1c_df.csv                          # solution dataframe for task 3 question 1c
                └── t3_q4a_df.csv                          # solution dataframe for task 3 question 4a
                └── t3_q4b_df.csv                          # solution dataframe for task 3 question 4b
                └── t3_q7a_df.csv                          # solution dataframe for task 3 question 7a
                └── t3_q8_df.csv                           # solution dataframe for task 3 question 8
            └── tests/                                     # this folder contains all the individual tests as .py files, this folder is automatically created when                                                                    running otter assign in the terminal
                └── q1_c.py                                # .py test file for question 1c
                └── q2_a.py                                # .py test file for question 2a
                └── q2_b.py                                # .py test file for question 2b
                └── q2_c.py                                # .py test file for question 2c
                └── q3.py                                  # .py test file for question 3
                └── q4_a.py                                # .py test file for question 4a
                └── q4_b.py                                # .py test file for question 4b
                └── q5.py                                  # .py test file for question 5
                └── q7_a.py                                # .py test file for question 7a
                └── q8.py                                  # .py test file for question 8
                
            └── hwk1-task3-earthquakes-autograder_2024_10_02T20_47_06_767946.zip  # this is the task 3 zip file for the gradescope autograder configuration, this file                                                                                       gets uploaded directly into gradescope
            └── hwk1-task3-earthquakes.ipynb               # this is the task 3 notebook with solutions (no tests), it is used to uploaded to gradescope as a test file                                                               to ensure all tests are properly working
        └── student/
            └── data/                                      # contains all data needed to run the notebook, csvs that start with t2 or t3 are used in the otter tests 
                                                             to check if the student's solution matches the csv with the solution
                └── coral_data.csv                         # coral data used for task 2
                └── earthquake_data.csv                    # earthquake data used for task 3
                └── t2_q3d_df.csv                          # solution dataframe for task 2 question 3d
                └── t2_q10_df.csv                          # solution dataframe for task 2 question 10
                └── t2_q11_df.csv                          # solution dataframe for task 2 question 11
                └── t2_q14_df.csv                          # solution dataframe for task 2 question 14
                └── t2_q8_df.csv                           # solution dataframe for task 2 question 8
                └── t2_q9_df.csv                           # solution dataframe for task 2 question 9
                └── t3_q1c_df.csv                          # solution dataframe for task 3 question 1c
                └── t3_q4a_df.csv                          # solution dataframe for task 3 question 4a
                └── t3_q4b_df.csv                          # solution dataframe for task 3 question 4b
                └── t3_q7a_df.csv                          # solution dataframe for task 3 question 7a
                └── t3_q8_df.csv                           # solution dataframe for task 3 question 8
           └── tests/                                     # this folder contains all the individual tests as .py files, this folder is automatically created when                                                                    running otter assign
                └── q1_c.py                                # .py test file for question 1c
                └── q2_a.py                                # .py test file for question 2a
                └── q2_b.py                                # .py test file for question 2b
                └── q2_c.py                                # .py test file for question 2c
                └── q3.py                                  # .py test file for question 3
                └── q4_a.py                                # .py test file for question 4a
                └── q4_b.py                                # .py test file for question 4b
                └── q5.py                                  # .py test file for question 5
                └── q7_a.py                                # .py test file for question 7a
                └── q8.py                                  # .py test file for question 8
            └── hwk1-task3-earthquakes.ipynb               # this is the notebook that should be distrubted to the students, all solutions are removed and all                                                                        tests are hidden                                                                                                                       
        
    └── .gitignore                  
    └── LICENSE
    └── hwk1-task2-corals.ipynb                            # this is the master notebook for task 2, it contains all solutions and tests, this notebook is used to                                                                    generare the student notebook and all necessary files for the assignemnt
    └── hwk1-task3-earthquakes.ipynb                       # this is the master notebook for task 3, it contains all solutions and tests, this notebook is used to                                                                    generare the student notebook and all necessary files for the assignemnt
    └── README.md                                    

