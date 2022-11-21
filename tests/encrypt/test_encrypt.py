import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    first_message = encrypt_message("AABBCC", -1)
    assert first_message == "CCBBAA"

    second_message = encrypt_message("AABBCC", 4)
    assert second_message == "AC_CBBA"

    third_message = encrypt_message("AABBCC", 3)
    assert third_message == "BAA_CCB"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("message", "key")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message([5], 2)
