// Matrix operations we need:
// .copy()
// check if [0, 0] != [1, 1]
// re-set a, b, c, d, e, f
// convert to NumPy matrix
// reset to identity
// rotate in place
// translate in place
// scale in place
// skew in place
// dot two matrices

#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include <Eigen/Geometry>

namespace py = pybind11;
using namespace pybind11::literals;

PYBIND11_MODULE(_eigen, m) {
    py::class_<Eigen::Affine2d>(m, "Affine2d")
        .def(py::init([]() {
            return Eigen::Affine2d::Identity();
        }))
        .def(py::init([](const Eigen::Matrix3d& matrix) {
            return Eigen::Affine2d(matrix);
        }),
        "matrix"_a.none(false))

        .def("get_matrix", [](const Eigen::Affine2d& self) {
            return self.matrix();
        })
        .def_property_readonly("is_diagonal", [](const Eigen::Affine2d& self) {
            return self.matrix().isDiagonal();
        })
        .def("__call__", [](const Eigen::Affine2d& self, py::ssize_t i, py::ssize_t j) {
            if (i < 0 || i >= 3) {
                throw std::out_of_range(
                    "Index i (" + std::to_string(i) + ") out of range");
            }
            if (j < 0 || j >= 3) {
                throw std::out_of_range(
                    "Index j (" + std::to_string(j) + ") out of range");
            }
            return self(i, j);
        }, "i"_a, "j"_a)
    ;
}
