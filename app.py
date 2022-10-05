import streamlit as st 
import pandas as pd 
from PIL import Image
import seaborn as sns
from Bio.Seq import Seq
from Bio import SeqIO


image = Image.open(r'cd.png',mode='r')

st.image(image,use_column_width=True)

st.title(""" 

 Simple Bioinformatics Application

***
""")

st.header('Enter DNA sequence in Fasta format')

def read_fasta(x):
        for seq_record in SeqIO.parse(x,'fasta'):
            return seq_record

sequence_input = ''
# fasta_upload = st.file_uploader('upload fasta',type='fasta')

global sequence

# if fasta_upload is not None:
#     sequence = StringIO.read(fasta_upload)
    
sequence_input=''
sequence = st.text_area('the sequence',sequence_input,height=250)
sequence= sequence.splitlines()
sequence = sequence[1:]
sequence= ''.join(sequence)

st.write(""" 
***
""")

st.header('The input DNA query')

sequence

st.write("""
***
 """)

st.header("DNA nucleotide count")


def DNA_nucleotide_count(seq):
    d = dict([
    ('A',seq.count('A')),
    ("T",seq.count("T")),
    ("C",seq.count('C')),
    ('G',seq.count('G'))
    ])
    return d

x = DNA_nucleotide_count(sequence)

st.write(f'there are'+ " "+ str(x['A'])+ " " + 'Adenine (A)')

st.write(f'there are' +" "+ str(x['T']) +" "+ 'Thymine (T)')

st.write(f'there are'+" "+  str(x['C']) +" "+ 'Cytosine (C)')

st.write(f'there are'+" "+  str(x['G']) +" "+ 'Guanine (G)')

# making dta frame 
df = pd.DataFrame.from_dict(x,orient='index')
df = df.rename({0:'Count'},axis= 'columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index':'nucleotide'})
# print(df)
# displaying bar chart

fig  = sns.barplot(data=df,x= 'nucleotide',y= 'Count')

st.write(fig)

st.write(''' 

***
''')

st.header('mRNA transcript')

def Transcription(seq):
    '''Allow the transcription of DNA into mRNA'''
    return seq.replace('T','U')

st.write(Transcription(sequence))

st.write(''' 
***
''')

st.header('Translation of mRNA')

myseq = Seq(sequence[1:])

st.write(myseq.translate())

st.write(''' "*" symbol stands for stop codon 

"-" symbole stands for gaps

***
''')

