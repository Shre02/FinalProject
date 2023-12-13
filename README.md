# Project Title: AdaptiveCloudEnsemble (ACE)

## Overview
The AdaptiveCloudEnsemble (ACE) is a sophisticated cloud workload prediction system designed to handle the complexities of concept drift in dynamic cloud environments. Utilizing a combination of advanced machine learning algorithms, the ACE model offers enhanced predictive resource management, ensuring accuracy and adaptability in real-time cloud data processing.

## Features
- Implementation of ensemble learning techniques using XGBoost, AdaptiveRandomForest, and Streaming Random Patches (SRP) classifiers.
- Integration with AWS services like Kinesis Datastreams, Glue, and S3 for efficient data streaming and storage.
- Advanced concept drift detection and adaptation using DDM drift detector.
- Comprehensive statistical analysis using accuracy, precision, recall, and F1-score.

## Installation & Setup
Follow the steps given in the Configuration Manual file.

### Prerequisites
- Python 3.x
- AWS account and configuration
- Required Python libraries: `river`, `xgboost`, `boto3`,'pandas','lightgbm'.

### Setup Instructions
1. Clone the repository: `git clone https://github.com/your-repository-url`
2. Upload the Iotproducer.py and csv dataset file to Cloud9
3. Upload the 21195773_SourceCode.ipynb to Sagemaker Studio Notebook

## Usage
To run the Iotproducer.py file on Cloud9 in the terminal use python Iotproducer.py
To implement the cells in the 21195773_SourceCode.ipynb notebook use the 'Run' button or keyboard shortcut 'shift+enter'
