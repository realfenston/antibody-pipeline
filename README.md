# step-by-step guide for structural quality estimation of targeting antibodies.

**1. create a virtual env from current requirements.txt file**
```
conda create -n ab_design python=3.8
conda activate ab_design
pip install -r requirements.txt
```

**2. in case you are having only the sequence, get the corresponding structure with the server.**
```
#AlphaFold3
https://alphafoldserver.com/

#AlphaFold2-Multimer
https://colab.research.google.com/github/deepmind/alphafold/blob/main/notebooks/AlphaFold.ipynb
```
the whole structure prediction process might take few minutes to complete.

**3. download the most reasonable .mmcif file to ./examples dir, and convert it to .pdb format for estimation**
```
pip install gemmi
python scripts/mmcif2pdb.py --mmcif $in_mmcif --pdb $out_pdb
```

**4. complex binding energy**   
cbe = [complex energy - (antigen energy + antibody energy)], we run openmm to get approximation.
```
python scripts/mmcif2pdb.py --complex $in_complex --antigen $in_antigen --antibody $in_antibody
```
the console will print out the corresponding binding energy.

**5. abopt energy**   
please check Appendix.3 once the code repo is published released, this should come in the near future.

**6. log likelihoods**
this estimate the possibility of the sequence giving the current pdb structure, which can be estimated using the scripts under ./structural-evolution dir.
```
cd ./structural-evolution
python bin/score_log_likelihoods.py pdbfile $in_pdb
```
this script is kindly based on esm-if repo, you may find it online for further reference.

**7. af3 metrics**   
the following metrics, including plddt, pae, interface pae, are based on AlphaFold3 and not yet verified on af2-multimer, but it is totally open to you for further verification. the overall process should be more or less similar.
```
python scripts/plddt_pae.py
```
the console will then print all the plddt and pae related metrics. ptm is another important structural metric, it is used to understand to which extent the prediction result is analogous to the ground truth folding result.

**8. binding specificity**   
currently there is no known model for understanding this antibody-antigen characteristic. leave it for further investigation.

**9. pipeline building**   
pending work, integrate all the metrics into one pipeline. this might not seem to be necessary now, but will be required for extended metrics and difficulties for analysis.

## Appendix
1. see ./structural-evolution dir for guidance on antibody mutation and likelihood estimation.
2. see ./diffab dir for diffusion-based sequence+structure codesign/co-optimization.
3. [ABDPO paper](https://openreview.net/pdf?id=zKoIRoDZM5)