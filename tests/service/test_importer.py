from rttm_manager.service.importer import RTTMImporter
from rttm_manager.entity.rttm import RTTM


def test_importer():
    rttm_file = "tests/example_files/sample1.rttm"

    rttm_list: list[RTTM] = RTTMImporter.rttm_import(rttm_file)
    exptected = [
        ("SPEAKER", "sample", 1, 1.00, 1.00, None, None, "speech", 0.0, 0.0),
        ("SPEAKER", "sample", 1, 3.50, 1.50, None, None, "speech", 0.0, 0.0),
        ("SPEAKER", "sample", 1, 5.00, 1.00, None, None, "speech", 0.0, 0.0),
        ("SPEAKER", "sample", 1, 7.50, 0.50, None, None, "speech", 0.0, 0.0),
        ("SPEAKER", "sample", 1, 9.00, 1.00, None, None, "speech", 0.0, 0.0),
    ]
    assert isinstance(rttm_list, list)
    for rttm, exp in zip(rttm_list, exptected):
        assert isinstance(rttm, RTTM)
        assert rttm.type == exp[0]
        assert rttm.file_id == exp[1]
        assert rttm.channel_id == exp[2]
        assert rttm.turn_onset == exp[3]
        assert rttm.turn_duration == exp[4]
        assert rttm.orthography_field == exp[5]
        assert rttm.speaker_type == exp[6]
        assert rttm.speaker_name == exp[7]
        assert rttm.confidence_score == exp[8]
        assert rttm.signal_lookahead_time == exp[9]
