from services.text_utils import clean_band_name

def test_clean_band_name_removes_whitespace():
    assert clean_band_name("  Queen  ") == "queen"

def test_clean_band_name_normalizes_case():
    assert clean_band_name("DePeChE MoDe") == "depeche mode"
