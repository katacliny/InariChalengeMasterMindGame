from game import validate_color_sequence, validate_command, validate_help, get_pegs

secret = "RBYG"


def test_color_sequence_validator():
    
    assert validate_color_sequence("RBYG")
    
def test_validator_command():
     
     assert validate_command("--exit")
     
def test_validate_help():
    
    assert validate_help("--help")
    
def test_get_pegs():
    
    assert get_pegs("RBYG", secret) == "You win !"