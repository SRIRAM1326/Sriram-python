import pytest
from tests.conftest import load_project_module

def test_email_validator():
    email_mod = load_project_module("41_email_validator")

    # Valid formats
    valid, msg = email_mod.validate_email("developer@domain.com")
    assert valid is True

    valid, msg = email_mod.validate_email("user.name+tag@sub.example.org")
    assert valid is True

    # Invalid cases
    valid, msg = email_mod.validate_email("invalid_email")
    assert valid is False

    valid, msg = email_mod.validate_email("user@")
    assert valid is False

    valid, msg = email_mod.validate_email("@domain.com")
    assert valid is False

    valid, msg = email_mod.validate_email("user with spaces@domain.com")
    assert valid is False

    # Typo detection suggestion
    valid, msg = email_mod.validate_email("sriram@gmai.com")
    assert valid is True
    assert "gmail.com" in msg

def test_strong_password_checker():
    pw_mod = load_project_module("46_strong_password_checker")

    # Very strong password
    res = pw_mod.evaluate_password("C0mpl3x#P@ssw0rd!2026")
    assert "STRONG" in res["strength"]
    assert res["has_upper"] is True
    assert res["has_lower"] is True
    assert res["has_digit"] is True
    assert res["has_symbol"] is True
    assert res["entropy"] > 60

    # Weak password
    res_weak = pw_mod.evaluate_password("123456")
    assert "WEAK" in res_weak["strength"]

    # Insecure pattern flag
    res_pattern = pw_mod.evaluate_password("password")
    assert any("insecure pattern" in issue.lower() for issue in res_pattern["issues"])

def test_url_shortener_code_generation():
    shortener = load_project_module("43_url_shortener")
    code1 = shortener.generate_short_code(6)
    code2 = shortener.generate_short_code(6)
    assert len(code1) == 6
    assert len(code2) == 6
    assert code1.isalnum()
    assert code1 != code2  # Highly improbable to collide

def test_password_protected_notes_crypto():
    notes_mod = load_project_module("58_password_protected_notes")
    sample_data = {"notes": [{"id": 1, "title": "Secret Key", "content": "123456"}]}
    password = "CorrectHorseBatteryStaple123"

    # Encrypt
    encrypted_blob = notes_mod.encrypt_payload(sample_data, password)
    assert isinstance(encrypted_blob, bytes)
    assert b"Secret Key" not in encrypted_blob  # Plaintext must not leak

    # Decrypt with correct password
    decrypted = notes_mod.decrypt_payload(encrypted_blob, password)
    assert decrypted["notes"][0]["title"] == "Secret Key"
    assert decrypted["notes"][0]["content"] == "123456"

    # Decrypt with wrong password must fail
    with pytest.raises(Exception):
        notes_mod.decrypt_payload(encrypted_blob, "WrongPassword!")
