import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.rikas = Maksukortti(1000)
        self.koyha = Maksukortti(100)

    def test_rahat_oikein_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lounaat_oikein_alussa(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_edullinen_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_edullinen_rahat_tulee_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullinen_lounaat_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_rahat_ei_riita_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(210), 210)

    def test_edullinen_rahat_ei_riita_kassa(self):
        self.kassapaate.syo_edullisesti_kateisella(210)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_rahat_ei_riita_lounaat(self):
        self.kassapaate.syo_edullisesti_kateisella(210)
        self.assertEqual(self.kassapaate.edulliset, 0)


    def test_maukas_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_maukas_rahat_tulee_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukas_lounaat_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_rahat_ei_riita_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(210), 210)

    def test_maukas_rahat_ei_riita_kassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(210)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_rahat_ei_riita_lounaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(210)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    
    def test_kortilla_edullinen_osto_onnistuu(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.rikas), True)

    def test_kortilla_edullinen_kortin_rahat(self):
        self.kassapaate.syo_edullisesti_kortilla(self.rikas)
        self.assertEqual(str(self.rikas), "Kortilla on rahaa 7.60 euroa")

    def test_kortilla_edullinen_lounaat_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.rikas)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortilla_edullinen_osto_epaonnistuu(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.koyha), False)

    def test_kortilla_edullinen_rahat_ei_riita_kortin_rahat(self):
        self.kassapaate.syo_edullisesti_kortilla(self.koyha)
        self.assertEqual(str(self.koyha), "Kortilla on rahaa 1.00 euroa")

    def test_kortilla_edullinen_lounaat_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kortilla(self.koyha)
        self.assertEqual(self.kassapaate.edulliset, 0)

    
    def test_kortilla_maukas_osto_onnistuu(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.rikas), True)

    def test_kortilla_maukas_kortin_rahat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.rikas)
        self.assertEqual(str(self.rikas), "Kortilla on rahaa 6.00 euroa")

    def test_kortilla_maukas_lounaat_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.rikas)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortilla_maukas_osto_epaonnistuu(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.koyha), False)

    def test_kortilla_maukas_rahat_ei_riita_kortin_rahat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.koyha)
        self.assertEqual(str(self.koyha), "Kortilla on rahaa 1.00 euroa")

    def test_kortilla_maukas_lounaat_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.koyha)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    
    def test_rahan_lataus_kortilla_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.koyha, 300)
        self.assertEqual(str(self.koyha), "Kortilla on rahaa 4.00 euroa")

    def test_rahan_lataus_kassassa_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.koyha, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100300)

    def test_rahan_lataus_negatiivinen_kortilla_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.koyha, -20)
        self.assertEqual(str(self.koyha), "Kortilla on rahaa 1.00 euroa")

    def test_rahan_lataus_negatiivinen_kassassa_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.koyha, -20)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)