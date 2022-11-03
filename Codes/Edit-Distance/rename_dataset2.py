import os

ori_path = '../../data/npy/dataset1_ori/'
plag_path = '../../data/npy/dataset1_plag/'

diff = 9


for root, dirs, files in os.walk(plag_path):
    for file in files:
        if file.endswith('.npy'):
            print(file)
            if file.startswith('case'):
                continue
            else:
                index = int(file.split('_')[0]) + diff
                new_name = 'case' + str(index) + '_' + file.split('_')[1]
                print(new_name)
                os.rename(os.path.join(root, file), os.path.join(root, new_name))
            # os.rename(os.path.join(root, file), os.path.join(root, file[:-4] + '.npy'))