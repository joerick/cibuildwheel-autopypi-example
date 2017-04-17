cibuildwheel auto-deploy to PyPI example
========================================

Travis setup
------------

- Add to your `.travis.yml`

        env:
          - TWINE_USERNAME=...your pypi username...
          # Note: TWINE_PASSWORD is set in Travis settings

        deploy:
          provider: script
          script:
            - pip install twine
            - twine upload wheelhouse/*.whl
          on:
            tags: true

- In the Travis web UI, go to your project settings and add the environment variable TWINE_PASSWORD, set to your PyPI password.

Appveyor setup
--------------

- Add this to your appveyor.yml

		environment:
		  TWINE_USERNAME: joerick
		  # Note: TWINE_PASSWORD is set in Appveyor settings
		
		deploy_script:
		  - pip install twine
		  - twine upload wheelhouse/*.whl

On each release
---------------

- Bump the version number in `setup.py` and anywhere else it occurs (I use [`bumpversion`](https://github.com/peritus/bumpversion) for this)
- Commit these changes, tag that commit, and push to Github (don't forget to push the tag! `git push --tags`). Your wheels will start building.
- Locally, build a source distribution with `rm -rf dist && python setup.py sdist`
- Upload the source distribution using `twine upload dist/*.tar.gz`

Your wheels will build in Travis/Appveyor and push to PyPI when ready.
