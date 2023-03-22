file = open("Output.txt", 'w+')
# print("Task 1", file=file)
# print("Step 1: Started to crawl context", file=file)
# from Crawler import main
# main.crawler_main()
# print("Crawling finished", file=file)

# print("Step 2: Use text summary for text crawling", file=file)
# from Summarization import main
# main.summary()
# print("Summary finished", file=file)


# print("Step 3: Use QA model on the collected context", file=file)
# from QA import main
# main.main()
# print("Step 3 completed", file=file)

# print("Step 4: COSMOS baseline", file=file) 
# import sys 
# sys.path.append('./COSMOS')
# from COSMOS import evaluate_ooc

# print('Running COSMOS')
# evaluate_ooc.main(None)

print("Step 5: Boosting", file=file)
import pandas as pd
from evaluate_utils import *
df = pd.read_csv('df_answer.csv')
print(df.head(5))
cosmos_iou = pd.read_csv('pred_contexts.txt', header=None)
cosmos_iou.columns = ['iou']
df = pd.concat([df, cosmos_iou['iou']], axis=1)

docnli = eval(open('docnli.txt', 'r').read())
df['nli'] = docnli

# print(df.head(5))
print('Evaluating...', file=file)
confusion_matrix, result, method_acc = evaluate(df, predict_final)
print("Confusion matrix", confusion_matrix, file=file)
print("Acc", result, file=file)
print("Method_acc", method_acc, file=file)
# print(df.head(5))

