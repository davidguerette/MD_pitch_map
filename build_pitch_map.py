class BuildMDPitchMap():
    def __init__(self, machine, min_note, max_note, md_pitch_seq):
        self.machine = machine
        self.min_note = min_note
        self.max_note = max_note
        self.md_pitch_seq = md_pitch_seq

        self.full_note_range = self.create_full_note_range()
        self.machine_note_range = self.get_machine_note_range()

    def create_full_note_range(self):
        # Create full range note list
        full_note_range = []

        octave_notes = ['C-','C#','D-','D#','E-','F-','F#','G-','G#','A-','A#','B-',]
        octave_range_min = 1
        octave_range_max = 10

        for octave in range(octave_range_min, octave_range_max):
            for note in octave_notes:
                full_note_range.append(note + str(octave))

        return full_note_range

    def get_machine_note_range(self):
        # Create machine-specific note list
        start_note_index = self.full_note_range.index(self.min_note)
        end_note_index = self.full_note_range.index(self.max_note)
        machine_note_range = self.full_note_range[start_note_index:end_note_index + 1]

        return machine_note_range

    def create_machine_pitch_map(self):
        if len(self.machine_note_range) == len(self.md_pitch_seq):
            machine_pitch_map = zip(self.machine_note_range, self.md_pitch_seq)
            return machine_pitch_map
        else:
            print('Error: Cannot create pitch map due to discrepancy between note range and input pitch lists')
            exit()

if __name__ == '__main__':
    # test script with TRX-BD
    trx_bd_pitch_seq = [1,7,12,17,23,28,33,39,44,49,55,60,66,71,76,82,87,92,98,103,108,114,119,124]
    pitch_map_builder = BuildMDPitchMap('TRX-BD', 'B-1', 'A#3', trx_bd_pitch_seq)
    test_map_output = pitch_map_builder.create_machine_pitch_map()
    print(list(test_map_output))
