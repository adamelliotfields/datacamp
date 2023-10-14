jupyter_opts := --IdentityProvider.token='' --ServerApp.password='' --ServerApp.disable_check_xsrf=True --ServerApp.use_redirect_file=False --ServerApp.root_dir="${PWD}/notebooks"
jupyter_opts_codespace := --ServerApp.allow_origin='*' --ServerApp.custom_display_url="https://${CODESPACE_NAME}-8888.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}" --ip=0.0.0.0 --no-browser

.PHONY: jupyter venv pip

jupyter:
ifeq ($(CODESPACES), true)
	@jupyter lab $(jupyter_opts) $(jupyter_opts_codespace)
else
	@jupyter lab $(jupyter_opts)
endif

venv:
	@python -m venv venv

pip:
	@python -m pip install -r requirements.txt
