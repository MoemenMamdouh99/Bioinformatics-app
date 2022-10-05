import streamlit as st 
import pandas as pd 
from PIL import Image
import plotly_express as px
from Bio.Seq import Seq
from Bio import SeqIO


image = Image.open(r'C:\Users\lenovo\OneDrive\Desktop\python\my projects\bioinformatics app\central dogma.png')

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
    
# else:
if sequence_input[0:]=='>':
    sequence = st.text_area('the sequence',sequence_input,height=250)
    sequence= sequence.splitlines()
    sequence = sequence[1:]
    sequence= ''.join(sequence)
else:
    sequence = st.text_area('the sequence',sequence_input,height=250)
    sequence = sequence.splitlines()
    sequence = ''.join(sequence)

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
# displaying pie chart

fig  = px.bar(df, x='nucleotide',y='Count')
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

myseq = Seq(sequence)

st.write(myseq.translate())

st.write(''' "*" symbol stands for stop codon 

"-" symbole stands for gaps

***
''')
