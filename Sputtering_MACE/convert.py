from ase.io import read, write

traj = read(
    "dump_cpu.lammpstrj",
    index=":",
    format="lammps-dump-text"
)

# Convert LAMMPS atom types to actual elements
for atoms in traj:
    # LAMMPS type 1 = Si, type 2 = Ar
    numbers = []

    for atom in atoms:
        if atom.number == 1:
            numbers.append(14)   # Si
        elif atom.number == 2:
            numbers.append(18)   # Ar

    atoms.set_atomic_numbers(numbers)

# Write full trajectory
write("trajectory.extxyz", traj)


def group_by_element(atoms):
    """Group atoms by atomic number: Si first, then Ar."""
    indices = sorted(
        range(len(atoms)),
        key=lambda i: atoms[i].number
    )
    return atoms[indices]


# First structure
first_atoms = group_by_element(traj[0])

write(
    "first_structure.vasp",
    first_atoms,
    format="vasp",
    direct=False
)


# Last structure
last_atoms = group_by_element(traj[-1])

write(
    "last_structure.vasp",
    last_atoms,
    format="vasp",
    direct=False
)

print(f"Total frames: {len(traj)}")
print("Written:")
print("  first_structure.vasp")
print("  last_structure.vasp")