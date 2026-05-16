from sklearn.feature_extraction.text import TfidfVectorizer

negative_sentences = [
    "I was deeply disappointed with the service at the restaurant.",
    "The movie was awful, and I regretted spending money on tickets.",
    "Her constant criticism made me feel worthless and upset.",
    "The weather ruined our vacation; it was rainy and cold the entire time.",
    "I felt overwhelmed and stressed by the high workload and tight deadlines.",
    "The customer support was terrible; they were unresponsive and unhelpful.",
    "The news of the company's bankruptcy was devastating for its employees.",
    "The food was tasteless, and I couldn't finish my meal.",
    "The presentation was a disaster, and I forgot half of my points.",
    "The long wait and delays at the airport were frustrating and exhausting."
]

positive_sentences = [
    "I love spending time with my family.",
    "The concert was absolutely amazing.",
    "The team's hard work paid off, and we won the championship.",
    "She received a promotion, and she is over the moon.",
    "The movie had a heartwarming and uplifting ending.",
    "The compliments I received on my presentation made me feel proud of my work.",
    "The beautiful scenery took my breath away.",
    "The surprise gift brought tears of joy to her eyes.",
    "The delicious food at the restaurant left me completely satisfied.",
    "He is incredibly talented and deserves all the success."
]

tfid_vector_neg = TfidfVectorizer(negative_sentences)
tfid_vector_pos = TfidfVectorizer(positive_sentences)
print(tfid_vector_neg)

