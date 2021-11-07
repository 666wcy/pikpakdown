import sys
from sys import exc_info


def get_frame_fallback(n):
    try:
        raise Exception
    except Exception:
        frame = exc_info()[2].tb_frame.f_back
        for _ in range(n):
            frame = frame.f_back
        return frame


if hasattr(sys, "_getframe"):
    get_frame = sys._getframe
else:
    get_frame = get_frame_fallback
