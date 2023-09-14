#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject *
print_hello(PyObject *self, PyObject *args)
{
    // const char *command;
    // int sts;

    // if (!PyArg_ParseTuple(args, "s", &command))
    //     return NULL;
    // sts = system(command);
    printf("This line come from printf\n");
    return Py_BuildValue("s", "Hello World!");
}

static PyMethodDef mydemoMethods[] = {
    {"print_hello",  print_hello, METH_VARARGS,
     "Print some text (Hello world)"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "mydemo",   /* name of module */
    "this is some mydemo's doc", /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    mydemoMethods
};

PyMODINIT_FUNC
PyInit_mydemo(void)
{
    PyObject *m;

    m = PyModule_Create(&spammodule);
    if (m == NULL)
        return NULL;

    return m;
}
