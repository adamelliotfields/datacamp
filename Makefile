poetry_path := $(shell command -v poetry 2>/dev/null)
npm_path := $(shell command -v npm 2>/dev/null)

# Setting the token to an empty string disables authentication and thus makes the redirect file unnecessary.
# When running in a Codespace, it will still be behind GitHub authentication unless you explicitly make it public.
# https://docs.github.com/en/codespaces/developing-in-codespaces/forwarding-ports-in-your-codespace
jupyter_opts := --IdentityProvider.token='' --ServerApp.password='' --ServerApp.disable_check_xsrf=True --ServerApp.use_redirect_file=False --ServerApp.root_dir="${PWD}/notebooks"
jupyter_opts_codespace := --ServerApp.allow_origin='*' --ServerApp.custom_display_url="https://${CODESPACE_NAME}-8888.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}" --ip=0.0.0.0 --no-browser

.PHONY: poetry jupyter

# requires ~/.local/bin to be in your $PATH
poetry:
ifdef poetry_path
	@poetry env use $(shell which python)
	@poetry install
else
	@python -m pip install --user poetry
	@poetry env use $(shell which python)
	@poetry install
endif

# jupysql sends telemetry to posthog, which is blocked by adguard, and the errors will spam your notebook
# https://docs.ploomber.io/en/latest/community/user-stats.html
jupyter:
ifeq ($(CODESPACES), true)
	@PLOOMBER_STATS_ENABLED=false poetry run jupyter lab $(jupyter_opts) $(jupyter_opts_codespace)
else
	@PLOOMBER_STATS_ENABLED=false poetry run jupyter lab $(jupyter_opts)
endif
