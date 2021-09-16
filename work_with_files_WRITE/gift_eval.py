# Добавить 5 к оценкам и чтоб число стало не больше 100
with open('txt_files/class_scores.txt') as score, open('txt_files/new_scores.txt', 'w') as new_score:
    scores = [line.strip().split() for line in score]
    for i in range(len(scores)):
        if int(scores[i][1]) < 100:
            scores[i][1] = int(scores[i][1]) + 5
        if int(scores[i][1]) > 100:
            scores[i][1] = 100
    for i in scores:
        print(i[0], i[1], file=new_score)
