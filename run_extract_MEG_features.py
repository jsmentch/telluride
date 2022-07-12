#!/bin/bash
#SBATCH -t 1:00:00
#SBATCH -c 1
#SBATCH --mem=15G
#SBATCH -p normal

conda activate mne
cmd1="cd /om2/user/jsmentch/projects/telluride"
cmd2="python extract_MEG_features.py $1"

#cmd="singularity shell -B /om,/om2,/om4,/nobackup,/nese /om2/user/jsmentch/projects/nat_img/.datalad/environments/analysis/image"


#echo Submitted job for: ${s}
echo $'Command :\n'${cmd1}
${cmd1}

echo $'Command :\n'${cmd2}
${cmd2}
which python
pwd
