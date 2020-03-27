from Bio import SeqIO
from Bio import AlignIO
from Bio.Seq import Seq
from Bio import pairwise2
from Bio.pairwise2 import format_alignment


def score_match(subject, query, subject_start, query_start, length):
    score = 0
    # for each base in the match
    for i in range(0, length):
        # first figure out the matching base from both sequences
        subject_base = subject[subject_start + i]
        query_base = query[query_start + i]
        # then adjust the score up or down depending on
        # whether or not they are the same
        if subject_base == query_base:
            score = score + 1
        else:
            score = score - 1
    return score


def get_similarity(seq_a, seq_b):
    print(seq_a.id + " compare to ", seq_b.id)
    print('++++++++++++++++++++++++++++++++++')
    seq_a_str = str(seq_a.seq)
    seq_b_str = str(seq_b.seq)
    same_thing = str(seq_a.seq) == str(seq_b.seq)
    if same_thing != True:
        seq_a_len = len(seq_a_str)
        seq_b_len = len(seq_b_str)

        seq_compare_range = min(seq_a_len, seq_b_len)

        print("Length of Sequence A: " + str(seq_a_len))
        print("Length of Sequence B: " + str(seq_b_len))

        sim_score = score_match(
            seq_a_str, seq_b_str, 0, 0, seq_compare_range)

        match_percentage = (sim_score / seq_a_len) * 100

        print("Total match score: " + str(sim_score),
              "Similarity: " + str(match_percentage) + "%")

        # alignment = pairwise2.align.globalxx(seq_a_str, seq_b_str)
        # for al in alignment:
        #     print(al)

    else:
        print("Sequnces are identical")


cc_china_seq = SeqIO.read("./COVID_CHINA.fasta", "fasta")
cc_japan_seq = SeqIO.read("./COVID_JAPAN.fasta", "fasta")
flu_denmark_seq = SeqIO.read("./INFLUENZA_A_VIRUS.fasta", "fasta")

get_similarity(cc_china_seq, flu_denmark_seq)
