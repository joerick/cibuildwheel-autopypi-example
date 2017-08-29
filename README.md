cibuildwheel auto-deploy to PyPI example
========================================

Travis setup
------------

- Add an `env` section to your `.travis.yml`

      env:
        global:
          - TWINE_USERNAME=...your pypi username...
          # Note: TWINE_PASSWORD is set in Travis settings

  And add an upload step to the `script` section

      script:
        - pip install cibuildwheel==x.x.x
        - cibuildwheel --output-dir wheelhouse
        - |
          if [[ $TRAVIS_TAG ]]; then
            python -m pip install twine
            python -m twine upload wheelhouse/*.whl
          fi

  Check this repo's [.travis.yml](.travis.yml) as an example.

- In the Travis web UI, go to your project settings and add the environment variable `TWINE_PASSWORD`, set to your PyPI password.

Appveyor setup
--------------

- Add this env to your appveyor.yml

      environment:
        TWINE_USERNAME: ...your pypi username...
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

- In the Appveyor UI, add your PyPI password as `TWINE_PASSWORD` (click Settings > Environment > Add Variable...). Make sure to mark it as private!

On each release
---------------

- Bump the version number in `setup.py` and anywhere else it occurs (I use [`bumpversion`](https://github.com/peritus/bumpversion) for this)
- Commit these changes, tag that commit, and push to Github (don't forget to push the tag! `git push --tags`). Your wheels will start building.
- Locally, build a source distribution with `rm -rf dist && python setup.py sdist`
- Upload the source distribution using `twine upload dist/*.tar.gz`

Your wheels will build in Travis/Appveyor and push to PyPI when ready.
