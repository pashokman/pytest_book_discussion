def test_normal():
    print("\nnormal print")


def test_fail():
    print("\nprint in failing test")
    assert False

def test_disabled(capsys):
    # The output in the with block will always be displayed, even without the -s flag
    with capsys.disabled():
        print("\ncapsys disabled print")