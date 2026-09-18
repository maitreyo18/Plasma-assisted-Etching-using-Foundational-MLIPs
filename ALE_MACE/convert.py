from ase.io import read, write

traj = read("dump_cpu.lammpstrj", index=":", format="lammps-dump-text")

for atoms in traj:
    # LAMMPS type 1 = Si, type 2 = Ar, type 3 = Cl
    numbers = []
    for atom in atoms:
        if atom.number == 1:
            numbers.append(14)   # Si
        elif atom.number == 2:
            numbers.append(18)   # Ar
        elif atom.number == 3:
            numbers.append(17)   # Cl

    atoms.set_atomic_numbers(numbers)

write("trajectory.extxyz", traj)
write("last_structure.vasp", traj[-1], format="vasp", direct=False)
