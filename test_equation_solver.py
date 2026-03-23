import unittest
from equation_solver import EquationSolver


class TestEquationSolverCE(unittest.TestCase):
    # TC_CE_01: Clasa CE1 - Validarea tipului de date (cel putin un coeficient nu este numar real); vom trata fenomenul defect masking
    def test_tc_ce_01_a_invalid(self):
        solver = EquationSolver("text", 2, 1)
        with self.assertRaises(ValueError):
            solver.solve()

    def test_tc_ce_01_b_invalid(self):
        solver = EquationSolver(1, "text", 1)
        with self.assertRaises(ValueError):
            solver.solve()

    def test_tc_ce_01_c_invalid(self):
        solver = EquationSolver(1, 2, "text")
        with self.assertRaises(ValueError):
            solver.solve()

    # TC_CE_02: Clasa CE2 - Restrictia matematica (a != 0)
    def test_tc_ce_02_a_zero(self):
        solver = EquationSolver(0, 2, 1)
        with self.assertRaises(ValueError):
            solver.solve()

    # TC_CE_03: Clasa CS1 - Delta < 0 (Doua radacini complexe conjugate)
    def test_tc_ce_03_delta_negativ(self):
        solver = EquationSolver(1, 1, 1)
        x1, x2 = solver.solve()

        self.assertIsInstance(x1, complex)
        self.assertIsInstance(x2, complex)

        self.assertAlmostEqual(x1.real, -0.5)
        self.assertAlmostEqual(x2.real, -0.5)

        self.assertAlmostEqual(max(x1.imag, x2.imag), 0.866025, places=5)
        self.assertAlmostEqual(min(x1.imag, x2.imag), -0.866025, places=5)

    # TC_CE_04: Clasa CS2 - Delta = 0 (O radacina reala dubla)
    def test_tc_ce_04_delta_zero(self):
        solver = EquationSolver(1, 2, 1)
        x = solver.solve()

        self.assertIsInstance(x, float)
        self.assertEqual(x, -1.0)

    # TC_CE_05: Clasa CS3 - Delta > 0 (Doua radacini reale distincte)
    def test_tc_ce_05_delta_pozitiv(self):
        solver = EquationSolver(1, 5, 6)
        x1, x2 = solver.solve()

        self.assertIsInstance(x1, float)
        self.assertIsInstance(x2, float)

        self.assertAlmostEqual(max(x1, x2), -2.0, places=5)
        self.assertAlmostEqual(min(x1, x2), -3.0, places=5)

class TestEquationSolverAVF(unittest.TestCase):
    # Testele pentru a=0 si Delta=0 au fost deja implementate in clasa TestEquationSolverCE (test_tc_ce_02 si test_tc_ce_04)

    # TC_AVF_01: Limita stanga pentru coeficientul a (a -> 0-)
    def test_tc_avf_01_a_limita_negativa(self):
        solver = EquationSolver(-0.001, 2, 1)
        x1, x2 = solver.solve()

        self.assertIsInstance(x1, float)
        self.assertIsInstance(x2, float)

        self.assertAlmostEqual(max(x1, x2), 2000.49988, places=3)
        self.assertAlmostEqual(min(x1, x2), -0.49987, places=3)

    # TC_AVF_02: Limita dreapta pentru coeficientul a (a -> 0+)
    def test_tc_avf_02_a_limita_pozitiva(self):
        solver = EquationSolver(0.001, 2, 1)
        x1, x2 = solver.solve()

        self.assertIsInstance(x1, float)
        self.assertIsInstance(x2, float)

        self.assertAlmostEqual(max(x1, x2), -0.50012, places=3)
        self.assertAlmostEqual(min(x1, x2), -1999.49987, places=3)

    # TC_AVF_03: Limita stanga pentru Delta (Delta -> 0-)
    def test_tc_avf_03_delta_limita_negativa(self):
        solver = EquationSolver(1, 1.999, 1)
        x1, x2 = solver.solve()

        self.assertIsInstance(x1, complex)
        self.assertIsInstance(x2, complex)

        self.assertAlmostEqual(x1.real, -0.9995, places=3)
        self.assertAlmostEqual(x2.real, -0.9995, places=3)

        self.assertAlmostEqual(max(x1.imag, x2.imag), 0.03161, places=3)
        self.assertAlmostEqual(min(x1.imag, x2.imag), -0.03161, places=3)

    # TC_AVF_04: Limita dreapta pentru Delta (Delta -> 0+)
    def test_tc_avf_04_delta_limita_pozitiva(self):
        solver = EquationSolver(1, 2.001, 1)
        x1, x2 = solver.solve()

        self.assertIsInstance(x1, float)
        self.assertIsInstance(x2, float)

        self.assertAlmostEqual(max(x1, x2), -0.96887, places=3)
        self.assertAlmostEqual(min(x1, x2), -1.03213, places=1)

