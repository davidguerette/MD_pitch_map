'''
Module for building Machinedrum pitch map JSON
Handles the lifting of matching up pitch values (per machine) with corresponding notes
'''

class BuildMDPitchMapError(Exception):
    ''' raise custom exceptions for BuildMDPitchMap '''
    pass

class BuildMDPitchMap():
    ''' MD Pitch Map Builder class '''
    def __init__(self):
        self.note_range_list = self.full_note_range()

    def full_note_range(self):
        ''' Create full range note list - used as reference for each individual machine range '''
        octave_notes = ['C-', 'C#', 'D-', 'D#', 'E-', 'F-', 'F#', 'G-', 'G#', 'A-', 'A#', 'B-']
        octave_range_min = 1
        octave_range_max = 10

        full_note_range = []
        for octave in range(octave_range_min, octave_range_max):
            for note in octave_notes:
                full_note_range.append(note + str(octave))

        return full_note_range

    def machine_note_range(self, min_note, max_note):
        ''' Create machine-specific note list '''
        start_note_index = self.note_range_list.index(min_note)
        end_note_index = self.note_range_list.index(max_note)
        machine_note_range = self.note_range_list[start_note_index:end_note_index + 1]
        return machine_note_range

    def build_machine_pitch_map(self, input_data):
        return_dict = {}

        for machine in input_data:
            # input_data list format: [machine_group, machine, min_note, max_note, pitch_seq]
            machine_group = machine[0]
            machine_name = machine[1]
            min_note = machine[2]
            max_note = machine[3]
            pitch_seq = machine[4]

            # Find machine-specific range against full range of the MD
            machine_note_range = self.machine_note_range(min_note, max_note)

            if len(machine_note_range) == len(pitch_seq):
                machine_pitch_map = zip(machine_note_range, pitch_seq)

                if not machine_group in return_dict:
                    return_dict[machine_group] = {}

                if not machine_name in return_dict[machine_group]:
                    return_dict[machine_group][machine_name] = list(machine_pitch_map)
            else:
                raise BuildMDPitchMapError("Cannot create {0} pitch map due to length discrepancy"\
                    " between note range and input pitch lists".format(machine_name))

        return return_dict

if __name__ == '__main__':
    # pitch map data source: http://www.elektronauts.com/topics/view/8643/69758/page:1#69758
    builder_data = [
        ('TRX', 'BD', 'B-1', 'A#3', [1, 7, 12, 17, 23, 28, 33, 39, 44, 49, 55, 60, 66, 71, 76, 82,
                                     87, 92, 98, 103, 108, 114, 119, 124]),
        ('TRX', 'SD', 'F-4', 'G-5', [3, 13, 24, 35, 45, 56, 67, 77, 88, 98, 109, 120, 121, 123, 126]),
        ('TRX', 'XT', 'D-3', 'C#5', [2, 7, 12, 18, 23, 28, 34, 39, 44, 49, 55, 60, 65, 71, 76, 81,
                                     87, 92, 97, 103, 108, 113, 118, 124]),
        ('TRX', 'XC', 'F-3', 'E-5', [1, 6, 11, 17, 22, 27, 33, 38, 43, 49, 54, 60, 65, 70, 76, 81,
                                     86, 92, 97, 102, 108, 113, 118, 124]),
        ('EFM', 'BD', 'G#1', 'E-5', [1, 3, 6, 9, 11, 14, 17, 19, 22, 25, 27, 30, 33, 35, 38, 41,
                                     43, 46, 49, 51, 54, 57, 59, 62, 65, 67, 70, 73, 75, 78, 81,
                                     83, 86, 89, 91, 94, 97, 99, 102, 105, 107, 110, 113, 115, 118]),
    ]

    # build pitch map
    builder = BuildMDPitchMap()
    builder.build_machine_pitch_map(builder_data)

