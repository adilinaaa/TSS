import math
import unittest


class EquationSolver:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        if not all(
            isinstance(x, (int, float)) and not isinstance(x, bool)
            for x in [self.a, self.b, self.c]
        ):
            raise ValueError("Coeficientii ecuatiei trebuie sa fie numere reale!")

        if self.a == 0:
            raise ValueError("Coeficientul a nu poate fi 0!")

        delta = self.b ** 2 - 4 * self.a * self.c

        if math.isclose(delta, 0.0, abs_tol=1e-9):
            return -self.b / (2 * self.a)

        elif delta < 0:
            real_part = -self.b / (2 * self.a)
            imag_part = math.sqrt(abs(delta)) / (2 * self.a)
            x1 = complex(real_part, imag_part)
            x2 = complex(real_part, -imag_part)
            return x1, x2

        else:
            x1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            return x1, x2


class EquationSolver_Mutant_AOR:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        if not all(
            isinstance(x, (int, float)) and not isinstance(x, bool)
            for x in [self.a, self.b, self.c]
        ):
            raise ValueError("Coeficientii ecuatiei trebuie sa fie numere reale!")

        if self.a == 0:
            raise ValueError("Coeficientul a nu poate fi 0!")

        # Mutant AOR: b**2 - 4*a*c devine b**2 + 4*a*c
        delta = self.b ** 2 + 4 * self.a * self.c

        if math.isclose(delta, 0.0, abs_tol=1e-9):
            return -self.b / (2 * self.a)

        elif delta < 0:
            real_part = -self.b / (2 * self.a)
            imag_part = math.sqrt(abs(delta)) / (2 * self.a)
            x1 = complex(real_part, imag_part)
            x2 = complex(real_part, -imag_part)
            return x1, x2

        else:
            x1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            return x1, x2


class EquationSolver_Mutant_ROR:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        if not all(
            isinstance(x, (int, float)) and not isinstance(x, bool)
            for x in [self.a, self.b, self.c]
        ):
            raise ValueError("Coeficientii ecuatiei trebuie sa fie numere reale!")

        if self.a == 0:
            raise ValueError("Coeficientul a nu poate fi 0!")

        delta = self.b ** 2 - 4 * self.a * self.c

        if math.isclose(delta, 0.0, abs_tol=1e-9):
            return -self.b / (2 * self.a)

        # Mutant ROR: delta < 0 devine delta > 0
        elif delta > 0:
            real_part = -self.b / (2 * self.a)
            imag_part = math.sqrt(abs(delta)) / (2 * self.a)
            x1 = complex(real_part, imag_part)
            x2 = complex(real_part, -imag_part)
            return x1, x2

        else:
            x1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            return x1, x2


class EquationSolver_Mutant_LCR:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        # Mutant LCR: all(...) devine any(...)
        if not any(
            isinstance(x, (int, float)) and not isinstance(x, bool)
            for x in [self.a, self.b, self.c]
        ):
            raise ValueError("Coeficientii ecuatiei trebuie sa fie numere reale!")

        if self.a == 0:
            raise ValueError("Coeficientul a nu poate fi 0!")

        delta = self.b ** 2 - 4 * self.a * self.c

        if math.isclose(delta, 0.0, abs_tol=1e-9):
            return -self.b / (2 * self.a)

        elif delta < 0:
            real_part = -self.b / (2 * self.a)
            imag_part = math.sqrt(abs(delta)) / (2 * self.a)
            x1 = complex(real_part, imag_part)
            x2 = complex(real_part, -imag_part)
            return x1, x2

        else:
            x1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            return x1, x2


class EquationSolver_Mutant_STD1:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        if not all(
            isinstance(x, (int, float)) and not isinstance(x, bool)
            for x in [self.a, self.b, self.c]
        ):
            raise ValueError("Coeficientii ecuatiei trebuie sa fie numere reale!")

        if self.a == 0:
            raise ValueError("Coeficientul a nu poate fi 0!")

        delta = self.b ** 2 - 4 * self.a * self.c

        if math.isclose(delta, 0.0, abs_tol=1e-9):
            return -self.b / (2 * self.a)

        elif delta < 0:
            real_part = -self.b / (2 * self.a)
            imag_part = math.sqrt(abs(delta)) / (2 * self.a)
            x1 = complex(real_part, imag_part)
            x2 = complex(real_part, -imag_part)

            # Mutant STD-1: returnarea corecta este inlocuita cu None
            return None

        else:
            x1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            return x1, x2


class EquationSolver_Mutant_STD2:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        if not all(
            isinstance(x, (int, float)) and not isinstance(x, bool)
            for x in [self.a, self.b, self.c]
        ):
            raise ValueError("Coeficientii ecuatiei trebuie sa fie numere reale!")

        if self.a == 0:
            raise ValueError("Coeficientul a nu poate fi 0!")

        delta = self.b ** 2 - 4 * self.a * self.c

        if math.isclose(delta, 0.0, abs_tol=1e-9):
            # Mutant STD-2: -b / (2*a) devine -b / a
            return -self.b / self.a

        elif delta < 0:
            real_part = -self.b / (2 * self.a)
            imag_part = math.sqrt(abs(delta)) / (2 * self.a)
            x1 = complex(real_part, imag_part)
            x2 = complex(real_part, -imag_part)
            return x1, x2

        else:
            x1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            return x1, x2


class TestEquationSolverMutationAdequacy(unittest.TestCase):

    def test_invalid_types(self):
        with self.assertRaises(ValueError):
            EquationSolver("text", 2, 1).solve()

        with self.assertRaises(ValueError):
            EquationSolver(1, "text", 1).solve()

        with self.assertRaises(ValueError):
            EquationSolver(1, 2, "text").solve()

        with self.assertRaises(ValueError):
            EquationSolver(True, 2, 1).solve()

    def test_a_zero(self):
        with self.assertRaises(ValueError):
            EquationSolver(0, 2, 1).solve()

    def test_delta_negative(self):
        result = EquationSolver(1, 1, 1).solve()

        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], complex)
        self.assertIsInstance(result[1], complex)

        self.assertAlmostEqual(result[0].real, -0.5)
        self.assertAlmostEqual(result[1].real, -0.5)

    def test_delta_zero(self):
        result = EquationSolver(1, 2, 1).solve()

        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, -1.0)

    def test_delta_positive(self):
        result = EquationSolver(1, 5, 6).solve()

        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)

        self.assertAlmostEqual(result[0], -2.0)
        self.assertAlmostEqual(result[1], -3.0)

    def test_mutant_aor_is_killed(self):
        original = EquationSolver(1, 5, 6).solve()
        mutant = EquationSolver_Mutant_AOR(1, 5, 6).solve()

        self.assertNotEqual(original, mutant)

    def test_mutant_ror_is_killed(self):
        original = EquationSolver(1, 5, 6).solve()
        mutant = EquationSolver_Mutant_ROR(1, 5, 6).solve()

        self.assertNotEqual(original, mutant)

    def test_mutant_lcr_is_killed(self):
        with self.assertRaises(Exception):
            EquationSolver_Mutant_LCR("text", 2, 1).solve()

    def test_mutant_std1_is_killed(self):
        original = EquationSolver(1, 1, 1).solve()
        mutant = EquationSolver_Mutant_STD1(1, 1, 1).solve()

        self.assertNotEqual(original, mutant)

    def test_mutant_std2_is_killed(self):
        original = EquationSolver(1, 2, 1).solve()
        mutant = EquationSolver_Mutant_STD2(1, 2, 1).solve()

        self.assertNotEqual(original, mutant)


if __name__ == "__main__":
    unittest.main(verbosity=2)
