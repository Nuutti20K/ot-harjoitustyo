import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_oikein_alussa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataaminen_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(300)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 13.00 euroa")
    
    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(200)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 8.00 euroa")

    def test_ei_muutu_jos_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1200)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_palauttaa_true_jos_onnistuu(self):
        self.assertEqual(self.maksukortti.ota_rahaa(200), True)

    def test_palauttaa_false_jos_epaonnistuu(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1200), False)