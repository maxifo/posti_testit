import postitoimipaikka


def test_postinumerot_ei_ole_tyhja():
    tulos = postitoimipaikka.postinumerot["00100"]
    assert tulos == "HELSINKI"
