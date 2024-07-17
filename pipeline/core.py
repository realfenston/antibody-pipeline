from collections import namedtuple


def collect_pdb():
    pass


def collect_metrics(metrics: dict=None, pdb=None, mmcif=None, fasta=None):
    casual_output = []
    
    for metric, to_use in metrics.items():
        if to_use is not None:
            casual_output.append(None)
        if pdb is not None:
            casual_output.append(eval(metric)(pdb))
        elif mmcif is not None:
            casual_output.append(eval(metric)(mmcif))
        else:
            pdb = collect_pdb(fasta)
            casual_output.append(eval(metric)(pdb))
        
    output_tuple = namedtuple("CasualOutput", casual_output)