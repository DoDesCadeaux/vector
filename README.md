# Vector Library for Python

Welcome to the Vector Library for Python! This lightweight library is designed to facilitate basic vector manipulations for educational and professional use.

## Features

- **Vector Addition**: Sum two vectors with matching dimensions.
- **Vector Subtraction**: Subtract one vector from another of the same dimensions.
- **Scalar Multiplication and Division**: Easily scale vectors by multiplying or dividing with a scalar value.
- **Dot Product**: Compute the dot product between two compatible vectors.
- **Vector Transposition**: Switch between row and column vector representations.

## Installation

To get started with this library, clone this repository to your local machine using:

```bash
git clone https://github.com/DoDesCadeaux/vector.git
```

## Usage
Here's a quick example on how to use the library:

```python
from vector import Vector

# Create two column vectors
v1 = Vector([[1], [2], [3]])
v2 = Vector([[4], [5], [6]])

# Create two row vectors
v3 = Vector([[5.0, 6.0, 7.0]])
v4 = Vector([[10.0, 13.0, 19.0]]) * 2

# Add the vectors
v5 = v1 + v2
print(v5)
# Output
# Vector([[5], [7], [9]]) of shape (3, 1)

# Show vector product
print(v4)
# Output
# Vector([[20.0, 26.0, 38.0]]) of shape (1, 3)
```

## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

## Fork the Project
1. Create your Feature Branch  ```git checkout -b feature/AmazingFeature```
2. Commit your Changes  ```git commit -m 'Add some AmazingFeature'```
3. Push to the Branch  ```git push origin feature/AmazingFeature```
4. Open a Pull Request
