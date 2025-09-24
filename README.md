# Files and Plan

## Make Dataset
The first thing will be to make the dataset. For this, we have some data from the [repo of the authors](https://github.com/aaronmueller/clams) that we will convert into data that our models can parse. This means we will make a python file to automate the process and use the resulting .tsv file as our data.
## Make Config
To run the proper evaluate and analyze experiments on our models, we will create one yaml file. This will include paths to the data alongside both BERT and mBert.
## Run Models
This will be simply running NLPScholar and getting the results, additionally to do this step, proper paths such as data, predictions and results will be made.
## Get Statistics
The final result will be going through the results from running the models and getting some statistical informationo from them. We will run a python file to do some of this statistical analysis, and ultimately include this in the final replication write-up.
