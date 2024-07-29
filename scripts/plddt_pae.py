import argparse
import json

import numpy as np


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--pdb", required=True, help="")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args()
    
    with open(args.pdb, 'r') as f:
        cont = json.load(f)
        
    plddt = np.array(cont['atom_plddts']).mean()
    pae = np.array(cont['pae'])
    cp = np.array(cont['contact_probs'])
    
    pae_mean = np.mean(pae)
    intf_pae = np.sum(pae * cp) / np.sum(cp)
    
    print(f"plddt={plddt}, pae={pae}, interface pae={intf_pae}")