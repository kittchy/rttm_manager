# RTTM Exporter and Importer

## Example

1. Emport RTTM

```python
from rttm_manager import import_rttm

file_name = "example.rttm"

rttm_list = import_rttm(file_name)
```

2. Export RTTM

```python
from rttm_manager import RTTM
from rttm_manager import export_rttm

rttms = [
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
    )
]*3

file_name = "example.rttm"

export_rttm(rttms, file_name)
"""
SPEAKER sample 1 9.00 1.00 <NA> <NA> speech 0.00 0.00
SPEAKER sample 1 9.00 1.00 <NA> <NA> speech 0.00 0.00
SPEAKER sample 1 9.00 1.00 <NA> <NA> speech 0.00 0.00
"""

```

## Installation

```bash
pip install rttm_manager
```
