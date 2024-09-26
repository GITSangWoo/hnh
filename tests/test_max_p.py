from hnh.utils import get_max_score

def test_max_p_label():
    p  = [
        {
            "label": "hot dog",
            "score": 0.9471007585525513
        },
        {
            "label": "not hot dog",
            "score": 0.05289924517273903
        }
    ]

    r = get_max_score(p)
    r1 = max(p,key=lambda x : x['score'])['label'] 
    assert r == "hot dog"
    assert r1 == "hot dog"

