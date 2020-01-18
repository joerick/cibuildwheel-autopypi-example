cibuildwheel auto-deploy to PyPI example
========================================

Travis setup
------------

- Add an `env` section to your `.travis.yml`

      env:
        global:
          - TWINE_USERNAME=__token__
          # Note: TWINE_PASSWORD is set to an API token in Travis settings

  Install `cibuildwheel` and `twine` in your `install` section

      install:
        - python -m pip install twine cibuildwheel==x.y.z

  Build in the `script` section

      script:
        - python -m cibuildwheel --output-dir wheelhouse

  Finally, upload if the build was successful

       after_success:
         - if [[ $TRAVIS_TAG ]]; then python -m twine upload wheelhouse/*.whl; fi

  Check this repo's [.travis.yml](.travis.yml) as an example.

- Generate a [PyPI API token](https://pypi.org/help/#apitoken)
- In the Travis web UI, go to your project settings and add the environment variable `TWINE_PASSWORD`, set to your new PyPI API token.

Appveyor setup
--------------

- Add this env to your appveyor.yml

      environment:
        TWINE_USERNAME: __token__
        # Note: TWINE_PASSWORD is set in Appveyor settings

    Add this upload step to the `build_script`:

      build_script:
        - pip install cibuildwheel==x.x.x
        - cibuildwheel --output-dir wheelhouse
        - >
          IF "%APPVEYOR_REPO_TAG%" == "true"
          (
          python -m pip install twine
          &&
          python -m twine upload wheelhouse/*.whl
          )

  Check this repo's [appveyor.yml](appveyor.yml) as an example.

- Generate a [PyPI API token](https://pypi.org/help/#apitoken)
- In the Appveyor UI, add your new API token as `TWINE_PASSWORD` (click Settings > Environment > Add Variable...). Make sure to mark it as private!

On each release
---------------

- Bump the version number in `setup.py` and anywhere else it occurs (I use [`bumpversion`](https://github.com/peritus/bumpversion) for this)
- Commit these changes, tag that commit, and push to Github (don't forget to push the tag! `git push --tags`). Your wheels will start building.
- Locally, build a source distribution with `rm -rf dist && python setup.py sdist`
- Upload the source distribution using `twine upload dist/*.tar.gz`

Your wheels will build in Travis/Appveyor and push to PyPI when ready.
