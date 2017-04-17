cibuildwheel auto-deploy to PyPI example
========================================

Setup
-----

- Add to your `.travis.yml`

        env:
          - TWINE_USERNAME=joerick
          - TWINE_PASSWORD=from-travis-settings

        deploy:
          provider: script
          script:
            - pip install twine
            - twine upload wheelhouse/*.whl
          on:
            tags: true

- In the Travis web UI, go to your project settings and add the environment variable TWINE_PASSWORD, set to your PyPI password.

On each release
---------------

- Bump the version number in `setup.py` and anywhere else it occurs (I use [`bumpversion`](https://github.com/peritus/bumpversion) for this)
- Commit these changes, tag that commit, and push to Github (don't forget to push the tag! `git push --tags`)
- Locally, build a source distribution with `rm -rf dist && python setup.py sdist`
- Upload the source distribution using `twine upload dist/*.tar.gz`

Your wheels will build in Travis/Appveyor and push to PyPI when ready.