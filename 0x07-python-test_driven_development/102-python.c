#include <Python3.4/python.h>
void print_python_string(PyObject *p) {
    // Check if the object is a string
    if (!PyUnicode_Check(p)) {
        printf("[ERROR] Invalid String Object\n");
        return;
    }

    // Extract string information
    Py_ssize_t length;
    const char *value = PyUnicode_AsUTF8AndSize(p, &length);

    // Determine the type of the string object
    const char *type;
    if (PyUnicode_IS_COMPACT_ASCII(p)) {
        type = "compact ascii";
    } else if (PyUnicode_IS_COMPACT(p)) {
        type = "compact unicode object";
    } else {
        type = "string object";
    }

    // Print string object info
    printf("[.] string object info\n");
    printf("  type: %s\n", type);
    printf("  length: %zd\n", length);
    printf("  value: %s\n", value);
}
