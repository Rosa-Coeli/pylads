import os
import sys


temp_dir = './data/temp/'


def fret_symbol():
    return '\n\t\t   ___________\n'


def prepare_fret(fret):
    printed_fret = '  '
    finger_positions = []
    for i in fret:
        if i in [chr(x) for x in range(ord('1'), ord('7'))]:
            finger_positions.append(int(i))
    for i in range(1, 7):
        printed_fret += 'O ' if i in finger_positions else '| '
    printed_fret += fret_symbol()
    return printed_fret


def write_chords(chord_playdict):
    for chord_name, chord in chord_playdict.items():
        chord_path = temp_dir + '.'+ chord_name + '.txt'
        if not os.path.exists(chord_path):
            with open(chord_path, 'a+', encoding='utf-8') as chord_file:
                chord_file.write('\t' + chord_name + '\t' + chord[0][0] + prepare_fret(chord[0][1]))
                for fret in chord[1:-1]:
                    chord_file.write('\t\t ' + prepare_fret(fret[1]))
                chord_file.write('\t\t' + chord[-1][0] + prepare_fret(chord[-1][1]))


def write_missing_chords(missing_chords):
    with open(temp_dir + '.missing_chords.txt', 'a+', encoding='utf-8') as missing_file:
        for chord in missing_chords:
            missing_file.write(chord + '\n')


def read_chords():
    chord_playlist = []  # Loads list of chords to be played from a file.
    with open(temp_dir + '.playlist.txt', 'r', encoding='utf-8') as chords:
        for chord in chords.readlines():
            chord = chord.strip()
            if chord not in chord_playlist:
                chord_playlist.append(chord)
    chord_playdict = {}  # Loads dictionary of all saved chords.
    with open('./data/chords.txt', 'r', encoding='utf-8') as chords:
        for chord in chords.readlines():
            chord = chord.strip()
            chord_name, chord = chord.rsplit(sep=':', maxsplit=1)
            if chord_name in chord_playlist:
                chord_playdict[chord_name] = []
                chord_playlist.remove(chord_name)
                for fret in chord.split(';'):
                    fret_number, fret = fret.split(',', 1)
                    chord_playdict[chord_name].append((fret_number, fret))
    return chord_playdict, chord_playlist


def main():
    chord_playdict, missing_chords = read_chords()
    write_chords(chord_playdict)
    if missing_chords:
        write_missing_chords(missing_chords)
        #print(1, file=sys.stderr)
        print(1)
    else:
        #print(0, file=sys.stderr)
        print(0)


main()


"""
    chords_dict = {}
    with open(chords.txt, 'r', encoding='utf-8') as chords:
        for chord.strip() in chords.readlines():
            chord_name, chord = chord.rsplit(sep=':', maxsplit=1)
            chords_dict[chord_name] = {}
            for fret in chord.split(';'):
                fret_number, fret = fret.split(',', 1)
                chords_dict[chord_name][fret_number] = fret
    """

