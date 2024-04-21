from rttm_manager.entity.rttm import RTTM


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
        speaker_name="hogehoge",
        orthography_field=None,
        speaker_type=None,
        confidence_score=None,
        signal_lookahead_time=None,
    )
    assert rttm
    assert rttm.type == "SPEAKER"
    assert rttm.file_id == "hogehoge"
    assert rttm.channel_id == 1
    assert rttm.turn_onset == 0.0
    assert rttm.turn_duration == 1.0
    assert rttm.orthography_field is None
    assert rttm.speaker_type is None
    assert rttm.speaker_name == "hogehoge"
    assert rttm.confidence_score is None
    assert rttm.signal_lookahead_time is None
