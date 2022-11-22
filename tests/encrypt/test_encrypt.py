import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("AABBCC", -1) == "CCBBAA"
    assert encrypt_message("AABBCC", 4) == "AC_CBBA"
    assert encrypt_message("AABBCC", 3) == "BAA_CCB"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("message", "key")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(5, 2)
