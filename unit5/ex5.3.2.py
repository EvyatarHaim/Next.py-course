class MusicNotes:
    def __init__(self):
        self._base_notes = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
        self._num_of_octaves = 5
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._base_notes) * self._num_of_octaves:
            raise StopIteration

        note_index = self._index % len(self._base_notes)
        octave_index = self._index // len(self._base_notes)
        result = self._base_notes[note_index] * (2 ** octave_index)
        self._index += 1

        return result


notes_iter = iter(MusicNotes())

for freq in notes_iter:
    print(freq)
