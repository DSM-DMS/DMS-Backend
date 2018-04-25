import unittest as ut

from app import app


def run_v1_test():
    all_tests = ut.TestLoader().discover('tests_v1', 'test_*.py')
    ut.TextTestRunner().run(all_tests)


def run_v2_test():
    all_tests = ut.TestLoader().discover('tests_v2', 'test_*.py')
    ut.TextTestRunner().run(all_tests)


if __name__ == '__main__':
    app.testing = True

    run_v1_test()
    run_v2_test()
