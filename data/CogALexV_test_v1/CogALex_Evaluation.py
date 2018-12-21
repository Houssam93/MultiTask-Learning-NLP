#!/usr/bin/python
#
# Author: Stefan Evert, Enrico Santus
# Description: Calculate Precision, Recall and F1 for the CogALex-V Shared Task, given the goldstandard and the output file.
#

from __future__ import print_function

import codecs
import sys
from docopt import docopt
from sklearn.metrics import precision_recall_fscore_support

def main():
    """
    Calculate Precision, Recall and F1 for CogALex-V Shared Task, given the goldstandard and the output files
    """

    # Get the arguments
    args = docopt("""Calculate official Precision, Recall and F1 scores for CogALex-V Shared Task.

Usage:
    CogALex_Evaluation.py <goldstandard_file> <output_file>

    <goldstandard_file> = a TAB-delimited file with word pairs and gold standard labels (either subtask 1 or subtask 2)
    <output_file> = a TAB-delimited file with word pairs and labels predicted by the system
    """)

    goldstandard_file = args['<goldstandard_file>']
    output_file = args['<output_file>']

    # Load the goldstandard and outupt files
    print('Loading the datasets ...')
    goldstandard, gold_tbl = load_dataset(goldstandard_file)
    system, sys_tbl = load_dataset(output_file)

    # Make sure goldstandard and output files are in the same order
    if (gold_tbl[0] != sys_tbl[0]) or (gold_tbl[1] != sys_tbl[1]):
        print("\nERROR: word pairs must appear exactly in the same order as in the input file.")
        sys.exit(1)

    # Gold labels and system labels
    gold = gold_tbl[2]
    pred = sys_tbl[2]
    
    if "TRUE" in gold:
        # Appears to be the Task 1 gold standard
        print("Evaluating subtask 1 ...")
        check_values(gold, ("TRUE","FALSE"), msg="ERROR in gold standard")
        check_values(pred, ("TRUE","FALSE"), msg="ERROR in system output", subset=True)

        # Calculate evaluation metrics for class TRUE
        p, r, f1, support = precision_recall_fscore_support(gold, pred, pos_label=None, labels=("TRUE",), average="weighted")
        print('Subtask 1:  P = %.3f  R = %.3f  F1 = %.3f' % (p, r, f1))

    else:
        # Appears to be the Task 2 gold standard
        print("Evaluating subtask 2 ...")
        labels = ("RANDOM", "SYN", "ANT", "HYPER", "PART_OF")
        check_values(gold, labels, msg="ERROR in gold standard")
        check_values(pred, labels, msg="ERROR in system output", subset=True)
        
        # Calculate evaluation metrics for each class (except RANDOM)
        labels = labels[1:]
        p_vec, r_vec, f1_vec, supp_vec = precision_recall_fscore_support(gold, pred, pos_label=None, labels=labels, average=None)
        for l, p, r, f1, s in zip(labels, p_vec, r_vec, f1_vec, supp_vec):
            print('%9s:  P = %.3f  R = %.3f  F1 = %.3f  n =%4d' % (l, p, r, f1, s))
        
        # Overall score = weighted average over the non-RANDOM classes
        p, r, f1, support = precision_recall_fscore_support(gold, pred, pos_label=None, labels=labels, average="weighted")
        print('Subtask 2:  P = %.3f  R = %.3f  F1 = %.3f' % (p, r, f1))


def load_dataset(dataset_file):
    """
    Loads a dataset file
    :param dataset_file: the file path
    :return: a list of table rows [x, y, relation] and list of table columns
    """

    # Load the file as a list of rows
    with codecs.open(dataset_file, 'r', 'utf-8') as f_in:
        dataset = [list(line.strip().split('\t')) for line in f_in]

    # Convert into list of columns
    columns = list(zip(*dataset))

    # Return the dataset in row format and in column format
    return dataset, columns

def check_values(x, labels, msg="ERROR", subset=False):
    x_set = set(x)
    lab_set = set(labels)
    if subset:
        if not x_set <= lab_set:
            print("\n%s: found labels %s but only %s are allowed" % (msg, ", ".join(x_set), ", ".join(lab_set)))
            sys.exit(1)
    else:
        if x_set != lab_set:
            print("\n%s: expected labels %s but found %s" % (msg, ", ".join(x_set), ", ".join(lab_set)))
            sys.exit(1)


if __name__ == '__main__':
    main()
