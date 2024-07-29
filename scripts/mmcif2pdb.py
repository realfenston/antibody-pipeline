import argparse

import gemmi


def convert_cif_to_pdb(input_cif, output_pdb):
    doc = gemmi.cif.read_file(input_cif)
    st = gemmi.make_structure_from_block(doc.sole_block())
    st.write_pdb(output_pdb)
    
    
def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--mmcif", required=True, help="input mmcif")
    parser.add_argument("--pdb", required=True, help="output pdb path")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args()
    convert_cif_to_pdb(args.mmcif, args.pdb)