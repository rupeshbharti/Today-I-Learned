During your check-in, Charithra outlines your key objectives:

Review the provided dataset and assess its structure, completeness, and key attributes, and then identify any missing or inconsistent data points that could affect predictions.
Use GenAI-assisted tools to generate insights while ensuring data confidentiality and avoiding the exposure of sensitive financial information.
Summarize the patterns, anomalies, and risk indicators that should be considered in later stages of the project in a report.

## Generating model code without coding
With the right prompts, GenAI can generate an initial modeling workflow in Python, R, or SQL. However, these outputs should be viewed as a starting point—manual review and refinement are essential to ensure alignment with best practices..

💡 Example GenAI prompt:
"Generate a logistic regression model framework using this dataset to predict customer delinquency. Provide an explanation of each step, ensuring outputs are reviewed and refined for accuracy and fairness."

## Evaluating model performance
Once a model is built, its accuracy must be assessed. GenAI can:

Suggest evaluation metrics (e.g., accuracy, precision, recall).
Interpret results and suggest improvements.
Highlight ethical concerns, such as potential biases.

💡 Example GenAI prompt:
"Evaluate the performance of this predictive model using precision and recall. Identify any biases in the predictions."

## 💡 Decision Tree Example GenAI prompt:
"Generate a decision tree model to predict delinquency risk based on income, credit utilization, and missed payments. Explain how the model determines risk categories."

## 💡 Logistic Regression Example GenAI prompt:
"Explain how logistic regression can be used to predict credit card delinquency. Generate a simple model using income, debt-to-income ratio, and payment history."
"Generate a logistic regression model using this dataset to predict customer delinquency. Include preprocessing steps and evaluation metrics."

## 💡 Neural Networks Example GenAI prompt:
"Create a basic neural network model for predicting delinquency risk. Compare its strengths and weaknesses against decision trees and logistic regression."

## 💡 Bias Example GenAI prompt:
“Check for bias in this credit risk model. Are certain customer groups unfairly predicted as high risk?”

## 💡 Explainability Example GenAI prompt:
"Explain why this model predicted high delinquency risk for a specific customer."
*While GenAI is great for assisting in summarizing explanations, relying solely on it for explainability presents significant risks—it may "hallucinate" or generate inaccurate justifications that do not reflect the true model logic. Best practice is to use established interpretability frameworks to ensure transparency and accuracy.

## 💡 Fairness Example GenAI prompt:
"Assess fairness in this model’s predictions. Does it disproportionately flag certain customer demographics as high risk?"

## 💡 Refining Example GenAI prompt:
"Analyze this model’s performance and suggest improvements to increase accuracy and reduce bias."
