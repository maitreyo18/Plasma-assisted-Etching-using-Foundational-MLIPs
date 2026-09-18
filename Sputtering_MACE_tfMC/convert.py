from ase.io import read, write

traj = read("dump_cpu.lammpstrj", index=":", format="lammps-dump-text")

for atoms in traj:
    # LAMMPS type 1 = Si, type 2 = Ar
    numbers = []

    for atom in atoms:
        if atom.number == 1:
            numbers.append(14)   # Si
        elif atom.number == 2:
            numbers.append(18)   # Ar

    atoms.set_atomic_numbers(numbers)

write("trajectory.extxyz", traj)

# Final structure
final_atoms = traj[-1]

# Group atoms by element: Si first, then Ar
indices = sorted(
    range(len(final_atoms)),
    key=lambda i: final_atoms[i].number
)

final_atoms = final_atoms[indices]

write(
    "last_structure.vasp",
    final_atoms,
    format="vasp",
    direct=False
)