# iTunes Podcast Reviews - Data Analysis

## Introduction
This project delves into a vast dataset of 2 million podcast reviews for 100,000 unique podcasts, updated monthly on iTunes. Our primary aim is to derive valuable insights from this extensive textual feedback and review data.

## Project Objective
Our core objective is to employ data science and machine learning techniques to gain a profound understanding of iTunes podcast reviews. By conducting comprehensive data analysis and constructing a machine learning model using the BERT framework from Google, we strive to unearth trends, sentiments, and patterns within this expansive dataset. The ultimate goal is to provide actionable insights for podcast creators, advertisers, and enthusiasts.

## Methodology
### 1. Data Loading and Preparation
We loaded and prepared the dataset for analysis.

### 2. Data Cleaning
Data cleaning was performed to address missing values, inconsistencies, and outliers.

### 3. Exploratory Data Analysis (EDA)
The EDA phase involved extensive data exploration and visualization. Key elements of EDA included:
   - **Statistical Summaries:** Understanding the data's basic characteristics.
   - **Charts and Visualizations:** Visualizing trends and distributions.
   - **Correlation Analysis:** Discovering relationships between variables.
   - **Testing for Anomalies:** Identifying and handling outliers or anomalies.

### 4. Data Analysis
The data analysis phase focused on deriving meaningful insights and patterns from the dataset. Key elements of the analysis consisted of:
   - **Prediction Analysis:** Developing a BERT-based machine learning model for predictive tasks.
   - **Inferential Statistical Analysis:** Extracting actionable insights through statistical methods.

We fine-tuned a BERT model using the pre-trained 2-layer, 128-hidden, 12-attention-head, 110M-parameter BERT model (Turc et al., 2019) by training it on the podcast reviews and ratings. This specialized NLP model enables in-depth analysis of review text and associated ratings.
   - To retrain the model:
```bash
python run_classifier.py 
	--task_name=cola 
	--do_train=true 
	--do_eval=true 
	--do_predict=true 
	--data_dir=./data/ 
	--vocab_file=./uncased_L-2_H-128_A-2/vocab.txt 
	--bert_config_file=./uncased_L-2_H-128_A-2/bert_config.json 
	--init_checkpoint=./uncased_L-2_H-128_A-2/bert_model.ckpt 
	--max_seq_length=128 
	--train_batch_size=32 
	--learning_rate=2e-5 
	--num_train_epochs=3.0 
	--output_dir=./bert_output/ 
	--do_lower_case=True
```
   - To use the trained model for predictions on the test data, *test.tsv*:
       - Go into the *bert_output* directory and record the highest number of the *model.ckpt* file
       - Run the following command after having replaced `<n_max>` with that highest number:

 ```bash
python run_classifier.py 
    --task_name=cola 
    --do_predict=true 
    --data_dir=./data 
    --vocab_file=./uncased_L-2_H-128_A-2/vocab.txt 
    --bert_config_file=./uncased_L-2_H-128_A-2/bert_config.json 
    --init_checkpoint=./bert_output/model.ckpt-<n_max>
    --max_seq_length=128 
    --output_dir=./bert_output
 ```


### 5. Data Visualization
The project utilized Matplotlib and Seaborn to create visually appealing and informative charts and plots that complemented the analysis.

### 6. Explanation and Interpretation
Clear and concise explanations were provided in the notebook to guide the reader through the analysis process. The results and their implications were thoroughly explained to facilitate a better understanding of the findings.

### 7. Suggestions and Recommendations
We offer concrete suggestions and recommendations based on the analysis to enhance the effectiveness of leveraging podcast reviews. These insights are invaluable for podcast creators and stakeholders. It's important to note that our model, while specialized, may not achieve the accuracy of larger models, warranting further research with more powerful hardware to create a state-of-the-art BERT model.

## Conclusion
This project presents a comprehensive analysis of iTunes podcast reviews, empowering podcast creators and enthusiasts with actionable insights from a dynamic dataset. It also serves as a valuable resource for those interested in the technical aspects of BERT models and NLP for review analysis, particularly within the podcast domain.

## Contributing
Pull requests are welcome. For significant changes, please open an issue to discuss proposed modifications. Ensure that tests are added or updated as needed.

## Citation
   1. Turc, I., Chang, M.-W., Lee, K., & Toutanova, K. (2019). [Well-Read Students Learn Better: On the Importance of Pre-training Compact Models](https://arxiv.org/abs/1908.08962v2). arXiv preprint arXiv:1908.08962v2.

## Changelog
For a detailed history of changes, please refer to the [CHANGELOG](CHANGELOG.md) file.

## License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
