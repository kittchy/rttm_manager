from rttm_manager.service.exporter import RTTMExporter
from rttm_manager.entity.rttm import RTTM


def test_exporter():

    rttm_list = [
        RTTM(
            type="SPEAKER",
            file_id="sample",
            channel_id=1,
            turn_onset=1.00,
            turn_duration=1.00,
            speaker_name="speech",
            orthography_field=None,
            speaker_type=None,
            confidence_score=0.00,
            signal_lookahead_time=0.0,
        ),
        RTTM(
            type="SPEAKER",
            file_id="sample",
            channel_id=1,
            turn_onset=3.50,
            turn_duration=1.50,
            speaker_name="speech",
            orthography_field=None,
            speaker_type=None,
            confidence_score=0.00,
            signal_lookahead_time=0.0,
        ),
        RTTM(
            type="SPEAKER",
            file_id="sample",
            channel_id=1,
            turn_onset=5.00,
            turn_duration=1.00,
            speaker_name="speech",
            orthography_field=None,
            speaker_type=None,
            confidence_score=0.00,
            signal_lookahead_time=0.0,
        ),
        RTTM(
            type="SPEAKER",
            file_id="sample",
            channel_id=1,
            turn_onset=7.50,
            turn_duration=0.50,
            speaker_name="speech",
            orthography_field=None,
            speaker_type=None,
            confidence_score=0.00,
            signal_lookahead_time=0.0,
        ),
        RTTM(
            type="SPEAKER",
            file_id="sample",
            channel_id=1,
            turn_onset=9.00,
            turn_duration=1.00,
            speaker_name="speech",
            orthography_field=None,
            speaker_type=None,
            confidence_score=0.00,
            signal_lookahead_time=0.0,
        ),
    ]

    rttm_file = "tests/example_files/sample2.rttm"
    ret = RTTMExporter.rttm_export(rttm_list, rttm_file)
    assert ret is None

    exptected_lines = [
        "SPEAKER sample 1 1.00 1.00 <NA> <NA> speech 0.00 0.00\n",
        "SPEAKER sample 1 3.50 1.50 <NA> <NA> speech 0.00 0.00\n",
        "SPEAKER sample 1 5.00 1.00 <NA> <NA> speech 0.00 0.00\n",
        "SPEAKER sample 1 7.50 0.50 <NA> <NA> speech 0.00 0.00\n",
        "SPEAKER sample 1 9.00 1.00 <NA> <NA> speech 0.00 0.00\n",
    ]
    with open(rttm_file, "r") as f:
        result_lines = f.readlines()

    for result, line in zip(result_lines, exptected_lines):
        assert result == line
