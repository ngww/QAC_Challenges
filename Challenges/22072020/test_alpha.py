import pytest
from alpha_words import alpha

def test_alpha():
    return alpha("the sandwich pants in the complaining profile") == "complaining in pants profile sandwich the"
    return alpha("withdrawing champagne cautions with the upsetting sail") == "cautions champagne sail the upsetting with withdrawing"
    return alpha("beside the betting trigger leaks her consecutive temple") == "beside betting consecutive her leaks temple the trigger"
    return alpha("when can the unobtainable neighbor belong to the partial disaster") == "belong can disaster neighbor partial the to unobtainable when"
    return alpha("over the wisdom gasps the complete mummy") == "complete gasps mummy over the wisdom"