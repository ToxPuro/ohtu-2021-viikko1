import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def liika_ottaminen_ottaa_kaiken(self):
        self.varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(self.varasto.ota_varastosta(100),10)

    def liika_tayttaminen_ei_tayta_liikaa(self):
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo,self.varasto.tilavuus)

    def negatiivinen_lisays_ei_muuta(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo,5)

    def negatiivinen_otto_ei_muuta(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota(-5)
        self.assertAlmostEqual(self.varasto.saldo,5)

    def negatiivinen_tilavuus_nolla(self):
        varasto=Varasto(-2)
        self.assertAlmostEqual(varasto.tilavuus,0)

    def uudella_varastolla_oikea_saldo(self):
        self.assertAlmostEqual(varasto.saldo,0)

    def saldo_on_oikea(self):
        varasto=Varasto(10,5)
        self.assertAlmostEqual(varasto.saldo,5)
x
    def ei_voi_antaa_negatiivista_saldoa(self):
        varasto=Varasto(10,-1)
        self.assertAlmostEqual(varasto.saldo,0)

    def alku_saldo_ei_ole_enempaa_kuin_tilavuus(self):
        varasto=Varasto(2,3)
        self.assertAlmostEqual(varasto.saldo,2)

    
    


