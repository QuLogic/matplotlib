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

        .def("copy", [](const Eigen::Affine2d& self) {
            return Eigen::Affine2d(self);
        })
        .def("__copy__", [](const Eigen::Affine2d& self) {
            return Eigen::Affine2d(self);
        })
        .def("__deepcopy__", [](const Eigen::Affine2d& self, py::dict) {
            return Eigen::Affine2d(self);
        }, "memo"_a)
        .def(py::pickle(
            [](const Eigen::Affine2d &self) { // __getstate__
                return py::make_tuple(
                    self(0, 0), self(0, 1), self(0, 2),
                    self(1, 0), self(1, 1), self(1, 2));
            },
            [](const py::tuple& t) { // __setstate__
                if (t.size() != 6) {
                    throw std::runtime_error("Invalid state!");
                }

                Eigen::Affine2d ret;

                ret(0, 0) = t[0].cast<double>();
                ret(0, 1) = t[1].cast<double>(); 
                ret(0, 2) = t[2].cast<double>();

                ret(1, 0) = t[3].cast<double>(); 
                ret(1, 1) = t[4].cast<double>(); 
                ret(1, 2) = t[5].cast<double>();

                ret.makeAffine();

                return ret;
            }
        ))

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

        .def("__matmul__", [](const Eigen::Affine2d& self, const Eigen::Affine2d& other) {
            return self * other;
        }, "other"_a,
        "Combines two transforms.")

        .def("remove_translate", [](Eigen::Affine2d& self) {
            self(0, 2) = 0.0;
            self(1, 2) = 0.0;
        },
        "Remove the translation part of a transform.")

        .def("reset", [](Eigen::Affine2d& self) {
            self.setIdentity();
        },
        "Reset to the identity transformation.")

        .def("rotate", [](Eigen::Affine2d& self, double theta) {
            self.prerotate(theta);
        }, "theta"_a,
        "Add a rotation (in radians) to this transform in place.")

        .def("scale", [](Eigen::Affine2d& self, double sx, double sy) {
            self.prescale(Eigen::Vector2d(sx, sy));
        }, "sx"_a, "sy"_a,
        "Add a scale in place.")

        .def("skew", [](Eigen::Affine2d& self, double xShear, double yShear) {
            // Transform.preshear appears to be buggy in Eigen 3.4, so do this manually.
            auto skew = Eigen::Affine2d::Identity();
            skew.shear(tan(yShear), tan(xShear));
            self = skew * self;
        }, "xShear"_a, "yShear"_a,
        "Add a skew in place.")

        .def("translate", [](Eigen::Affine2d& self, double tx, double ty) {
            self.pretranslate(Eigen::Vector2d(tx, ty));
        }, "tx"_a, "ty"_a,
        "Add a translation in place.")

        .def("affine_transform",
            [](const Eigen::Affine2d& self, Eigen::Ref<const Eigen::Vector2d> vertices) {
                Eigen::Vector2d result = self * vertices;
                return result;
            }
        )
        .def("affine_transform",
            [](const Eigen::Affine2d& self, py::array_t<double> vertices_arr) {
                auto vertices = vertices_arr.attr("transpose")().cast<Eigen::Ref<const Eigen::Matrix2Xd>>();
                auto result = py::cast(self * vertices, py::return_value_policy::move);
                return result.attr("transpose")();
            }
        )
    ;
}
