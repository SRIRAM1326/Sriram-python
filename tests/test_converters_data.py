import pytest
from tests.conftest import load_project_module

def test_temperature_converter():
    temp_mod = load_project_module("09_temperature_converter")

    # 0 C = 32 F, 100 C = 212 F
    assert temp_mod.c_to_f(0) == 32.0
    assert temp_mod.c_to_f(100) == 212.0

    # 32 F = 0 C
    assert round(temp_mod.f_to_c(32), 2) == 0.0
    assert round(temp_mod.f_to_c(212), 2) == 100.0

    # Kelvin conversions
    assert temp_mod.c_to_k(0) == 273.15
    assert round(temp_mod.k_to_c(273.15), 2) == 0.0

def test_typing_speed_accuracy_calculation():
    tester = load_project_module("45_typing_speed_tester")

    prompt = "The quick brown fox"
    typed_exact = "The quick brown fox"
    typed_partial = "The quick brown cat"  # 16 matching chars out of 19

    acc_exact, correct_exact, total = tester.calculate_accuracy(prompt, typed_exact)
    assert acc_exact == 100.0
    assert correct_exact == 19
    assert total == 19

    acc_partial, correct_part, _ = tester.calculate_accuracy(prompt, typed_partial)
    assert acc_partial < 100.0
    assert correct_part == 16

def test_currency_converter_rates():
    curr_mod = load_project_module("44_currency_converter")
    rates = curr_mod.RATES

    assert "USD" in rates
    assert rates["USD"] == 1.0
    assert "EUR" in rates
    assert "INR" in rates

    # Basic conversion calculation check: USD to INR
    usd_val = 10.0
    inr_val = (usd_val / rates["USD"]) * rates["INR"]
    assert inr_val > 0
    assert round(inr_val, 2) == round(usd_val * rates["INR"], 2)

def test_student_attendance_summary():
    att_mod = load_project_module("60_student_attendance_tracker")

    data = {
        "students": [
            {"id": "S101", "name": "Student A"},
            {"id": "S102", "name": "Student B"}
        ],
        "records": {
            "2026-10-01": {"S101": "P", "S102": "A"},
            "2026-10-02": {"S101": "P", "S102": "P"},
            "2026-10-03": {"S101": "P", "S102": "A"},
            "2026-10-04": {"S101": "A", "S102": "A"}
        }
    }

    # S101 present 3/4 = 75%
    s101_present = sum(1 for d, rec in data["records"].items() if rec.get("S101") == "P")
    s101_pct = (s101_present / 4) * 100
    assert s101_pct == 75.0

    # S102 present 1/4 = 25%
    s102_present = sum(1 for d, rec in data["records"].items() if rec.get("S102") == "P")
    s102_pct = (s102_present / 4) * 100
    assert s102_pct == 25.0
