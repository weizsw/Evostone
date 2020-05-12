#!/bin/sh
#
#SBATCH --verbose
#SBATCH --job-name=lunarLander
#SBATCH --output=slurm_%j.out
#SBATCH --error=slurm_%j.err
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --mem=1GB

/bin/hostname
/bin/pwd

module load python3/intel/3.6.3
module load dotnet/2.2.300


donet bin.DeckSearch.dll condig/paladin.tml