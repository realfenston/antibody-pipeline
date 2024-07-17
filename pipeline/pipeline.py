import argparse
import yaml

from easydict import EasyDict

from .core import collect_metrics


def get_args():
    parser = argparse.ArgumentParser(description="antibody design-evaluation-ranking pipeline")
    parser.add_argument("--config", default='configs/test.yml', help="path to load yml-like configurations")
    parser.add_argument("--in_pdb", default=None, help="")
    parser.add_argument("--in_mmcif", default=None, help="")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    metrics = {
        'plddt': 'get_plddt',
        'pae': 'get_pae',
        'bind_energy': 'get_energy',
        'nll': 'get_nll', # negative log likelihood
        'abdpo': 'get_abdpp', # unreleased
        'pae_intf': 'get_intf_pea',
        'energy_intf': None,
    }
    
    args = get_args()
    with open(args.config, 'r') as config_f:
        config = EasyDict(yaml.safe_load(config_f))
        
    ouput_tuple = collect_metrics(metrics, args.pdb, args.mmcif)
        
    