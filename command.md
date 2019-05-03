train crossentropy: python train_crossent.py --data "" --cuda -n crossentropy

train scst: python train_scst.py --data "" --cuda -n scst -l saves\crossentropy\epoch_000_0.091_0.082_loss5.532.dat

export env: conda env export | grep -v "^prefix: pytorch" > environment.yml

import env: conda env create -n test -f environment.yml