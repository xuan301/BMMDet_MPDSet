import numpy as np
from Classes import *
from Utilities import *
import os
from tqdm import tqdm
plag_data_path = '../../data/npy/dataset_real_plag/'
ori_data_path = '../../data/npy/dataset_real_ori/'
'''
    overlap_rate:   overlap rate of pieces
    piece_len:      length of piece
    k:      weight of duration
    mode:   1 -> direct pitch + consider consonance
            2 -> pitch difference + not consider consonance
    pitch_operation:    1->pitch difference 2->pitch mode 12
    duration_operation: 1->duration ratio   2->duration difference 
    consider_note_distance: True    ->  pitch difference is cost
                            False   ->  cost is 1 if different
    consider_downbeat:      True    ->  consider downbeat of note by weighing the cost more
    consider_force:         True    ->  consider force
    '''
overlap_rate = 0.2
piece_len = 7
k = 0

mode = 2 # 1:(direct pitch) consider consonance, 2:not consider consonance
pitch_operation = 1 # 1:difference, 2:direct
duration_operation = 1 # 1: ratio 2: difference
consider_note_distance = True
consider_downbeat = False
downbeat_weight = 1.2
consider_force = False

def brutal():
    plag_files = os.listdir(plag_data_path)
    plag_file_num = len(plag_files)
    plag_musics = []
    for file in plag_files:
        music = Music(plag_data_path + file)
        music.execute_change(pitch_operation=pitch_operation, duration_operation=duration_operation,
                        piece_len=piece_len, overlap_rate=overlap_rate)
        plag_musics.append(music)
    accuracy = 0
    avg_index = 0

    for i in range(plag_file_num):
        res = {}
        for j in range(plag_file_num):
            if (i == j) or (plag_files[i][6:] == plag_files[j][6:]):
                continue
            '''
            three functions for brutal:
            average_minimum_distance_between_pieces()
            three_minimum_distance_between_pieces()
            minimum_distance_between_pieces()
            '''
            distance = average_minimum_distance_between_pieces(plag_musics[i], plag_musics[j], mode=mode, k=k,
                                    consider_note_distance=consider_note_distance, consider_downbeat=consider_downbeat,
                                    downbeat_weight=downbeat_weight,consider_force=consider_force)
            res[plag_files[j]] = distance
        res = sorted(res.items(), key=lambda d: d[1], reverse=False)
        print('name:\t{}-------------------------------------------------------'.format(plag_files[i]))

        index = 0
        for key, value in res:
            print("{}:\t{}".format(key, value))
            index += 1
            if key[:6] == plag_files[i][:6]:  # ground truth
                print(index)
                avg_index += index
                if (index == 1):
                    accuracy += 1

    print("accuracy:{}\taverage index:{}".format(accuracy / plag_file_num, avg_index / plag_file_num))

def edit_distance_optimized():
    plag_files = os.listdir(plag_data_path)
    ori_files = os.listdir(ori_data_path)
    plag_file_num = len(plag_files)
    ori_file_num = len(ori_files)
    plag_musics = []
    ori_musics = []
    for file in plag_files:
        music = Music(plag_data_path + file)
        music.execute_change(pitch_operation=pitch_operation, duration_operation=duration_operation,
                        piece_len=piece_len, overlap_rate=overlap_rate)
        plag_musics.append(music)

    for file in ori_files:
        music = Music(ori_data_path + file)
        music.execute_change(pitch_operation=pitch_operation, duration_operation=duration_operation,
                        piece_len=piece_len, overlap_rate=overlap_rate)
        ori_musics.append(music)

    accuracy = 0
    avg_index = 0

    for i in range(plag_file_num):
        # if ('case19' not in plag_files[i]):
        #     continue
        res = {}
        # if ("case24" not in plag_files[i]):
        #     continue
        for j in tqdm(range(ori_file_num)):
            # if (plag_files[i][6:] == ori_files[j][6:]):
                # continue
            '''
            three functions for brutal:
            average_minimum_distance_between_pieces()
            three_minimum_distance_between_pieces()
            minimum_distance_between_pieces()
            '''
            distance, _ = max_flow_value(plag_musics[i], ori_musics[j], mode=mode, k=k,
                                    consider_note_distance=consider_note_distance, consider_downbeat=consider_downbeat,
                                    downbeat_weight=downbeat_weight, consider_force=consider_force)
            res[ori_files[j]] = distance
        res = sorted(res.items(), key=lambda d: d[1], reverse=True)
        print('name:\t{}-------------------------------------------------------'.format(plag_files[i]))

        index = 0
        for key, value in res:
            # print("{}:\t{}".format(key, value))
            index += 1
            if key[:6] == plag_files[i][:6]:  # ground truth
                print("Here is the index: ", index)
                # print(key[:6])
                avg_index += index
                if (index == 1):
                    accuracy += 1
    print("overlap_rate={}\tpiece_len={}\tk={}\tmode={}".format(overlap_rate, piece_len, k, mode))
    print("pitch_operation={}\tduration_operation={}\tconsider_note_distance={}".format(pitch_operation, duration_operation, consider_note_distance))
    print("consider_downbeat={}\tdownbeat_weight={}\tconsider_force={}".format(consider_downbeat, downbeat_weight, consider_force))
    print("accuracy:{}\taverage index:{}".format(accuracy / plag_file_num, avg_index / plag_file_num))
    return accuracy / plag_file_num, avg_index / plag_file_num

def main():
    edit_distance_optimized()
main()


