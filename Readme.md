# Music Plagiarism Detection: A Bipartite Graph Matching based Approach and a Simulated Large-Scale Dataset

## Introduction
For detecting fine-grained music plagiarism across datasets, we propose a novel bipartite graph based method, ```BMM-Det```, which is robust to transposition, duration variance, pitch shifts, and melody change. We devise a simulated large-scale dataset, ```MPD-Set```, by adding different ways of plagiarism and using a generation model. A real-life dataset with many legally-confirmed music plagiarism cases is also collected. Experimental results prove BMM-Det's competitive performance on detecting fine-grained plagiarism.

## Environment:
>```python
>numpy==1.19.4
>os
>tqdm
>```
## Datasets: Real Dataset

There are two datasets which are introduced in our paper. `data/npy/dataset_real_*` contains 29 pairs of real-life examples which constitute plagiarism. 

## Datasets: MPD-Set
Music Plagiarism Detection Dataset (MPD-Set) is the first (to our best knowledge) publicly available large-scale dataset (2,000 pieces) for the music plagiarism task and can be used by researchers for model design, result validation, etc. It contains a large number of fine-grained plagiarism pairs that more closely resemble real-life plagiarism situations. The original song data for MPD-Set is selected from [Wikifonia](https://www.wikifonia.org), an open-sourced dataset with songs collected from samples of real-life songs composed by humans. We obtain song fragments from it in MusicXML format, convert them into the MIDI format commonly used in academia, and further construct MPD-Set.
    
MPD-Set contains a total of 2,000 pieces of music, which two by two constitute a copying relationship. We design four types of plagiarism for the dataset, taking into account the specific situations of plagiarism in reality: transposition, pitch shifts, duration variance, and melody change, where each accounts for a quarter of the dataset. The specific implications of these four situations are as follows:

```Transposition```: structural transposition of original song.

```Pitch Shifts```: pitch shifts of a fragment of the original song and the addition of it to a completely unrelated song.

```Duration Variance```: a similar operation to pitch shifts, but with a duration variance to the original piece.

```Melody Change```: melody change of a fragment of the original song, yet through [MuseMorphose](https://github.com/YatingMusic/MuseMorphose), a Transformer-based VAE model, and the addition of this fragment to a completely unrelated song.
### Structure
The structure of the MPD-Set is as follows:
```
midi
├───MPD-Set_ori
├───MPD-Set_plag
├───shuffle.xlsx
├───pitch.xlsx
├───duration.xlsx
├───melody.xlsx
npy
├───MPD-Set_ori
├───MPD-Set_plag
```
### MIDI
Due to the different methods of plagiarism in different situations, we introduce the specific  methods of various simulated plagiarized content.
#### Transposition
For the original midi in MPD-Set_ori/shuffle, we randomly divide it into different parts and combine them into new pieces out of order. In ```shuffle.xlsx```, we record the original start time (OST) and original end time (OET) of each part respectively.
#### Pitch Shifts
Pitch shifts means the pitch of a fragment of the original song is shifted and then added to a completely unrelated song. In ```pitch.xlsx```, we record the plagiarized song name (Name) and original song name (OriFile), the pitch shifted part in the plagiarized song (Start Time, End Time) and the original piece in the original song (Original Start Time, Original End Time).
#### Duration Variance
Duration variance means the duration of a fragment of the original song is changed and then added to a completely unrelated song. In ```duration.xlsx```, we record the plagiarized song name (Name) and original song name (OriFile), the duration variance part in the plagiarized song (Start Time, End Time) and the original piece in the original song (Original Start Time, Original End Time).
#### Melody Change
Melody change means the melody of a fragment of the original song is changed and then added to a completely unrelated song. In ```melody.xlsx```, we record the plagiarized song name (Name) and original song name (OriFile), the melody change part in the plagiarized song (Start Time, End Time) and the original piece in the original song (Original Start Time, Original End Time).

### NPY
We convert the MIDI files into NPY files, which can be used for training models. The NPY files are stored in ```npy/MPD-Set_ori``` and ```npy/MPD-Set_plag```. The NPY files are named according to the original MIDI file names. For files in MPD-Set_ori and MPD-Set_plag, if they are started with the same case number, they constitute a plagiarism pair. For example, ```npy/MPD-Set_ori/Case0001_xxxx.npy``` and ```npy/MPD-Set_plag/Case0001_xxxx.npy``` are a plagiarism pair.


## Check the results on real-life dataset

You can check the results on real-life dataset by running the following command:

```
cd Codes/Edit-Distance
python run_dataset_real.py
```

## Check the results on MPD-Set

To check the results on MPD-Set, you should first download [MPD-Set](https://drive.google.com/drive/folders/16N5hXe368vBjuHzeyW_qzptY5LBVQo5_?usp=sharing) and organize the files to the existed data folder as follows:

```
data
├───midi
│   ├───dataset_real_ori
│   ├───dataset_rea_plag
│   ├───MPD-Set_ori
│   ├───MPD-Set_plag
│   ├───shuffle.xlsx
│   ├───pitch.xlsx
│   ├───duration.xlsx
│   ├───melody.xlsx
├───npy
│   ├───dataset_real_ori
│   ├───dataset_rea_plag
│   ├───MPD-Set_ori
│   ├───MPD-Set_plag
```

Then you can run the following command to check the results on MPD-Set:

```
cd Codes/Edit-Distance
python run_dataset_MPDSet.py
```

The results will be saved in ```Codes/Edit-Distance/result_MPDSet.txt```





