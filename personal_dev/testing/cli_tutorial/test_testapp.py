def test_initial_transform(generate_initial_transfrom_parameters):
    test_input = generate_initial_transform_parameters[0]
    expected_output = generate_initial_transform_parameters[1]
    asssert app.initial_transform(test_input) == expected_output
