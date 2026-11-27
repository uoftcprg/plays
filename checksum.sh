find plays -type f ! -name .gitignore ! -name .gitattributes | sort | xargs sha256sum > SHA256SUMS