class TestEquationSolverPC(unittest.TestCase):
    # TC_PC_01 -> TC_PC_03: Erori de validare a tipului de date pentru coeficientii a, b, c
    def test_tc_pc_01_a_invalid(self):
        solver = EquationSolver(True, 2, 1)
        with self.assertRaises(ValueError):
            solver.solve()

    def test_tc_pc_02_b_invalid(self):
        solver = EquationSolver(1, None, 1)
        with self.assertRaises(ValueError):
            solver.solve()

    def test_tc_pc_03_c_invalid(self):
        solver = EquationSolver(1, 2, [])
        with self.assertRaises(ValueError):
            solver.solve()

    # TC_PC_04: Valoare invalida matematic (a = 0)
    def test_tc_pc_04_a_zero(self):
        solver = EquationSolver(0, 2, 1)
        with self.assertRaises(ValueError):
            solver.solve()

    # TC_PC_05: Limita stanga pentru coeficientul a (a -> 0-)
    def test_tc_pc_05_a_limita_negativa(self):
        solver = EquationSolver(-0.001, 2, 1)
        x1, x2 = solver.solve()

        self.assertIsInstance(x1, float)
        self.assertIsInstance(x2, float)

        self.assertAlmostEqual(max(x1, x2), 2000.49988, places=3)
        self.assertAlmostEqual(min(x1, x2), -0.49987, places=3)

    # TC_PC_06: Limita dreapta pentru coeficientul a (a -> 0+)
    def test_tc_pc_06_a_limita_pozitiva(self):
        solver = EquationSolver(0.001, 2, 1)
        x1, x2 = solver.solve()

        self.assertIsInstance(x1, float)
        self.assertIsInstance(x2, float)

        self.assertAlmostEqual(max(x1, x2), -0.50012, places=3)
        self.assertAlmostEqual(min(x1, x2), -1999.49987, places=3)

    # TC_PC_07: Limita stanga pentru Delta (Delta -> 0-)
    def test_tc_pc_07_delta_limita_negativa(self):
        solver = EquationSolver(1, 1.999, 1)
        x1, x2 = solver.solve()

        self.assertIsInstance(x1, complex)
        self.assertIsInstance(x2, complex)

        self.assertAlmostEqual(x1.real, -0.9995, places=3)
        self.assertAlmostEqual(x2.real, -0.9995, places=3)

        self.assertAlmostEqual(max(x1.imag, x2.imag), 0.03161, places=3)
        self.assertAlmostEqual(min(x1.imag, x2.imag), -0.03161, places=3)

    # TC_PC_08: Delta = 0 (O radacina reala dubla)
    def test_tc_pc_08_delta_zero(self):
        solver = EquationSolver(1, 2, 1)
        x = solver.solve()

        self.assertIsInstance(x, float)
        self.assertEqual(x, -1.0)

    # TC_PC_09: Limita dreapta pentru Delta (Delta -> 0+)
    def test_tc_pc_09_delta_limita_pozitiva(self):
        solver = EquationSolver(1, 2.001, 1)
        x1, x2 = solver.solve()

        self.assertIsInstance(x1, float)
        self.assertIsInstance(x2, float)

        self.assertAlmostEqual(max(x1, x2), -0.96887, places=3)
        self.assertAlmostEqual(min(x1, x2), -1.03213, places=3)

    # TC_PC_10: Delta < 0 (Doua radacini complexe)
    def test_tc_pc_10_delta_negativ(self):
        solver = EquationSolver(1, 1, 1)
        x1, x2 = solver.solve()

        self.assertIsInstance(x1, complex)
        self.assertIsInstance(x2, complex)

        self.assertAlmostEqual(x1.real, -0.5)
        self.assertAlmostEqual(x2.real, -0.5)

        self.assertAlmostEqual(max(x1.imag, x2.imag), 0.866025, places=5)
        self.assertAlmostEqual(min(x1.imag, x2.imag), -0.866025, places=5)

    # TC_PC_11: Delta > 0 (Doua radacini reale distincte)
    def test_tc_pc_11_delta_pozitiv(self):
        solver = EquationSolver(1, 5, 6)
        x1, x2 = solver.solve()

        self.assertIsInstance(x1, float)
        self.assertIsInstance(x2, float)

        self.assertAlmostEqual(max(x1, x2), -2.0, places=5)
        self.assertAlmostEqual(min(x1, x2), -3.0, places=5)