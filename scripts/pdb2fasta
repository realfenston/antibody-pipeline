import argparse
from Bio import PDB
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import SeqIO

def get_args():
    parser = argparse.ArgumentParser(description="Convert PDB file to sequence file")
    parser.add_argument("--pdb", required=True, help="Path to the input PDB file")
    parser.add_argument("--fasta", required=True, help="Path to the output FASTA file")
    args = parser.parse_args()
    return args

def pdb_to_fasta(pdb_path, fasta_path):
    parser = PDB.PDBParser()
    structure = parser.get_structure('structure', pdb_path)
    
    sequences = []
    for model in structure:
        for chain in model:
            sequence = ''
            for residue in chain:
                if PDB.is_aa(residue):
                    sequence += PDB.Polypeptide.three_to_one(residue.resname)
            sequences.append(SeqRecord(Seq(sequence), id=chain.id, description=""))
    
    SeqIO.write(sequences, fasta_path, "fasta")

if __name__ == '__main__':
    args = get_args()
    pdb_to_fasta(args.pdb, args.fasta)

##pip install biopython
##python pdb_to_fasta.py --pdb input.pdb --fasta output.fasta
