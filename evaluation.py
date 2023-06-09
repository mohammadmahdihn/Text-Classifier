def get_accuracy(y_true, y_predicted):
    #TODO
    """
    Gets two array y_true and y_predicted and returns accuracy of model based on these two.
    y_true is an array that includes ground truth label and y_predicted includes predicted labels.
    """
    correct_predictions = 0
    for i in range(len(y_true)):
        if y_predicted[i] == y_true[i]:
            correct_predictions += 1
    return correct_predictions/len(y_true)

"""
Avarege variable can have three values: 1-'macro' 2-'micro' 3-'binary'.
For Multiclass classification average should be either 'macro' or 'micro' and for Binary classification average
is equal to 'binary'.
You can read this blog: https://medium.com/@ramit.singh.pahwa/micro-macro-precision-recall-and-f-score-44439de1a044 
"""


def get_recall(y_true, y_predicted, average='binary'):
    # TODO
    if average == 'binary':
        true_positive = 0
        false_negative = 0
        for i in range(len(y_true)):
            if y_true[i] and y_predicted[i]:
                true_positive += 1
            elif y_true[i] and not y_predicted[i]:
                false_negative += 1
        return true_positive/(true_positive + false_negative)
    elif average == 'micro':
        true_positive = 0
        false_negative = 0
        for i in range(len(y_true)):
            for j in range(len(y_true[i])):
                if y_true[i][j] and y_predicted[i][j]:
                    true_positive += 1
                elif y_true[i][j] and not y_predicted[i][j]:
                    false_negative += 1
        return true_positive/(true_positive + false_negative)
    elif average == 'macro':
        recalls = list()
        for i in range(len(y_true)):
            true_positive = 0
            false_negative = 0
            for j in range(len(y_predicted[i])):
                if y_true[i][j] and y_predicted[i][j]:
                    true_positive += 1
                elif y_true[i][j] and not y_predicted[i][j]:
                    false_negative += 1
            recalls.append(true_positive/(true_positive + false_negative))
        return sum(recalls)/len(recalls)




def get_precision(y_true, y_predicted, average='binary'):
    # TODO
    if average == 'binary':
        true_positive = 0
        false_positive = 0
        for i in range(len(y_true)):
            if y_true[i] and y_predicted[i]:
                true_positive += 1
            elif y_predicted[i]:
                false_positive += 1
        return true_positive/(true_positive + false_positive)
    elif average == 'micro':
        true_positive = 0
        false_positive = 0
        for i in range(len(y_true)):
            for j in range(len(y_true[i])):
                if y_true[i][j] and y_predicted[i][j]:
                    true_positive += 1
                elif y_predicted[i][j]:
                    false_positive += 1
        return true_positive/(true_positive + false_positive)
    elif average == 'macro':
        precisions = list()
        for i in range(len(y_true)):
            true_positive = 0
            false_positive = 0
            for j in range(len(y_predicted[i])):
                if y_true[i][j] and y_predicted[i][j]:
                    true_positive += 1
                elif y_predicted[i][j]:
                    false_positive += 1
            precisions.append(true_positive/(true_positive + false_positive))
        return sum(precisions)/len(precisions)


def get_f1_score(y_true, y_predicted, average='binary'):
    # TODO
    precision = get_precision(y_true, y_predicted, average)
    recall = get_recall(y_true, y_predicted, average)
    return (2 * precision * recall)/(precision + recall)

"""
Gets two lists as input and integer k as input and returns precision@k.
The actual_list input is a list of elements that should be predicted (without order).
Predicted_list input is a list of elemnts that are predicted (order matters).
"""


def get_precision_k(actual_list, predicted_list, k):
    # TODO

    true_positive = 0
    for i in range(k):
        if actual_list[predicted_list[i]]:
            true_positive += 1
    return true_positive/k


"""
Gets two lists as input and integer k as input and returns mean average precision for the first k elements of predicted_list.
If k=-1 the function should return map for all elements of predicted_list.
The actual_list input is a list of elements that should be predicted (without order).
Predicted_list input is a list of elemnts that are predicted (order matters).
"""


def get_map_k(actual_list, predicted_list, k=-1):
    # TODO

    if k == -1:
        k = len(predicted_list)
    precisions = list()
    for i in range(k):
        if actual_list[predicted_list[i]]:
            precisions.append(get_precision_k(actual_list, predicted_list, i + 1))
    if precisions == []:
        return 0
    return sum(precisions) / len(precisions)