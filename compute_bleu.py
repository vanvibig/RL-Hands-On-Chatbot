# from nltk.translate.bleu_score import sentence_bleu
import nltk
import argparse

def argparser():
    Argparser = argparse.ArgumentParser()
    Argparser.add_argument('--reference', type=str, default='summaries.txt', help='Reference File')
    Argparser.add_argument('--candidate', type=str, default='candidates.txt', help='Candidate file')

    args = Argparser.parse_args()
    return args

args = argparser()

reference = open(args.reference, 'r',encoding='utf-8').readlines()
candidate = open(args.candidate, 'r',encoding='utf-8').readlines()

if len(reference) != len(candidate):
    raise ValueError('The number of sentences in both files do not match.')

total_score = 0.
a = 0
for i in range(len(reference)):
    re = reference[i].split()
    ca = candidate[i].split()
    score = nltk.translate.bleu_score.sentence_bleu([re],ca,weights = [1])
    print(score)
    if(score > 0):
        a = a +1
    total_score = total_score + score

# score /= len(reference)
print(a)
avg = total_score/len(reference)
print("Bleu: ",avg)
# print("%f" %score)
# print("The bleu score is: "+str(score))
# python compute_bleu.py --reference re.answer --candidate test.answer