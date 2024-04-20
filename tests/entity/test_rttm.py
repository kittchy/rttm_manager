from rttm.entity.rttm import RTTM


def test_rttm_object():
    """
    test making RTTM object
    """
    rttm = RTTM(
        type="SPEAKER",
        file_id="hogehoge",
        channel_id=1,
        turn_onset=0.0,
        turn_duration=1.0,
        orthography_field="<NA>",
        speaker_type="<NA>",
        speaker_name="hogehoge",
        confidence_score="<NA>",
        signal_lookahead_time="<NA>",
    )
    assert rttm
    assert rttm.type == "SPEAKER"
    assert rttm.file_id == "hogehoge"
    assert rttm.channel_id == 1
    assert rttm.turn_onset == 0.0
    assert rttm.turn_duration == 1.0
    assert rttm.orthography_field == "<NA>"
    assert rttm.speaker_type == "<NA>"
    assert rttm.speaker_name == "hogehoge"
    assert rttm.confidence_score == "<NA>"
    assert rttm.signal_lookahead_time == "<NA>"
