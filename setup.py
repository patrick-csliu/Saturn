from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name="testpackage.mydemo",  # as it would be imported
                            # may include packages/namespaces separated by `.`

            sources=["./src/c/mydemo.c"], # all sources are compiled into a single binary file
        ),
    ]
)
