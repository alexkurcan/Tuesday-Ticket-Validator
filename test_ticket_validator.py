import pytest
from ticket_validator import validate_ticket, get_ticket_tier, calculate_total

# Ticket Vaildator tests
def test_valid_ticket_upper():
    assert valid_ticket_number("ABC1234") == True

def test_invaild_ticket_lower():
    assert valid_ticket_number("abc1234") == False

def test_invalid_ticket_short():
    assert valid_ticket_number("AC12") == False

def test_invaild_ticket_value_error():
    with pytest.raises(ValueError):
        valid_ticket_number(77777)

@pytest.mark.parametrize("ticket, expected", [
    ("AC1234", True),
    ("AA7777", True),
    ("ac1234", False),

])
def test_ticket_format(ticket, expected):
    assert valid_ticket_number(ticket) == expected


# Calculating Ticket Price Tests
def test_regular_price():
    assert calc_ticket_price("General", 30) == 19.00

def test_vip_tickets():
    assert calc_ticket_price("VIP", 30) == 50.00

def test_plat_tickets():
    assert calc_ticket_price("Platnium", 30) == 25.00

def test_invaild_ticket_type():
    with pytest.raises(ValueError):
        calc_ticket_price("Platinum", 25)

def test_age_out_of_range():
    with pytest.raises(ValueError):
        calc_ticket_price("General", 200)

@pytest.mark.parametrize("ticket_type, age, expected", [
    ("General",  30, 19.00),
    ("Platinum", 30, 25.00),
    ("VIP",      30, 50.00),
])
def test_prices(ticket_type, age, expected):
    assert calc_ticket_price(ticket_type, age) == expected

# Ticket is expired :( tests
def test_is_not_expired():
    