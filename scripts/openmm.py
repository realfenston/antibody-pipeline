import argparse

import openmm
from openmm import app
from openmm.unit import kilojoules_per_mole


def calculate_energy(system, positions):
    integrator = openmm.VerletIntegrator(1.0 * openmm.unit.femtoseconds)
    platform = openmm.Platform.getPlatformByName('Reference')
    context = openmm.Context(system, integrator, platform)
    context.setPositions(positions)

    state = context.getState(getEnergy=True)
    energy = state.getPotentialEnergy()

    del context, integrator

    return energy


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--complex", required=True, help="")
    parser.add_argument("--antigen", required=True, help="")
    parser.add_argument("--antibody", required=True, help="")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    pdb_complex = app.PDBFile(args.complex)
    pdb_ag = app.PDBFile(args.antigen)
    pdb_ab = app.PDBFile(args.antibody)

    # specify whatever forcefield can be used.
    forcefield = app.ForceField('amber14-all.xml', 'amber14/tip3pfb.xml')

    system_complex = forcefield.createSystem(pdb_complex.topology)
    system_ag = forcefield.createSystem(pdb_ag.topology)
    system_ab = forcefield.createSystem(pdb_ab.topology)

    energy_complex = calculate_energy(system_complex, pdb_complex.positions)
    energy_ag = calculate_energy(system_ag, pdb_ag.positions)
    energy_ab = calculate_energy(system_ab, pdb_ab.positions)

    binding_energy = energy_complex - (energy_ag + energy_ab)

    print("Binding Energy: ", binding_energy)