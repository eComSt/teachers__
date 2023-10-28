data = {
    'Петя': {'Физика': 50, 'Математика': 80, 'Биология': 90},
    'Ваня': {'Математика': 65, 'Химия': 64, 'Физика': 90, 'РЯ': 78},
    'Катя': {'РЯ': 45, 'История': 57, 'Математика': 87}
}

for name, subjects in data.items():
    summ = sum(subjects.values())
    # print(f'Сумма баллов ученика {name}: {summ}')
subject_scores = {}
for line in data.values():
    # print(line)
    # input()
    for subject in line:
        if subject in subject_scores:
            subject_scores[subject].append(line[subject])
        else:
            subject_scores[subject]=[line[subject]]
        print(subject_scores)

for subject, scores in subject_scores.items():
    summ_sr = sum(scores)/len(scores)
    print(f'Средний балл по предмету {subject}: {summ_sr}')