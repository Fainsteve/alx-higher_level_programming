def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list): First matrix to be multiplied.
        m_b (list): Second matrix to be multiplied.

    Returns:
        list: Result of multiplying the two matrices.

    Raises:
        TypeError: If either of the inputs is not a list or a list of lists,
            or if an element in either list is not an integer or a float, or if
            the rows in either list are not all the same size.
        ValueError: If either of the inputs is an empty list or a list of empty lists,
            or if the two matrices cannot be multiplied together.

    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty" if len(m_a) == 0 else "m_b can't be empty")
    if any(not isinstance(row, list) for row in m_a) or any(not isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists" if any(not isinstance(row, list) for row in m_a)
                        else "m_b must be a list of lists")
    if any(len(row) == 0 for row in m_a) or any(len(row) == 0 for row in m_b):
        raise ValueError("m_a can't be empty" if any(len(row) == 0 for row in m_a)
                         else "m_b can't be empty")
    if any(any(not isinstance(val, (int, float)) for val in row) for row in m_a) or any(
            any(not isinstance(val, (int, float)) for val in row) for row in m_b):
        raise TypeError("m_a should contain only integers or floats" if any(
            any(not isinstance(val, (int, float)) for val in row) for row in m_a)
                        else "m_b should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size" if any(len(row) != len(m_a[0]) for row in m_a)
                        else "each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for col in range(len(m_b[0]))] for row in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result

