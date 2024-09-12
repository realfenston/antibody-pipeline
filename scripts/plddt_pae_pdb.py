import argparse

import numpy as np
import gemmi

def get_args():
    parser = argparse.ArgumentParser(description="Process PDB file to extract pLDDT, PAE, and interface PAE")
    parser.add_argument("--pdb", required=True, help="Path to the input PDB file")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = get_args()
    
    # Read PDB file using gemmi
    st = gemmi.read_structure(args.pdb)
    
    # Extract relevant information from the structure
    # Assuming 'atom_plddts', 'pae', and 'contact_probs' are stored in the PDB file as custom fields or in some specific way
    # This will need to be adapted based on the actual content and format of your PDB file
    atom_plddts = []
    pae = []
    contact_probs = []
    
    for model in st:
        for chain in model:
            for residue in chain:
                for atom in residue:
                    # Example of how to extract custom fields, if they exist
                    if 'atom_plddt' in atom.b_iso:
                        atom_plddts.append(atom.b_iso['atom_plddt'])
                    if 'pae' in atom.b_iso:
                        pae.append(atom.b_iso['pae'])
                    if 'contact_prob' in atom.b_iso:
                        contact_probs.append(atom.b_iso['contact_prob'])
    
    # Convert to numpy arrays
    plddt = np.array(atom_plddts).mean() if atom_plddts else 0.0
    pae = np.array(pae)
    cp = np.array(contact_probs)
    
    pae_mean = np.mean(pae) if pae.size > 0 else 0.0
    intf_pae = np.sum(pae * cp) / np.sum(cp) if cp.size > 0 else 0.0
    
    print(f"plddt={plddt}, pae_mean={pae_mean}, interface pae={intf_pae}")
