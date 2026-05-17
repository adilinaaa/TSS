import math
import unittest
import io
from contextlib import redirect_stdout


class EquationSolver:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        if not all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in [self.a, self.b, self.c]):
            raise ValueError("Coeficienții ecuației trebuie să fie numere reale!")

        if self.a == 0:
            raise ValueError("Coeficientul „a” nu poate fi 0!")

        delta = self.b ** 2 - 4 * self.a * self.c

        if delta < 0:
            real_part = -self.b / (2 * self.a)
            imag_part = math.sqrt(abs(delta)) / (2 * self.a)
            x1 = complex(real_part, imag_part)
            x2 = complex(real_part, -imag_part)
            return x1, x2

        elif math.isclose(delta, 0.0, abs_tol=1e-9):
            return -self.b / (2 * self.a)

        else:
            x1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            return x1, x2


class TestEquationSolver(unittest.TestCase):

    # Helper pentru compararea numerelor complexe
    def assertComplexAlmostEqual(self, actual, expected, places=7):
        self.assertAlmostEqual(actual.real, expected.real, places=places)
        self.assertAlmostEqual(actual.imag, expected.imag, places=places)

    # 1. Statement coverage
    def test_statement_coverage_delta_positive(self):
        solver = EquationSolver(1, -5, 6)
        result = solver.solve()

        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0], 3.0)
        self.assertAlmostEqual(result[1], 2.0)

    def test_statement_coverage_delta_negative(self):
        solver = EquationSolver(1, 2, 5)
        x1, x2 = solver.solve()

        self.assertComplexAlmostEqual(x1, complex(-1.0, 2.0))
        self.assertComplexAlmostEqual(x2, complex(-1.0, -2.0))

    def test_statement_coverage_delta_zero(self):
        solver = EquationSolver(1, 2, 1)
        result = solver.solve()

        self.assertAlmostEqual(result, -1.0)

    # 2. Branch coverage
    def test_branch_coverage_invalid_coefficient(self):
        with self.assertRaises(ValueError) as context:
            EquationSolver("1", 2, 1).solve()

        self.assertEqual(
            str(context.exception),
            "Coeficienții ecuației trebuie să fie numere reale!"
        )

    def test_branch_coverage_a_zero(self):
        with self.assertRaises(ValueError) as context:
            EquationSolver(0, 2, 1).solve()

        self.assertEqual(
            str(context.exception),
            "Coeficientul „a” nu poate fi 0!"
        )

    def test_branch_coverage_all_delta_cases(self):
        negative_delta = EquationSolver(1, 0, 1).solve()
        zero_delta = EquationSolver(1, 2, 1).solve()
        positive_delta = EquationSolver(1, -3, 2).solve()

        self.assertIsInstance(negative_delta[0], complex)
        self.assertAlmostEqual(zero_delta, -1.0)
        self.assertAlmostEqual(positive_delta[0], 2.0)
        self.assertAlmostEqual(positive_delta[1], 1.0)

    # 3. Condition coverage
    def test_condition_coverage_invalid_a(self):
        with self.assertRaises(ValueError):
            EquationSolver("invalid", 2, 1).solve()

    def test_condition_coverage_invalid_b(self):
        with self.assertRaises(ValueError):
            EquationSolver(1, "invalid", 1).solve()

    def test_condition_coverage_invalid_c(self):
        with self.assertRaises(ValueError):
            EquationSolver(1, 2, "invalid").solve()

    def test_condition_coverage_bool_a(self):
        with self.assertRaises(ValueError):
            EquationSolver(True, 2, 1).solve()

    def test_condition_coverage_bool_b(self):
        with self.assertRaises(ValueError):
            EquationSolver(1, False, 1).solve()

    def test_condition_coverage_bool_c(self):
        with self.assertRaises(ValueError):
            EquationSolver(1, 2, True).solve()

    def test_condition_coverage_valid_int_and_float_values(self):
        result = EquationSolver(1.0, -3, 2.0).solve()

        self.assertAlmostEqual(result[0], 2.0)
        self.assertAlmostEqual(result[1], 1.0)

    # 4. Boundary value analysis
    def test_boundary_value_a_negative_near_zero(self):
        solver = EquationSolver(-0.001, 0, 1)
        x1, x2 = solver.solve()

        self.assertAlmostEqual(x1, -31.6227766017, places=6)
        self.assertAlmostEqual(x2, 31.6227766017, places=6)

    def test_boundary_value_a_positive_near_zero(self):
        solver = EquationSolver(0.001, 0, 1)
        x1, x2 = solver.solve()

        self.assertComplexAlmostEqual(x1, complex(0.0, 31.6227766017), places=6)
        self.assertComplexAlmostEqual(x2, complex(0.0, -31.6227766017), places=6)

    def test_boundary_value_delta_near_zero_negative(self):
        solver = EquationSolver(1, 1.999, 1)
        x1, x2 = solver.solve()

        self.assertIsInstance(x1, complex)
        self.assertIsInstance(x2, complex)
        self.assertAlmostEqual(x1.real, -0.9995, places=6)
        self.assertAlmostEqual(x2.real, -0.9995, places=6)

    def test_boundary_value_delta_near_zero_positive(self):
        solver = EquationSolver(1, 2.001, 1)
        x1, x2 = solver.solve()

        self.assertIsInstance(x1, float)
        self.assertIsInstance(x2, float)
        self.assertAlmostEqual(x1, -0.9688732708, places=6)
        self.assertAlmostEqual(x2, -1.0321267292, places=6)

    # 5. Equivalence partitioning
    def test_equivalence_partition_valid_real_roots(self):
        x1, x2 = EquationSolver(1, -4, 3).solve()

        self.assertAlmostEqual(x1, 3.0)
        self.assertAlmostEqual(x2, 1.0)

    def test_equivalence_partition_valid_double_root(self):
        result = EquationSolver(4, 4, 1).solve()

        self.assertAlmostEqual(result, -0.5)

    def test_equivalence_partition_valid_complex_roots(self):
        x1, x2 = EquationSolver(1, 0, 4).solve()

        self.assertComplexAlmostEqual(x1, complex(0.0, 2.0))
        self.assertComplexAlmostEqual(x2, complex(0.0, -2.0))

    def test_equivalence_partition_invalid_non_numeric(self):
        invalid_values = [
            ("a", 1, 1),
            (1, "b", 1),
            (1, 1, "c"),
            (None, 1, 1),
            (1, [], 1),
            (1, 1, {})
        ]

        for a, b, c in invalid_values:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    EquationSolver(a, b, c).solve()

    # 6. Category partitioning
    def test_category_partitioning_coefficient_types(self):
        categories = [
            (1, 2, 1, True),
            (1.0, 2.0, 1.0, True),
            (True, 2, 1, False),
            (1, False, 1, False),
            (1, 2, True, False),
            ("1", 2, 1, False)
        ]

        for a, b, c, should_be_valid in categories:
            with self.subTest(a=a, b=b, c=c):
                if should_be_valid:
                    self.assertIsNotNone(EquationSolver(a, b, c).solve())
                else:
                    with self.assertRaises(ValueError):
                        EquationSolver(a, b, c).solve()

    def test_category_partitioning_delta_categories(self):
        categories = [
            (1, 0, 1, "negative_delta"),
            (1, 2, 1, "zero_delta"),
            (1, -3, 2, "positive_delta")
        ]

        for a, b, c, category in categories:
            with self.subTest(category=category):
                result = EquationSolver(a, b, c).solve()

                if category == "negative_delta":
                    self.assertIsInstance(result[0], complex)
                    self.assertIsInstance(result[1], complex)
                elif category == "zero_delta":
                    self.assertIsInstance(result, float)
                    self.assertAlmostEqual(result, -1.0)
                else:
                    self.assertIsInstance(result, tuple)
                    self.assertAlmostEqual(result[0], 2.0)
                    self.assertAlmostEqual(result[1], 1.0)

    # 7. Path coverage
    def test_path_coverage_invalid_type_path(self):
        with self.assertRaises(ValueError):
            EquationSolver([], 2, 1).solve()

    def test_path_coverage_a_zero_path(self):
        with self.assertRaises(ValueError):
            EquationSolver(0, 2, 1).solve()

    def test_path_coverage_delta_negative_path(self):
        result = EquationSolver(1, 2, 10).solve()

        self.assertIsInstance(result, tuple)
        self.assertIsInstance(result[0], complex)
        self.assertIsInstance(result[1], complex)

    def test_path_coverage_delta_zero_path(self):
        result = EquationSolver(9, 6, 1).solve()

        self.assertAlmostEqual(result, -1 / 3)

    def test_path_coverage_delta_positive_path(self):
        x1, x2 = EquationSolver(2, -7, 3).solve()

        self.assertAlmostEqual(x1, 3.0)
        self.assertAlmostEqual(x2, 0.5)

    # 8. Mutation testing / killMutants
    def test_kill_mutant_accepts_bool_as_number(self):
        with self.assertRaises(ValueError):
            EquationSolver(True, 2, 1).solve()

    def test_kill_mutant_allows_a_zero(self):
        with self.assertRaises(ValueError):
            EquationSolver(0, 1, 1).solve()

    def test_kill_mutant_delta_sign_logic(self):
        complex_result = EquationSolver(1, 0, 1).solve()
        real_result = EquationSolver(1, -3, 2).solve()

        self.assertIsInstance(complex_result[0], complex)
        self.assertAlmostEqual(real_result[0], 2.0)
        self.assertAlmostEqual(real_result[1], 1.0)

    def test_kill_mutant_double_root_returns_single_value(self):
        result = EquationSolver(1, -2, 1).solve()

        self.assertNotIsInstance(result, tuple)
        self.assertAlmostEqual(result, 1.0)

    def test_kill_mutant_wrong_quadratic_formula(self):
        x1, x2 = EquationSolver(1, -5, 6).solve()

        self.assertAlmostEqual(x1, 3.0)
        self.assertAlmostEqual(x2, 2.0)
        self.assertNotAlmostEqual(x1, -3.0)
        self.assertNotAlmostEqual(x2, -2.0)

    # Verificare console output
    def test_solve_does_not_print_anything_for_valid_case(self):
        output = io.StringIO()

        with redirect_stdout(output):
            result = EquationSolver(1, -5, 6).solve()

        self.assertEqual(output.getvalue(), "")
        self.assertAlmostEqual(result[0], 3.0)
        self.assertAlmostEqual(result[1], 2.0)

    def test_solve_does_not_print_anything_for_invalid_case(self):
        output = io.StringIO()

        with redirect_stdout(output):
            with self.assertRaises(ValueError):
                EquationSolver("invalid", 2, 1).solve()

        self.assertEqual(output.getvalue(), "")


if __name__ == "__main__":
    unittest.main(verbosity=2)