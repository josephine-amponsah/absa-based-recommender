# Aspect Sentiment Generator

When looking up products or services to patronise, reviews of past customer form an essential part of decision making. Having to go through tons of reviews of several products can be quite tasking. From the perspective of businesses, assessing 1000s of customer reviews to pick out pain points or recommendation can also be quite the work.

With Aspect-Based Sentiment Analysis (ABSA), neither parties have to do all that work. ABSA generates sentiments of reviews or comments, fishing out subject(s) of each comment and providing the sentiment around them

In this sub-project is aimed at building a model that generates sentiments of reviews under subjects/categories related to a service. In this case, the service of interest is one provided by hotels or resorts in Ghana to tourists /customers.

## Skills

- Text Data Processing
- Word Embedding
- NLP
- Aspect-Based Sentiment Analysis
- Document clustering

# Table of Contents

1. Code Structure
2. Tools & Packages
3. Data
4. ML Model Training & Evaluation
5. Results
6. Future Development

# Code Structure

# Tools & Packages

## Frameworks

- NLTK
- PyABSA
- Pandas
- Gensim
- FastAPI
- Googletrans
- TextBlob

## Languages

- Python

# Data

## Data collection

Data of destinations were scraped from the web using APIFY's python client. The scraped data of destinations and their latest 50 reviews were written to a json file.

## Data cleaning

To extract the reviews data only, json data was then transform into a dataframe with: destination id, the date, rating and comment of each view into a dataframe. The data format/type of each column was assessed to ensure conformity to the desire data type. It was then stored in another json file.

# ML Model Training & Evaluation

## Feature engineering

To prep the data for the training of the NLP model, :

- stopwords were removed
- punctuations were eliminated
- language of all non-english reviews were converted to english

## ABSA model inferencing (ATEPC)

The model used is a pre-trained BERT model for aspect sentiment extraction. The ATEPC model from the PyABSA library was selected based on the output structure. The model was the inference with the prepped data to generate aspects and sentiments per review.

## Aspect clustering with Word2Vec

The resulting aspects were many and needed to be categorized under specific labels for proper aggregation of sentiments.

- reviews data was tokenized
- a Word2Vec model was trained on the reviews data
- the vectors of selected labels and the generated aspects were passed to cosine similarity function.
- the aspect were then replaced with labels they were closest to

Hallucinations, wrong placements of a significant number of aspects, were observed in the resulting data. Requiring that the model be retrained on better prepared or more data

## ABSA model training & inferencing

The data was preprocessed again, applying lemmatization, bigram tokenization and removal of caps.
Other models from the PyABSA library were experimented on. Each model was trained on the project data before inferencing.
With the introduction of the Category Aspect Sentiment generator (ABSAInstruction), further clustering the generated is no more needed.

<!-- # Results -->

# Future Development

1. Replace model with ABSAIntruction (Category-Aspect Sentiment Generator)
2. Build API for model deployment to applications
3. Build API documentation
