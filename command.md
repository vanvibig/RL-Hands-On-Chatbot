train crossentropy: python train_crossent.py --data "" --cuda -n crossentropy

train scst: python train_scst.py --data "" --cuda -n scst -l saves\crossentropy\epoch_000_0.091_0.082_loss5.532.dat

use model to chat: python use_model.py -m saves\scstRL\epoch_1620_0.9996738966238987_0.07972247296949114_loss0.010366539160410563.dat

require python==3.6

export env: conda env export | grep -v "^prefix: pytorch" > environment.yml

import env: conda env create -n test -f environment.yml