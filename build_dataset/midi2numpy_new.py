import pretty_midi
import os
import numpy as np

# path of MIDI folder
root = os.walk("../data/midi/shuffle/")


'''The class to represent note, including four factors:
    1. the note pitch
    2. the note duration
    3. downbeat
    4. intensity of note sound
'''
class Note:
    def __init__(self):
        self.pitch = 0
        self.length = 0
        self.downbeat = False
        self.force = 0

index = 1
for path, dir_list, file_list in root:
    for file_name in file_list:
        filepath = os.path.join(path, file_name)
        # print(filepath)
        midi_data = pretty_midi.PrettyMIDI(filepath)

        notes = midi_data.instruments[0].notes
        downbeats = midi_data.get_downbeats()
        dataset = []
        for n in notes:
            note = Note()
            for i in downbeats:
                if n.start <= i < n.end:
                    note.downbeat = True
            note.pitch = n.pitch
            note.length = n.end - n.start
            note.force = n.velocity
            dataset.append(note)

        # fix index to 3 digits
        index_str = str(index)
        # print(index_str)
        while len(index_str) < 3:
            index_str = '0' + index_str

        new_name = 'case' + index_str + '_' + file_name.rstrip('.mid')
        print(new_name)
        np.save("../data/npy/dataset_shuffle_plag/{}".format(new_name), dataset)
        index += 1
        

        # np.save("../data/npy/dataset_shuffle_ori/{}".format("case_"index + file_name.rstrip('.mid')), dataset)
