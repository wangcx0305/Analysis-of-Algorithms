I put the alignfunc.py, coster.py, runtime.py together with imp2cost.txt and imp2input.txt
in the same folder and use python3.5 to get the result file imp2output.txt under the same folder. To get the result file, I run “python3.5 coster.py” in mac terminal.

alignfunc.py: include three self defined function editdistance, backtrace, alignseq, which are used to compute the minimum edit distance, to construct the backtrace matrix and to align two sequence.

coster.py: .py file to generate imp2input.txt using imp2cost.txt, imp2input.txt and the self defined function in alignfunc.py

runtime.py: .py file to compute the empirical time and make plot