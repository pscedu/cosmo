For using the Anaconda environment for the project:

    # Load the API development environment
    source activate api_development environment

For running the test suite on the code:

    cd /path/to/project/
    python -m pytest
    

    ======================================= test session starts =======================================
    platform linux -- Python 3.8.3, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
    rootdir: /cosmo/repo/aibd-cosmo/api
    collected 9 items                                                                                 

    test_main.py .........                                                                      [100%]

    ======================================== warnings summary =========================================
    test_main.py::test_get_length
    test_main.py::test_get_length_invalid_haloid
    test_main.py::test_get_length_invalid_typeid
    test_main.py::test_get_index
    test_main.py::test_get_index_invalid_haloid
      /cosmo/anaconda/cosmo/lib/python3.8/site-packages/bigfile/__init__.py:346: DeprecationWarning: BigFile deprecated, use <class 'bigfile.File'> instead
        warnings.warn('%s deprecated, use %s instead' % (name, origin), DeprecationWarning)

    -- Docs: https://docs.pytest.org/en/latest/warnings.html
    ================================== 9 passed, 5 warnings in 0.58s ==================================
