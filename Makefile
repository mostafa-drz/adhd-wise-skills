.PHONY: check validate dist deps

deps:
	@python3 -c "import yaml" 2>/dev/null || pip install pyyaml

# House rules, frontmatter, and claim language.
check:
	@python3 scripts/check_skills.py

# Claude Code's own validator for the marketplace and every plugin in it.
validate:
	@claude plugin validate .
	@for p in plugins/*/; do claude plugin validate "$$p" || exit 1; done

dist: check
	@python3 scripts/build_dist.py
